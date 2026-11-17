# ETAPA 3 · VERIFICACIÓN DE PÓLIZAS

Capa 2 (flujo). Se activa cuando llegan las pólizas emitidas. Es la etapa donde más importa el rigor.

## Paso 1. Inventario

1. Pide que deje las pólizas y los certificados de pago en `obras/<obra>/04_polizas/` (por versión: `v1/`, `v2/`...). Nunca trabajes sobre el original fuera de la carpeta de la obra.
2. Lista las **pólizas que deberían existir** según la Etapa 1 (`02_etapa1/resultado_etapa1.json`): FCC, RC, TRC y, si corresponde, garantía adicional o anticipo. Marca las que faltan.
3. Para cada póliza, verifica que esté su certificado de pago.

## Paso 2. Leer la póliza entera

- Las pólizas suelen venir escaneadas. Léelas página por página.
- **Montos, RUT y fechas se leen dos veces.** Si un dígito no es legible, es NO VERIFICADO; no lo adivines.
- Anota en qué página está cada dato.

## Paso 3. Verificar

Aplica `memoria/conocimiento/checklist_verificacion.md`: el bloque común más el bloque del tipo de póliza. La referencia es la ficha de la Etapa 1, contrastada con la resolución y las bases. Nunca verifiques "de memoria".

Clasifica cada hallazgo:
- **CRÍTICO:** Fiscalía la rechazaría o el MOP no podría cobrarla.
- **FORMAL:** dato incorrecto que requiere un endoso.
- **LEVE:** inconsistencia menor; Fabiana decide si se pide corregir.
- **HUMANO:** firma del certificado y del apoderado, condiciones de cobertura (sublímites, cláusulas restrictivas): se le pregunta a Fabiana.
- **NO VERIFICADO:** falta información o algo no se lee.

Antes de dar un CRÍTICO o un FORMAL, revisa `memoria/aprendizajes.md`: puede que Fabiana ya te haya dicho que algo así Fiscalía lo acepta.

## Paso 4. Generar la copia anotada y el informe

1. Escribe `05_informes/<poliza>_v<N>_hallazgos.json` con este formato:
```json
{"poliza": "FCC HDI 16-118079", "obra": "Ruta B-12 Mejillones", "version": 1,
 "hallazgos": [{"n": 1, "severidad": "CRITICO", "pagina": 1, "campo": "Monto asegurado",
   "dice": "4.347,73 UF", "debe_decir": "4.374,73 UF", "fuente": "Ficha Etapa 1; Resolución resuelvo 6°",
   "zona": [0.62, 0.66, 0.93, 0.70]}]}
```
   `zona` (opcional) es el rectángulo en la página, en fracciones de 0 a 1 (izquierda, arriba, derecha, abajo). Si no estás seguro de la ubicación, omítela: la nota irá al margen.
2. Corre `python herramientas/anotar_poliza.py "<poliza.pdf>" <hallazgos.json> 05_informes/<poliza>_v<N>_revisada.pdf`.
3. Se generan: la copia anotada (con una franja lateral de notas y el informe al final) y un `_informe.txt` para copiar al correo.
4. Abre la copia anotada y revisa que las marcas queden donde corresponde.

## Paso 5. Presentar a Fabiana

> "Revisé la [póliza]: [X] críticos, [Y] formales, [Z] leves. Lo más importante: [1 o 2 líneas]. Necesito que revises: la firma del certificado de pago y la del apoderado. El informe para la aseguradora está en [ruta]."

- Nunca digas que está aprobada. Si no hay hallazgos: "Sin hallazgos en lo que revisé. Falta tu revisión de las firmas."
- Si Fabiana dice que un hallazgo no importa (por ejemplo, "eso Fiscalía siempre lo acepta"), anótalo en `aprendizajes.md` y en adelante márcalo como LEVE con esa nota. No lo dejes de revisar (regla 8 del núcleo).

## Paso 6. Ciclo de correcciones

Cuando llegue la versión corregida, guárdala en `v2/` y revisa **toda la póliza de nuevo**, no solo los puntos corregidos (al corregir a veces se introducen errores nuevos). En el informe, indica qué se corrigió y qué sigue pendiente.

Cuando no queden hallazgos y Fabiana confirme las firmas, actualiza `estado.md`: "Etapa 3: completada; lista para que Fabiana entregue al MOP".
