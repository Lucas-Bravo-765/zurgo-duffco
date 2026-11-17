# TRAZABILIDAD ETAPA 1 · Caso Ruta B-12

Versión: 0.1 | Fecha: 2026-10-17 | Fuente: paquete de Fabiana (insumos/polizas/ruta-b12/)
Objetivo: cada campo de cada salida de la Etapa 1 con su origen exacto o la regla que lo calcula. Es la especificación de lo que el agente debe producir.

Etiquetas: [V] verificado en documento o norma | [P] práctica de Fabiana observada en el MAESTRO, por confirmar con ella | [H] hipótesis.

---

## 1. Datos de entrada que el agente extrae

| Dato | Valor B-12 | Fuente | Conf. |
|---|---|---|---|
| Nombre de la obra | CAMINO BÁSICO POR CONSERVACIÓN, RUTA B-12, KM 35 AL KM 55, COMUNA DE MEJILLONES, PROVINCIA DE ANTOFAGASTA, REGIÓN DE ANTOFAGASTA, 2DO LLAMADO, NUEVO 2024 | Resolución de adjudicación, pág. 4 (REF.) y resuelvo 3° | [V] |
| Resolución | DRV Región de Antofagasta N°2 del 28-02-2025 | Resolución, pág. 8 | [V] |
| Fecha de total tramitación | 20-03-2025 | Timbre "TRAMITADO" Dirección de Vialidad, resolución pág. 4 | [V] |
| SAFI | 401.341 | Resolución, pág. 4 | [V] |
| BIP | 40058856-0 | Resolución, pág. 4 | [V] |
| ID licitación | 1369-24-0124 | Resolución, pág. 4; acta técnica | [V] |
| Dirección | Vialidad | Resolución; acta técnica | [V] |
| Región | Antofagasta | Resolución | [V] |
| Financiamiento | Sectorial | Acta técnica ("FINANCIAMIENTO: SECTORIAL"); bases 2.10 | [V] |
| Nivel de adjudicación | Regional (firma Director Regional y SEREMI) | Resolución pág. 10 | [V] |
| Monto del contrato | $5.478.886.204 IVA incluido | Resolución resuelvo 2° y 3° | [V] |
| Presupuesto oficial | $4.400.000.000 | Resolución resuelvo 1° | [V] |
| Plazo | 420 días corridos desde el día siguiente a la tramitación | Resolución resuelvo 5°; bases 2.8 | [V] |
| Fecha apertura técnica | 24-07-2024 | Acta de apertura técnica | [V] |
| Garantía FCC exigida | 3% en UF, vigencia plazo + 24 meses, a nombre del SEREMI MOP Antofagasta RUT 61.202.000-0, con nombre del proyecto, código BIP y concepto | Resolución resuelvo 6°; bases anexo complementario 5.4.1 | [V] |
| RC exigida | Se exige; monto mínimo según cláusulas 5.4.3 y 5.4.6 de las bases | Resolución resuelvo 7°; bases 5.4.3 | [V] |
| TRC exigida | Monto igual al contrato en UF, UF del último día del mes anterior a la tramitación, vigencia plazo del contrato o sus prórrogas, a favor de Fisco MOP Dirección de Vialidad | Resolución resuelvo 8°; bases 5.4.4 | [V] |
| Anticipo | Podrá otorgarse según punto 7.14.4 del anexo complementario | Resolución resuelvo 11° | [V] |
| Retenciones | Cláusula 7.14.5 de las bases y art. 158 RCOP | Resolución resuelvo 6° | [V] |

## 2. Reglas de cálculo

| Regla | Detalle | Fuente | Conf. |
|---|---|---|---|
| Fecha de inicio de vigencias | Día siguiente a la fecha de total tramitación (21-03-2025) | Resolución 5°; MAESTRO | [V] |
| Fecha de término de obra | Inicio + plazo en días. Fabiana usa 21-03-2025 + 420 = 15-05-2026. Contando el día de inicio como día 1, el último día sería 14-05-2026: la convención de Fabiana da un día extra (conservador) | MAESTRO | [P] confirmar convención |
| UF de la FCC | Último día del mes anterior al mes de la apertura técnica (30-06-2024: $37.571,86) | MAESTRO; Fabiana en su correo ("fecha de apertura técnica") | [P] respaldo normativo por ubicar en bases tipo |
| UF de RC y TRC | Último día del mes anterior al mes de la tramitación (28-02-2025: $38.647,94) | Resolución 8° (TRC) [V]; MAESTRO (RC) [P] |
| Monto FCC | 3% × monto contrato / UF FCC = 4.374,73 UF | RCOP art. 96 (Obras Mayores) [V]; resolución 6° [V] |
| Monto RC | 5% × monto contrato / UF RC = 7.088,20 UF | MAESTRO [P]; resolución remite a bases 5.4.3 y 5.4.6, cuyo texto tipo no viene en el paquete |
| Monto TRC | 100% × monto contrato / UF TRC = 141.764 UF | Resolución 8° [V] |
| Redondeo | Siempre hacia arriba, nunca bajo el mínimo (FCC 4.374,7258 → 4.374,73; TRC 141.763,99 → 141.764) | MAESTRO | [P] |
| Vigencia FCC | Término de obra + 24 meses. Fabiana: 16-05-2028 (un día más que 15-05-2028) | RCOP art. 96 [V]; MAESTRO [P] el día extra |
| Vigencia RC | Término de obra + 12 meses. Fabiana: 16-05-2027 | MAESTRO [P] |
| Vigencia TRC | Plazo del contrato: 15-05-2026. La nota del MAESTRO dice "más dos meses", pero no se aplicó | Resolución 8° [V]; nota del MAESTRO inconsistente [P] |
| Garantía adicional | Solo si oferta < presupuesto oficial × 0,85: monto = (PO × 0,85 − oferta), en UF, vigencia como retenciones (art. 158). B-12: 3.740 M < 5.479 M, **no aplica** | RCOP art. 98 [V] |
| Beneficiario FCC | Regional: "Secretario Regional Ministerial de Obras Públicas, Región de X". Nacional: "Director Nacional de X". RUT 61.202.000-0. Nunca "MOP Dirección Gral de OO.PP. DCyF" | RCOP art. 96 [V]; Guía DGOP de emisión de pólizas (bases, pág. ~13600) [V]; MAESTRO ("depende de quien financia, Gore o Sectorial") [P] |
| Beneficiario RC y TRC | "Fisco de Chile, Ministerio de Obras Públicas, Dirección de X, Región de X", RUT 61.202.000-0 | Resolución 8° [V]; MAESTRO ("siempre es al MOP") |
| Glosa | Nombre exacto de la obra + "CÓDIGO SAFI N°..." + "RESOLUCIÓN ... N°... DEL [fecha], TRAMITADO EL [fecha]" | MAESTRO; Guía DGOP [V]. Ojo: el anexo complementario 5.4.1 pide además **código BIP**, que la glosa de la B-12 no incluye | [P] preguntar |
| Valor UF | Fuente oficial (SII o Banco Central). La tabla del MAESTRO llega solo hasta abril de 2025 | [V] |

## 3. Salidas y origen de cada campo

### 3.1 MAESTRO Solicitud de Pólizas (hoja "Calculo de Boletas y Polizas" y hoja "Solicitud")

| Campo | Origen |
|---|---|
| Nombre de la obra, resolución, SAFI, región, dirección, tipo de fondo, monto licitado | Sección 1 |
| Fecha propuesta técnica | Acta apertura técnica |
| Fecha adjudicación | Fecha de total tramitación |
| Fecha inicio, plazo, fecha término | Reglas sección 2 |
| UF y fecha UF por póliza | Reglas sección 2 + fuente oficial |
| Montos FCC, RC, TRC | Reglas sección 2 |
| Asegurado y glosa por póliza | Reglas de beneficiario y glosa |
| Vigencias por póliza | Reglas de vigencia |
| VB (Nicolás Paredes, Fabiana Pañella, Cristian Domínguez) | Fijo del formato; el agente no firma ni marca VB |

### 3.2 Datos para emitir póliza de garantía (Conosur)

| Campo | Origen |
|---|---|
| Contratante, RUT, dirección | Fijo Duffco (conocimiento permanente) |
| Asegurado, RUT | Beneficiario FCC |
| 1. Garantía correcta inversión de anticipo | N/A salvo que haya anticipo aprobado (resolución del convenio) |
| 2. Fiel cumplimiento: monto contrato, monto UF, inicio, término, glosa | MAESTRO |
| 3. Correcta ejecución | Vacío en B-12; se usa en canje de retenciones [H] |

### 3.3 Cuestionario RC y Cuestionario TRC (Conosur)

| Campo | Origen |
|---|---|
| Asegurado (Duffco y RUT) | Fijo |
| Mandante y RUT | Beneficiario RC/TRC |
| Detalle de trabajos | "Se adjunta descripción del proyecto" (TRC: + carta Gantt y metodología) → información adicional |
| Ubicación | "Se adjunta plano de ubicación" → información adicional |
| Vigencia | RC: inicio a término RC; TRC: inicio a término de obra |
| Valor del contrato | RC: pesos // UF RC; TRC: UF TRC + presupuesto itemizado |
| Mecánica de suelos (TRC) | "No aplica" en B-12 → preguntar a Fabiana en cada obra |
| Trabajadores | "Se adjunta programa ocupacional de mano de obra" → propuesta técnica (bases 3.2 letra h2) |
| Vehículos y equipos | "Se adjunta detalle" → propuesta técnica |
| Medidas de seguridad | Texto fijo de Duffco → conocimiento permanente |

### 3.4 Documentos de información adicional (variables por obra)

En B-12 los cuestionarios piden: descripción del proyecto, plano de ubicación, carta Gantt, metodología, programa ocupacional de mano de obra, detalle de vehículos y equipos y presupuesto itemizado. El agente: (1) lee los cuestionarios, (2) lista lo que se debe adjuntar, (3) lo busca en la propuesta técnica o las bases e indica página, (4) pregunta a Fabiana qué más pide Conosur para esta obra, (5) arma los documentos con ella.

## 4. Preguntas para Fabiana (sesión del lunes)

1. Convención de término de obra: ¿siempre inicio + plazo (un día extra)?
2. ¿Por qué FCC y RC terminan un día después (16-05) y TRC no (15-05)?
3. Regla del 5% de RC y fecha de UF de la FCC: ¿en qué documento está? (para citarla)
4. Nota del TRC "más dos meses": ¿está desactualizada?
5. Código BIP en la glosa de la FCC: el anexo complementario lo pide y la B-12 no lo tiene. ¿Fiscalía nunca lo observó?
6. ¿De dónde saca el valor de la UF?
7. ¿Qué textos de los cuestionarios son fijos de Duffco (medidas de seguridad, etc.)?
