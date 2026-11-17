# ETAPA 2 · COMPARACIÓN DE COTIZACIONES

Capa 2 (flujo). Se activa cuando llegan las cotizaciones de Conosur. Tu criterio aquí todavía es bajo: lo construyes con Fabiana. Dilo con naturalidad.

## Paso 1. Reunir

1. Pide que deje en `obras/<obra>/03_cotizaciones/` los correos (.eml o PDF) o archivos de Conosur.
2. Extrae cada oferta: póliza (FCC, RC, TRC...), compañía, monto asegurado, vigencia, prima neta, IVA, prima bruta, tasa si la informan, deducibles, cláusulas restrictivas, condiciones especiales y si es una "oferta modificada" (mejora).
3. Anota también las **compañías que declinaron y su motivo** (zona, tipo de obra, monto expuesto). Es información valiosa.

## Paso 2. Comparar

Por cada póliza, arma una tabla:

| Compañía | Prima neta (UF) | Tasa anual equivalente | % sobre el contrato | Cláusulas restrictivas | Observaciones |
|---|---|---|---|---|---|

- **Tasa anual equivalente** = prima neta / monto asegurado / (días de vigencia / 365). Así se comparan ofertas con vigencias distintas.
- **% sobre el contrato** = prima neta en pesos / monto del contrato. Es la medida que usa el histórico de Fabiana.
- Compara contra `historico/` (primas pagadas por Duffco en obras anteriores) y contra `memoria/criterio/registro_decisiones.md`, buscando obras parecidas: misma dirección (Vialidad, DOH...), zona (altiplano, costa, norte grande), tipo (conservación, puente, obra fluvial) y monto.
- Señala lo que llame la atención: una compañía que cobra bastante más que antes por una obra similar, cláusulas que limitan la cobertura, vigencias que no calzan con la Etapa 1.

## Paso 3. Proponer y conversar

1. Da una primera opinión breve: "A primera vista, para el TRC conviene X porque ... Lo que no sé evaluar todavía es ...".
2. Pregúntale qué opina y qué estás pasando por alto.
3. Escucha. Cada razón que te dé es criterio: anótala en `memoria/criterio/criterio_cotizaciones.md`.

## Paso 4. Registrar la decisión

En `memoria/criterio/registro_decisiones.md` agrega una fila por póliza: fecha, obra (nombre corto), tipo de obra y zona, compañías cotizadas, elegida, prima y tasa elegidas, **por qué** (en palabras de Fabiana) y compañías que declinaron. Sin datos personales.

Actualiza `estado.md`: "Etapa 2: completada; esperando emisión de pólizas".
