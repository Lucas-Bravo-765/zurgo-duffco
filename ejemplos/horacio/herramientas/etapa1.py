#!/usr/bin/env python3
"""
Etapa 1: cálculo de montos y vigencias de pólizas y llenado de formatos.

Replica las fórmulas del Excel MAESTRO de Fabiana (verificado con el caso Ruta B-12).

Uso:
  python herramientas/etapa1.py uf-necesarias  obras/<obra>/02_etapa1/ficha.json
  python herramientas/etapa1.py calcular       obras/<obra>/02_etapa1/ficha.json
  python herramientas/etapa1.py generar        obras/<obra>/02_etapa1/ficha.json

La ficha la arma el agente leyendo los documentos (ver memoria/flujo/etapa1.md).
Los valores de UF los agrega el agente desde una fuente oficial o los entrega Fabiana.
"""
import json, math, shutil, sys
from datetime import date, datetime, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PLANTILLAS = RAIZ / "plantillas"

MESES = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO",
         "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]


def d(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


def ultimo_dia_mes_anterior(f):
    return date(f.year, f.month, 1) - timedelta(days=1)


def round2(x):
    # Excel ROUND (mitad hacia arriba)
    return math.floor(x * 100 + 0.5) / 100


def roundup2(x):
    # Excel ROUNDUP a 2 decimales (con tolerancia a errores de coma flotante)
    return math.ceil(round(x * 100, 6)) / 100


def fmt_fecha(f, sep="/"):
    return f.strftime(f"%d{sep}%m{sep}%Y")


def fmt_pesos(n):
    return "$" + f"{int(n):,}".replace(",", ".")


def fmt_uf(x):
    s = f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s


def fecha_larga(f):
    return f"{f.day} DE {MESES[f.month - 1]} DE {f.year}"


def cargar(ruta):
    with open(ruta, encoding="utf-8") as fh:
        return json.load(fh)


def calcular(ficha):
    f_tec = d(ficha["fecha_apertura_tecnica"])
    f_tram = d(ficha["fecha_tramitacion"])
    plazo = int(ficha["plazo_dias"])
    monto = float(ficha["monto_contrato"])
    po = float(ficha.get("presupuesto_oficial") or 0)

    inicio = f_tram + timedelta(days=1)            # MAESTRO B14 = B13 + 1
    termino = inicio + timedelta(days=plazo)       # MAESTRO B16 = B14 + B15
    f_uf_fcc = ultimo_dia_mes_anterior(f_tec)      # MAESTRO C21
    f_uf_tram = ultimo_dia_mes_anterior(f_tram)    # MAESTRO C27 y C33

    uf = ficha.get("uf", {})
    faltan = [str(x) for x in {f_uf_fcc, f_uf_tram} if str(x) not in uf]
    if faltan:
        raise SystemExit("FALTAN VALORES DE UF para: " + ", ".join(sorted(faltan)) +
                         ". Agregarlos en ficha.json -> \"uf\": {\"AAAA-MM-DD\": valor} con su fuente.")
    uf_fcc = float(uf[str(f_uf_fcc)])
    uf_tram = float(uf[str(f_uf_tram)])

    pct_fcc = float(ficha.get("pct_fcc", 0.03))
    pct_rc = float(ficha.get("pct_rc", 0.05))
    pct_trc = float(ficha.get("pct_trc", 1.0))

    fcc = round2(monto * pct_fcc / uf_fcc)          # MAESTRO B23 ROUND
    rc = roundup2(monto * pct_rc / uf_tram)         # MAESTRO B29 ROUNDUP
    trc = roundup2(monto * pct_trc / uf_tram)       # MAESTRO B35 ROUNDUP

    region = ficha["region"].upper()
    direccion = ficha["direccion"].upper()
    fondo = ficha.get("fondo", "Sectorial")
    if fondo.lower().startswith("sector"):
        aseg_fcc = f"SECRETARIO REGIONAL MINISTERIAL DE OBRAS PÚBLICAS, REGIÓN DE {region}"
    else:
        aseg_fcc = f"GOBIERNO REGIONAL DE {region}"
    if ficha.get("nivel_adjudicacion", "regional").lower() == "nacional":
        aseg_fcc = f"DIRECTOR NACIONAL DE {direccion}"
    aseg_mop = f"FISCO DE CHILE - MINISTERIO DE OBRAS PÚBLICAS - DIRECCIÓN DE {direccion}, REGIÓN DE {region}"

    res = ficha["resolucion"]
    texto_res = (f"RESOLUCIÓN {res['servicio']} N°{res['numero']} DEL {fecha_larga(d(res['fecha_emision']))}, "
                 f"TRAMITADO EL {fecha_larga(f_tram)}")
    safi = str(ficha["safi"])
    safi_pts = f"{int(safi):,}".replace(",", ".") if safi.isdigit() else safi
    nombre = ficha["nombre_obra"].upper()
    glosa = f'{nombre}, CÓDIGO SAFI N°{safi_pts}, {texto_res}'
    if ficha.get("bip"):
        glosa_fcc_bip = f', CÓDIGO BIP N°{ficha["bip"]}'
    else:
        glosa_fcc_bip = ""
    glosa_fcc = (f'PARA GARANTIZAR EL FIEL CUMPLIMIENTO DE LA OBRA: "{nombre}" CÓDIGO SAFI: {safi_pts}'
                 f'{glosa_fcc_bip}, {texto_res}.')

    r = {
        "inicio": str(inicio),
        "termino_obra": str(termino),
        "uf_fcc": {"fecha": str(f_uf_fcc), "valor": uf_fcc, "regla": "último día del mes anterior al mes de la apertura técnica"},
        "uf_rc_trc": {"fecha": str(f_uf_tram), "valor": uf_tram, "regla": "último día del mes anterior al mes de la tramitación"},
        "polizas": {
            "FCC": {"asegurado": aseg_fcc, "rut": "61.202.000-0", "monto_uf": fcc, "pct": pct_fcc,
                    "inicio": str(inicio), "termino": str(termino + timedelta(days=732)),
                    "regla_vigencia": "término de obra + 366×2 días (fórmula del MAESTRO; cubre plazo + 24 meses del art. 96 RCOP)",
                    "glosa": glosa_fcc},
            "RC": {"asegurado": aseg_mop, "rut": "61.202.000-0", "monto_uf": rc, "pct": pct_rc,
                   "inicio": str(inicio), "termino": str(termino + timedelta(days=366)),
                   "regla_vigencia": "término de obra + 366 días (fórmula del MAESTRO) [P]", "glosa": glosa},
            "TRC": {"asegurado": aseg_mop, "rut": "61.202.000-0", "monto_uf": trc, "pct": pct_trc,
                    "inicio": str(inicio), "termino": str(termino),
                    "regla_vigencia": "plazo del contrato (resolución de adjudicación)", "glosa": glosa},
        },
        "garantia_adicional": None,
    }
    if po:
        umbral = po * (1 - float(ficha.get("pct_baja_adicional", 0.15)))
        if monto < umbral:
            r["garantia_adicional"] = {
                "aplica": True, "monto_pesos": umbral - monto,
                "monto_uf": roundup2((umbral - monto) / uf_fcc),
                "regla": "RCOP art. 98: (PO × 0,85 − oferta) en UF; vigencia como retenciones (art. 158). Confirmar fecha de UF con Fabiana [P]"}
        else:
            r["garantia_adicional"] = {"aplica": False,
                                       "motivo": f"oferta {fmt_pesos(monto)} no es inferior a PO × 0,85 = {fmt_pesos(umbral)}"}
    r["_ficha"] = {"monto": monto, "plazo": plazo, "nombre": nombre, "region": region, "direccion": direccion,
                   "fondo": fondo, "safi": safi, "texto_res": texto_res, "f_tec": str(f_tec), "f_tram": str(f_tram)}
    return r


def uf_necesarias(ficha):
    f_tec = d(ficha["fecha_apertura_tecnica"])
    f_tram = d(ficha["fecha_tramitacion"])
    return sorted({str(ultimo_dia_mes_anterior(f_tec)), str(ultimo_dia_mes_anterior(f_tram))})


def generar(ficha, ruta_ficha):
    import openpyxl, docx
    r = calcular(ficha)
    fx = r["_ficha"]
    salida = Path(ruta_ficha).parent
    obra_corta = ficha.get("nombre_corto", "obra")

    # 1. MAESTRO
    dst = salida / f"MAESTRO Solicitud de Polizas {obra_corta}.xlsx"
    shutil.copy(PLANTILLAS / "MAESTRO_Solicitud_de_Polizas_PLANTILLA.xlsx", dst)
    wb = openpyxl.load_workbook(dst)
    ws = wb["Calculo de Boletas y Polizas"]
    ws["B3"] = fx["nombre"]
    ws["B4"] = fx["texto_res"]
    ws["B5"] = int(fx["safi"]) if fx["safi"].isdigit() else fx["safi"]
    ws["B6"] = fx["region"]
    ws["B7"] = fx["direccion"]
    ws["B8"] = fx["fondo"]
    ws["B9"] = fx["monto"]
    ws["B12"] = datetime.strptime(fx["f_tec"], "%Y-%m-%d")
    ws["B13"] = datetime.strptime(fx["f_tram"], "%Y-%m-%d")
    ws["B15"] = fx["plazo"]
    ws["B21"] = r["uf_fcc"]["valor"]
    ws["B27"] = r["uf_rc_trc"]["valor"]
    ws["B33"] = r["uf_rc_trc"]["valor"]
    ws["E21"] = "UF ingresada como valor por el agente; fuente en ficha.json"
    wb.save(dst)

    # 2. Datos Conosur (garantía)
    p = r["polizas"]["FCC"]
    dst2 = salida / f"DATOS PARA EMITIR POLIZA DE GARANTIA_CONOSUR {obra_corta}.xlsx"
    shutil.copy(PLANTILLAS / "DATOS_PARA_EMITIR_POLIZA_DE_GARANTIA_CONOSUR_PLANTILLA.xlsx", dst2)
    wb = openpyxl.load_workbook(dst2)
    ws = wb.active
    ws["D8"] = p["asegurado"]
    ws["D22"] = fx["monto"]
    ws["D23"] = f"UF$ {fmt_uf(p['monto_uf'])}"
    ws["D24"] = datetime.strptime(p["inicio"], "%Y-%m-%d")
    ws["D25"] = datetime.strptime(p["termino"], "%Y-%m-%d")
    for c in ("D24", "D25"):
        ws[c].number_format = "dd-mm-yyyy"
    ws["D26"] = p["glosa"]
    wb.save(dst2)

    # 3. Cuestionarios
    rc, trc = r["polizas"]["RC"], r["polizas"]["TRC"]
    mandante = f"FISCO DE CHILE - MINISTERIO DE OBRAS PÚBLICAS, DIRECCIÓN DE {fx['direccion']}, REGIÓN DE {fx['region']}"
    reemplazos = {
        "{{MANDANTE}}": mandante,
        "{{PLAZO_DIAS}}": str(fx["plazo"]),
        "{{RC_INICIO}}": fmt_fecha(d(rc["inicio"])),
        "{{RC_TERMINO}}": fmt_fecha(d(rc["termino"])),
        "{{MONTO_CONTRATO_PESOS}}": fmt_pesos(fx["monto"]),
        "{{RC_MONTO_UF}}": fmt_uf(rc["monto_uf"]),
        "{{TRC_INICIO}}": fmt_fecha(d(trc["inicio"]), "-"),
        "{{TRC_TERMINO}}": fmt_fecha(d(trc["termino"]), "-"),
        "{{TRC_MONTO_UF}}": fmt_uf(trc["monto_uf"]),
        "{{MECANICA_SUELOS}}": ficha.get("mecanica_suelos", "NO APLICA"),
    }
    for plantilla, nombre in [("CUESTIONARIO_RC_CONOSUR_PLANTILLA.docx", f"CUESTIONARIO RC DE OBRA_CONOSUR {obra_corta}.docx"),
                              ("CUESTIONARIO_TRC_CONOSUR_PLANTILLA.docx", f"CUESTIONARIO TODO RIESGO CONSTRUCCION_CONOSUR {obra_corta}.docx")]:
        doc = docx.Document(PLANTILLAS / plantilla)
        for par in doc.paragraphs:
            if "{{" in par.text:
                t = par.text
                for k, v in reemplazos.items():
                    t = t.replace(k, v)
                for run in par.runs[1:]:
                    run.text = ""
                par.runs[0].text = t
        doc.save(salida / nombre)

    out = {k: v for k, v in r.items() if k != "_ficha"}
    with open(salida / "resultado_etapa1.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("uf-necesarias", "calcular", "generar"):
        print(__doc__)
        sys.exit(1)
    accion, ruta = sys.argv[1], sys.argv[2]
    ficha = cargar(ruta)
    if accion == "uf-necesarias":
        print(json.dumps(uf_necesarias(ficha)))
    elif accion == "calcular":
        r = calcular(ficha)
        r.pop("_ficha")
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        r = generar(ficha, ruta)
        print(json.dumps(r, ensure_ascii=False, indent=2))
