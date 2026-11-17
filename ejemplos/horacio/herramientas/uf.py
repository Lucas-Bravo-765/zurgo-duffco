#!/usr/bin/env python3
"""
Obtiene el valor de la UF para una o más fechas desde fuentes públicas.

Uso:
  python herramientas/uf.py 2024-06-30 2025-02-28

Intenta, en orden: mindicador.cl (API pública que replica al Banco Central) y la tabla anual del SII.
Si ninguna responde (por ejemplo, porque el computador no tiene acceso a esos sitios), lo dice:
en ese caso el agente le pide el valor a Fabiana y lo anota con su fuente. Nunca se inventa una UF.
"""
import json, re, sys, urllib.request
from datetime import datetime

UA = {"User-Agent": "Mozilla/5.0 (agente-polizas Duffco)"}


def mindicador(fecha):
    f = datetime.strptime(fecha, "%Y-%m-%d").strftime("%d-%m-%Y")
    with urllib.request.urlopen(urllib.request.Request(f"https://mindicador.cl/api/uf/{f}", headers=UA), timeout=15) as r:
        data = json.load(r)
    serie = data.get("serie") or []
    if serie:
        return float(serie[0]["valor"]), f"mindicador.cl (Banco Central), consulta {datetime.now():%d-%m-%Y}"
    raise ValueError("sin dato")


def sii(fecha):
    dt = datetime.strptime(fecha, "%Y-%m-%d")
    url = f"https://www.sii.cl/valores_y_fechas/uf/uf{dt.year}.htm"
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=15) as r:
        html = r.read().decode("latin-1")
    # La tabla del SII trae un bloque por mes con filas día -> valor. Se busca el mes y luego el día.
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
             "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    bloque = re.split(r'id=["\']mes_', html)
    for b in bloque[1:]:
        if b.lower().startswith(meses[dt.month - 1].lower()):
            m = re.search(rf"<strong>\s*{dt.day}\s*</strong>\s*</th>\s*<td[^>]*>\s*([\d\.]+,\d+)", b)
            if m:
                return float(m.group(1).replace(".", "").replace(",", ".")), f"SII {url}, consulta {datetime.now():%d-%m-%Y}"
    raise ValueError("no encontrado en SII")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    res = {}
    for fecha in sys.argv[1:]:
        for fuente in (mindicador, sii):
            try:
                v, src = fuente(fecha)
                res[fecha] = {"valor": v, "fuente": src}
                break
            except Exception as e:
                res[fecha] = {"error": f"{fuente.__name__}: {e}"}
    print(json.dumps(res, ensure_ascii=False, indent=2))
    if any("error" in v for v in res.values()):
        print("\nNo se pudo obtener al menos un valor. Pedirle el valor a Fabiana (o revisar sii.cl / bcentral.cl) y anotar la fuente.")
