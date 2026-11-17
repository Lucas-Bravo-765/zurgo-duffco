# ETAPA 1 · MONTOS, PLAZOS E INFORMACIÓN ADICIONAL

Capa 2 (flujo). Se activa cuando Fabiana dice que llegó una adjudicación nueva.

## Paso 1. Abrir la obra

1. Pregunta el nombre corto de la obra (ej. "Ruta B-12 Mejillones").
2. Crea `obras/<nombre corto>/` con las subcarpetas `01_entrada`, `02_etapa1`, `03_cotizaciones`, `04_polizas`, `05_informes` y un archivo `estado.md` ("Etapa 1: en curso", fecha).
3. Pídele que deje en `01_entrada/`:
   - Acta de apertura técnica
   - Acta de apertura económica
   - Resolución de adjudicación (con su timbre de tramitación)
   - Bases del contrato (incluido el anexo complementario)
   - Propuesta técnica de Duffco
   (El RCOP ya lo tienes en tu conocimiento.)

## Paso 2. Extraer datos y armar la ficha

Lee los documentos y arma `02_etapa1/ficha.json` con este formato:

```json
{
 "nombre_corto": "Ruta B-12 Mejillones",
 "nombre_obra": "nombre EXACTO como aparece en la resolución",
 "resolucion": {"servicio": "DRV. REGIÓN DE ANTOFAGASTA", "numero": "2", "fecha_emision": "2025-02-28"},
 "safi": "401341", "bip": "40058856-0", "region": "Antofagasta", "direccion": "Vialidad",
 "fondo": "Sectorial", "nivel_adjudicacion": "regional",
 "monto_contrato": 5478886204, "presupuesto_oficial": 4400000000,
 "fecha_apertura_tecnica": "2024-07-24", "fecha_tramitacion": "2025-03-20", "plazo_dias": 420,
 "uf": {}
}
```

Dónde está cada dato (detalle en `memoria/conocimiento/reglas_calculo.md`):
- Nombre, número, fechas, SAFI, BIP, monto, plazo, presupuesto oficial: **resolución de adjudicación**.
- Fecha de tramitación: **timbre "TRAMITADO"** en la resolución. Si no la encuentras, pregúntala; no la supongas.
- Fecha de apertura técnica: **acta de apertura técnica**.
- Fondo (Sectorial o GORE): acta técnica ("Financiamiento") o bases 2.10.
- Nivel (regional o nacional): quién firma la resolución (Director Regional o SEREMI = regional).
- Exigencias de cada garantía: resolución (resuelvos de garantías y pólizas) y bases, cláusulas 5.4.x del anexo complementario.

Las bases pueden tener cientos de páginas: **no las leas enteras**. Busca el anexo complementario y las cláusulas 5.4.1, 5.4.3, 5.4.4 y 5.4.6, más 7.14.4 (anticipo) y 7.14.5 (retenciones).

Muéstrale la ficha a Fabiana en una tabla corta, con la fuente de cada dato, y pídele que la confirme.

## Paso 3. Valores de la UF

1. Corre `python herramientas/etapa1.py uf-necesarias obras/<obra>/02_etapa1/ficha.json` para saber qué fechas necesitas.
2. Corre `python herramientas/uf.py <fechas>`.
3. Si falla (sin acceso a internet), usa tu búsqueda web en sii.cl o bcentral.cl si la tienes; si no, pídele los valores a Fabiana.
4. Agrégalos a la ficha en `"uf": {"AAAA-MM-DD": valor}` y anota la fuente en `estado.md`.

## Paso 4. Calcular y generar

1. Corre `python herramientas/etapa1.py generar obras/<obra>/02_etapa1/ficha.json`.
2. Se generan en `02_etapa1/`: el MAESTRO, los Datos para emitir la póliza de garantía (Conosur), el Cuestionario RC, el Cuestionario TRC y `resultado_etapa1.json`.
3. **Revisa el resultado con tu propio criterio** contra la resolución y las bases: ¿el porcentaje de la FCC es el de las bases? ¿Las bases piden algo distinto para RC o TRC? ¿Aplica la garantía adicional? ¿Hay anticipo? Si algo no calza, avisa y no entregues el documento hasta resolverlo.
4. Muéstrale a Fabiana un resumen:

| Póliza | Asegurado | Monto (UF) | Desde | Hasta | Regla |
|---|---|---|---|---|---|

Más: UF usadas (fecha, valor, fuente), si aplica garantía adicional y dónde quedaron los archivos.

## Paso 5. Información adicional

1. Revisa los cuestionarios: cada "SE ADJUNTA..." es un documento por preparar (descripción del proyecto, plano de ubicación, carta Gantt, metodología, programa de mano de obra, vehículos y equipos, presupuesto itemizado).
2. Para cada uno, busca en la propuesta técnica o en las bases dónde está y dile la página.
3. Pregúntale: "¿Conosur pidió algo más para esta obra?"
4. Arma con ella lo que haga falta (extraer páginas a PDF, ordenar en una carpeta `02_etapa1/informacion_adicional/`).
5. Cierra con: "Quedó todo listo en `02_etapa1/` para que lo envíes a Conosur." Actualiza `estado.md`: "Etapa 1: completada; esperando cotizaciones".
