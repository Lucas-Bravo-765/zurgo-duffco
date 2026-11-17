# CHECKLIST DE VERIFICACIÓN · ETAPA 3

Versión: 0.2 | Fecha: 2026-10-17
Fuentes: RCOP arts. 96, 98 y 158 [V]; guía DGOP para la emisión de pólizas (ver `guia_dgop_polizas.md`) [V]; verificaciones pedidas por Fabiana (reunión del 14-10-2026) [V]; prueba con 22 errores sintéticos y con las pólizas reales de la Ruta B-12.
Referencia siempre: la ficha de la Etapa 1 (`resultado_etapa1.json`) más la resolución y las bases.

Severidades: CRÍTICO, FORMAL, LEVE, HUMANO, NO VERIFICADO (ver `memoria/flujo/etapa3.md`).

## 0. Antes de empezar

- [ ] Inventario: están todas las pólizas exigidas (incluida la garantía adicional si `resultado_etapa1.json` dice que aplica). Si falta una exigida: CRÍTICO.
- [ ] Cada póliza tiene su certificado de pago. Si falta: CRÍTICO (y NO VERIFICADO lo que dependa de él).
- [ ] Todas las páginas presentes y legibles. Si no: NO VERIFICADO en lo afectado.

## 1. Común a todas las pólizas

| # | Verificación | Si falla |
|---|---|---|
| C1 | Tipo de póliza correcto para lo exigido | CRÍTICO |
| C2 | Tomador o contratante: DUFFCO INGENIERÍA Y CONSTRUCCIÓN SPA, RUT 77.119.761-2 (o consorcio si aplica). Ojo con "LTDA" (razón social antigua) | CRÍTICO |
| C3 | Nombre de la obra idéntico al de la resolución, en **cada** mención (km, llamado, año, comuna) | FORMAL |
| C4 | Resolución citada completa: servicio, número, fecha de emisión y fecha de tramitación | FORMAL |
| C5 | SAFI correcto; BIP si las bases lo exigen | FORMAL |
| C6 | Región, comuna y dirección coherentes en **todas** las menciones (error típico de copiar y pegar de otra obra) | FORMAL |
| C7 | Moneda: UF | CRÍTICO |
| C8 | Monto asegurado ≥ monto de la ficha | CRÍTICO |
| C9 | Inicio de vigencia = inicio de la ficha | FORMAL |
| C10 | Término de vigencia ≥ término de la ficha. Si encabezado y cuerpo difieren, vale la fecha menor | CRÍTICO si es menor |
| C11 | Encabezado y cuerpo con las mismas fechas y montos | FORMAL |
| C12 | Si la vigencia dice "a las 12 horas", el término debe cubrir el día exigido completo (la Ruta B-12 se aceptó así) | LEVE |
| C13 | Certificado de pago que diga **pago al contado** | CRÍTICO |
| C14 | Firma del certificado de pago y del apoderado o firma autorizada | HUMANO: preguntar siempre a Fabiana |

## 2. Fiel cumplimiento (FCC), garantía adicional y anticipo

| # | Verificación | Si falla |
|---|---|---|
| F1 | Asegurado: SEREMI MOP de la región (regional) o Director Nacional (nacional), RUT 61.202.000-0. No se acepta "MOP Dirección Gral de OO.PP. DCyF" sin la aclaración del condicionado particular | CRÍTICO |
| F2 | Beneficiario (si existe ese campo) = asegurado | FORMAL |
| F3 | Condiciones generales: póliza de garantía o caución **a primer requerimiento** de obras públicas, con su código POL (ver tabla) | CRÍTICO |
| F4 | Sin cláusulas, endosos o adiciones que limiten las atribuciones del MOP (ver frases de alerta) | CRÍTICO |
| F5 | "No se puede poner término anticipado ni modificar sin autorización escrita del MOP" | CRÍTICO |
| F6 | "Pagada al contado" en la póliza, más timbre de pago | CRÍTICO |
| F7 | Sin referencias a cuotas que confundan sobre el pago | LEVE (la FCC de la Ruta B-12 dice "Nro Cuota 1" y fue aceptada) |
| F8 | Glosa: "para garantizar el fiel cumplimiento..." + obra + SAFI + resolución | FORMAL |
| F9 | Deducible 0 | CRÍTICO |
| F10 | Figura del Defensor del Asegurado eliminada | LEVE [por confirmar con Fabiana] |
| A1 | Garantía adicional presente cuando la Etapa 1 dice que aplica, con monto y vigencia correctos | CRÍTICO |

## 3. Responsabilidad civil (RC)

| # | Verificación | Si falla |
|---|---|---|
| R1 | Asegurado adicional o beneficiario: Fisco de Chile, MOP, Dirección y región correctas, RUT 61.202.000-0 | CRÍTICO |
| R2 | Límite de indemnización ≥ monto RC de la ficha, por evento **y** en agregado | CRÍTICO |
| R3 | Actividad asegurada con nombre de la obra, SAFI y resolución | FORMAL |
| R4 | Ubicación del riesgo (región) correcta | FORMAL |
| R5 | No término ni modificación sin autorización escrita del MOP | CRÍTICO |
| R6 | Nombres del MOP coherentes dentro de la póliza | LEVE |
| R7 | Sublímites, deducibles y exclusiones: listarlos para Fabiana | HUMANO |

## 4. Todo riesgo de construcción (TRC)

| # | Verificación | Si falla |
|---|---|---|
| T1 | Beneficiario, mandante y asegurado adicional: Fisco de Chile, MOP, Dirección, región, RUT 61.202.000-0 | CRÍTICO |
| T2 | Monto asegurado ≥ monto del contrato en UF de la ficha | CRÍTICO |
| T3 | Vigencia de construcción ≥ plazo del contrato | CRÍTICO |
| T4 | Descripción del proyecto con el nombre exacto de la obra (en la Ruta B-12, la primera línea omitía "NUEVO 2024": hallazgo real) | FORMAL |
| T5 | Cláusulas restrictivas (incendio, bienes almacenados, caminos provisorios, etc.): listarlas | HUMANO |
| T6 | Periodo de mantenimiento: informar las fechas | HUMANO |

## 5. Códigos POL conocidos

| Código | Texto | Uso |
|---|---|---|
| POL120240042 | Póliza de seguro de garantía o caución a primer requerimiento de obras públicas | FCC (HDI, Ruta B-12, 2025) [V] |
| POL120140065 | Póliza de seguro de garantía o caución a primer requerimiento para obras públicas | Anticipo (guía DGOP) [V] |
| POL120190146 | Condiciones generales de responsabilidad civil | RC (Southbridge, Ruta B-12) [V] |

Un POL que no esté en la tabla: NO VERIFICADO; pedir a Fabiana que lo confirme o consultar el depósito de pólizas de la CMF (cmfchile.cl). Una vez confirmado, agregarlo a la tabla (cambio de capa 2).

## 6. Frases de alerta (posible limitación del cobro, F4)

Cualquier cláusula que condicione o retrase el pago al MOP, por ejemplo:
- "previa liquidación del contrato" o "una vez liquidado el contrato"
- plazos para reclamar o avisar el siniestro que corran contra el MOP
- "sujeto a aprobación de la compañía" o "previa evaluación del asegurador"
- exclusión por "agravación del riesgo" o "reclamo extemporáneo" aplicable al MOP
- arbitraje obligatorio para el MOP (en la RC de la Ruta B-12 dice que el MOP "sólo podrá participar en arbitraje cuando una norma o dictamen así lo disponga": eso está bien)

Antecedente: en el caso de la ampliación del GAM, una aseguradora se negó a pagar al MOP alegando falta de liquidación, reclamo extemporáneo y agravación de riesgo.
