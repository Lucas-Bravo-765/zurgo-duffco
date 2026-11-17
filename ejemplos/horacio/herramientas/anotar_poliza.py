#!/usr/bin/env python3
"""
Etapa 3: genera la copia anotada de una póliza y el informe de hallazgos.

Uso:
  python herramientas/anotar_poliza.py <poliza.pdf> <hallazgos.json> <salida.pdf>

hallazgos.json (lo escribe el agente):
{
  "poliza": "FCC HDI 16-118079",
  "obra": "Ruta B-12 Mejillones",
  "version": 1,
  "hallazgos": [
    {"n": 1, "severidad": "CRITICO|FORMAL|LEVE|HUMANO|NO_VERIFICADO",
     "pagina": 1, "campo": "Monto asegurado", "dice": "4.347,73 UF",
     "debe_decir": "4.374,73 UF", "fuente": "Ficha Etapa 1 / Resolución 6°",
     "zona": [0.55, 0.62, 0.95, 0.66]}
  ]
}
"zona" es opcional: rectángulo en fracciones de la página [x0, y0, x1, y1] (0 a 1, origen arriba a la izquierda).
Si no se indica, la nota va al margen derecho de la página.

Nunca modifica el original: escribe una copia nueva.
Requiere PyMuPDF (pip install pymupdf). Si no está, genera solo el informe con reportlab.
"""
import json, sys
from datetime import datetime

COLORES = {  # RGB 0-1
    "CRITICO": (0.85, 0.10, 0.10),
    "FORMAL": (0.95, 0.50, 0.05),
    "LEVE": (0.95, 0.80, 0.10),
    "HUMANO": (0.15, 0.40, 0.85),
    "NO_VERIFICADO": (0.45, 0.45, 0.45),
}
ETIQUETA = {"CRITICO": "CRÍTICO", "FORMAL": "FORMAL", "LEVE": "LEVE",
            "HUMANO": "REVISAR (Fabiana)", "NO_VERIFICADO": "NO VERIFICADO"}


def texto_nota(h):
    if h["severidad"] in ("HUMANO", "NO_VERIFICADO"):
        return f'#{h["n"]} {ETIQUETA[h["severidad"]]}: {h["campo"]}. {h.get("debe_decir", "")}'
    return f'#{h["n"]} {ETIQUETA[h["severidad"]]}: {h["campo"]}. Dice: {h.get("dice", "")}. Debe decir: {h.get("debe_decir", "")}'


def informe_lineas(data):
    hs = data["hallazgos"]
    cuenta = {k: sum(1 for h in hs if h["severidad"] == k) for k in COLORES}
    lin = [f'INFORME DE REVISIÓN · {data.get("poliza", "")}',
           f'Obra: {data.get("obra", "")} · Versión revisada: {data.get("version", 1)} · Fecha: {datetime.now():%d-%m-%Y}',
           f'Resumen: {cuenta["CRITICO"]} críticos, {cuenta["FORMAL"]} formales, {cuenta["LEVE"]} leves, '
           f'{cuenta["HUMANO"]} para revisión de Fabiana, {cuenta["NO_VERIFICADO"]} no verificados.', ""]
    if not hs:
        lin.append("Sin hallazgos en lo verificado. Pendiente: revisión humana de firmas.")
    for h in hs:
        lin.append(f'{h["n"]}. [{ETIQUETA[h["severidad"]]}] Pág. {h.get("pagina", "-")} · {h["campo"]}')
        if h.get("dice"):
            lin.append(f'    Dice: {h["dice"]}')
        if h.get("debe_decir"):
            lin.append(f'    Debe decir: {h["debe_decir"]}')
        if h.get("fuente"):
            lin.append(f'    Fuente: {h["fuente"]}')
    lin += ["", "Este informe es una revisión previa. La decisión de aceptar la póliza es de Duffco."]
    return lin


def con_pymupdf(pdf_in, data, pdf_out):
    import pymupdf as fitz
    doc = fitz.open(pdf_in)
    margen = 230  # franja agregada a la derecha de la página para las notas
    ampliadas, libre = {}, {}
    for h in sorted(data["hallazgos"], key=lambda x: (int(x.get("pagina") or 1), (x.get("zona") or [0, 0])[1])):
        p = int(h.get("pagina") or 1) - 1
        if p < 0 or p >= len(doc):
            continue
        page = doc[p]
        if p not in ampliadas:
            W0, H0 = page.rect.width, page.rect.height
            page.set_mediabox(fitz.Rect(0, 0, W0 + margen, H0))
            page.draw_rect(fitz.Rect(W0, 0, W0 + margen, H0), color=None, fill=(0.97, 0.97, 0.97), overlay=True)
            page.insert_text((W0 + 10, 24), "REVISIÓN DEL AGENTE (copia)", fontsize=8, fontname="helv")
            ampliadas[p] = (W0, H0)
            libre[p] = 34
        W0, H0 = ampliadas[p]
        col = COLORES[h["severidad"]]
        deseada = 40
        if h.get("zona"):
            x0, y0, x1, y1 = h["zona"]
            r = fitz.Rect(x0 * W0, y0 * H0, x1 * W0, y1 * H0)
            hl = page.add_rect_annot(r)
            hl.set_colors(stroke=col)
            hl.set_border(width=2)
            hl.update()
            deseada = r.y0
        ny = max(deseada, libre[p])
        txt = texto_nota(h)
        alto = 14 + 10 * (len(txt) // 42 + 1)
        nota = fitz.Rect(W0 + 8, ny, W0 + margen - 8, ny + alto)
        page.draw_rect(nota, color=col, fill=(1, 1, 1), width=1.5, overlay=True)
        page.insert_textbox(nota + (4, 3, -4, -2), txt, fontsize=8, fontname="helv", color=(0, 0, 0))
        if h.get("zona"):
            page.draw_line(fitz.Point(r.x1, (r.y0 + r.y1) / 2), fitz.Point(nota.x0, nota.y0 + 8), color=col, width=1)
        libre[p] = nota.y1 + 6
    # páginas de informe
    lineas = informe_lineas(data)
    porpag = 55
    for i in range(0, len(lineas), porpag):
        pg = doc.new_page(width=595, height=842)
        y = 50
        for j, ln in enumerate(lineas[i:i + porpag]):
            bold = (i == 0 and j == 0)
            pg.insert_text((40, y), ln, fontsize=11 if bold else 9, fontname="helv")
            y += 14
    doc.save(pdf_out, garbage=3, deflate=True)


def con_reportlab(data, pdf_out):
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    c = canvas.Canvas(pdf_out, pagesize=A4)
    y = 800
    for ln in informe_lineas(data):
        if y < 50:
            c.showPage(); y = 800
        c.setFont("Helvetica", 9); c.drawString(40, y, ln); y -= 14
    c.save()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__); sys.exit(1)
    pdf_in, js, pdf_out = sys.argv[1:]
    with open(js, encoding="utf-8") as fh:
        data = json.load(fh)
    try:
        con_pymupdf(pdf_in, data, pdf_out)
        print(f"OK: copia anotada en {pdf_out}")
    except ImportError:
        con_reportlab(data, pdf_out)
        print(f"PyMuPDF no disponible: se generó solo el informe en {pdf_out}")
    txt = pdf_out.rsplit(".", 1)[0] + "_informe.txt"
    with open(txt, "w", encoding="utf-8") as fh:
        fh.write("\n".join(informe_lineas(data)))
    print(f"Informe en texto (para copiar al correo): {txt}")
