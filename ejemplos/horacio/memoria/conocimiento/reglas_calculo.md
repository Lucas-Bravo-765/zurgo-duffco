# REGLAS DE CÁLCULO · ETAPA 1

Versión: 0.1 | Verificado: 2026-10-17 con el caso Ruta B-12 (la herramienta `etapa1.py` reproduce exactamente el MAESTRO de Fabiana).
Etiquetas: [V] verificado en norma o documento | [P] práctica de Fabiana (su Excel MAESTRO), por confirmar en la primera sesión.
**Regla madre:** la resolución de adjudicación y las bases de cada obra mandan sobre todo lo que sigue. Si dicen algo distinto, se sigue lo que dicen y se avisa a Fabiana.

## Fechas

| Concepto | Regla | Conf. |
|---|---|---|
| Fecha de tramitación | Timbre "TRAMITADO" de la Dirección en la resolución (fecha de total tramitación) | [V] |
| Inicio de obra y de vigencias | Día siguiente a la tramitación | [V] resolución |
| Término de obra | Inicio + plazo en días (fórmula del MAESTRO; da 1 día de margen sobre contar el inicio como día 1) | [P] |
| UF de la FCC | Valor del último día del mes anterior al mes de la apertura técnica | [P] |
| UF de RC y TRC | Valor del último día del mes anterior al mes de la tramitación | [V] TRC (resolución B-12, 8°); [P] RC |

## Montos

| Póliza | Monto | Redondeo | Fuente |
|---|---|---|---|
| Fiel cumplimiento (FCC) | 3% del contrato / UF FCC (Obras Mayores) | 2 decimales, normal | [V] RCOP art. 96; resolución |
| FCC Obras Menores | 5% del contrato | 2 decimales | [V] RCOP art. 96 |
| Responsabilidad civil (RC) | 5% del contrato / UF de la tramitación | 2 decimales hacia arriba | [P] MAESTRO; la resolución remite a bases 5.4.3 y 5.4.6 |
| Todo riesgo de construcción (TRC) | 100% del contrato / UF de la tramitación | 2 decimales hacia arriba | [V] resolución B-12, 8° |
| Garantía adicional | Solo si oferta < presupuesto oficial × 0,85 (o el % de las bases): monto = PO × 0,85 − oferta, en UF | hacia arriba | [V] RCOP art. 98 |
| Anticipo (si se otorga) | 100% del monto anticipado; UF del último día del mes anterior a la emisión de la resolución que aprueba el convenio | | [V] guía DGOP incluida en las bases |

## Vigencias

| Póliza | Término | Fuente |
|---|---|---|
| FCC | Término de obra + 732 días (366 × 2: cubre plazo + 24 meses) | [V] art. 96 (mínimo); [P] fórmula |
| RC | Término de obra + 366 días | [P] |
| TRC | Término de obra (plazo del contrato o prórrogas) | [V] resolución |
| Garantía adicional | Como las retenciones: plazo pendiente + 12 meses (art. 158) | [V] art. 98 y 158 |
| Anticipo | Plazo del contrato + 6 meses | [V] guía DGOP |

## Asegurados y beneficiarios

| Póliza | Nombre | RUT |
|---|---|---|
| FCC, fondos sectoriales, adjudicación regional | SECRETARIO REGIONAL MINISTERIAL DE OBRAS PÚBLICAS, REGIÓN DE [REGIÓN] | 61.202.000-0 |
| FCC, adjudicación nacional | DIRECTOR NACIONAL DE [DIRECCIÓN] | 61.202.000-0 |
| FCC, fondos GORE | GOBIERNO REGIONAL DE [REGIÓN] [P] (fórmula del MAESTRO; confirmar RUT y texto en las bases) | según bases |
| RC y TRC | FISCO DE CHILE - MINISTERIO DE OBRAS PÚBLICAS - DIRECCIÓN DE [DIRECCIÓN], REGIÓN DE [REGIÓN] | 61.202.000-0 |

Nunca se acepta "MINISTERIO DE OBRAS PÚBLICAS DIRECCIÓN GRAL DE OO PP DCYF" como asegurado de una garantía [V guía DGOP].

## Glosa

- FCC: `PARA GARANTIZAR EL FIEL CUMPLIMIENTO DE LA OBRA: "[NOMBRE EXACTO]" CÓDIGO SAFI: [SAFI], RESOLUCIÓN [SERVICIO] N°[N] DEL [FECHA EMISIÓN], TRAMITADO EL [FECHA TRAMITACIÓN].`
- Si las bases piden código BIP (en la B-12 el anexo complementario 5.4.1 lo pide), agregarlo [P: confirmar con Fabiana].
- RC y TRC: `[NOMBRE EXACTO], CÓDIGO SAFI N°[SAFI], RESOLUCIÓN ... TRAMITADO EL ...`
- El nombre se copia **exactamente** como en la resolución (km, llamado, año).
