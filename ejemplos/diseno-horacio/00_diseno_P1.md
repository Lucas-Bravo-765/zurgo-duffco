# DISEÑO P1 · Agente de pólizas (nombre lo elige Fabiana)

Versión: 0.1 | Fecha: 2026-10-17 | Estado: P1 aprobado por Santi el 2026-10-17
Anexos: `01_trazabilidad_etapa1.md`, `02_checklist_y_errores_etapa3.md`, `03_diff_auto_modificacion.md`

---

AGENTE: [nombre por definir] · acompaña a Fabiana desde la adjudicación de una obra hasta la entrega de las pólizas al MOP.

## ASSESSMENT INICIAL

- El brief es correcto, con un ajuste de expectativas: Duffco adjudica unas **3 obras al año** (17 en 6 años), cada una con 3 o 4 pólizas, más endosos, aumentos y canjes de retenciones. **El ROI no está en horas ahorradas**, sino en (1) evitar rechazos de Fiscalía, que atrasan estados de pago, y (2) **capturar el criterio de Fabiana**: hoy vive solo en su cabeza y en su Excel. Así hay que presentarlo al directorio.
- La Etapa 1 ya tiene una especificación probada: el MAESTRO de Fabiana. El agente lo replica y lo llena; no inventa un formato nuevo.
- La Etapa 2 parte con criterio bajo (aceptado por Fabiana) y se construye en la operación.
- La Etapa 3 se diseñó con errores sintéticos; se valida con casos reales en el computador de Fabiana.
- Pendiente después del lunes: ampliar el alcance a endosos (aumentos de obra, prórrogas de plazo) y canje de retenciones. Es el mismo motor y es frecuente.

## PROCESO Y LÍNEA BASE

- Flujo: adjudicación → Etapa 1 (agente) → Fabiana envía a Conosur → cotizaciones → Etapa 2 (agente con Fabiana) → Fabiana confirma y paga → pólizas → Etapa 3 (agente) → ciclo de correcciones → Fabiana entrega al MOP.
- Volumen: ~3 obras por año, 3 o 4 pólizas cada una [V por cartera]; endosos y canjes: [P].
- Tiempo por obra hoy: **[P] medirlo el lunes con Fabiana**. Sin línea base no hay ROI.
- Errores típicos: datos copiados de otra obra (región, nombre), fechas, beneficiario, glosa [V Fabiana].

## USUARIO

Fabiana Pañella, Gerente de Administración [V]. Fluencia en IA baja, aprende rápido, motivada. PC Windows, Claude Team (asiento Standard), Cowork. Más de 4 años en este proceso. Perfil: `memoria/usuarios/fabiana.md`.

## PERSONALITY RATIONALE

Una colega meticulosa y desconfiada por oficio: "no le creo a ninguna póliza hasta leerla entera". Comunica rigor sin ser fría. Habla claro y directo, sin jerga de IA; explica un término la primera vez y después lo usa normal. Trata a Fabiana como la experta que es: cuando no sabe algo de criterio, le pregunta y anota lo que aprende. Nada de humor en la Etapa 3 cuando hay errores críticos. El nombre lo pone Fabiana el lunes; el agente se presenta como "tu asistente de pólizas" hasta entonces.

## ESPECIFICACIONES

- **Objetivo principal:** que cada póliza llegue a Fiscalía sin errores, con la mitad del trabajo manual de Fabiana en Etapa 1 y Etapa 3 [meta a calibrar con la línea base].
- **Capacidades core:**
  1. Abrir la carpeta de una obra nueva y pedir los documentos de entrada.
  2. Etapa 1: extraer datos, calcular montos y vigencias con UF oficial, generar MAESTRO, Datos Conosur, cuestionarios RC y TRC y la lista de información adicional con su ubicación en la propuesta técnica; armar los documentos adicionales con Fabiana.
  3. Etapa 2: tabla comparativa (prima, tasa anual equivalente, % sobre el contrato, cláusulas restrictivas, compañías que declinaron) contra el histórico de Duffco; propuesta inicial; conversación con Fabiana; registro de la decisión y su porqué.
  4. Etapa 3: inventario de pólizas esperadas, verificación con checklist, PDF anotado e informe para enviar a la aseguradora; iterar versión tras versión.
  5. Aprender: registrar correcciones y criterio de Fabiana (capa 3) y proponer cambios de flujo (capa 2).
- **No hace:** no aprueba pólizas, no firma, no envía correos, no paga, no entrega al MOP, no borra ni modifica originales, no da por válida una firma, no inventa valores de UF ni normas.
- **Restricciones duras del dominio:** RCOP arts. 96, 98 y 158 [V]; la resolución y las bases de cada obra prevalecen sobre las reglas generales; todo hallazgo con cita (documento, página, campo); sin cita = "no verificado".
- **Conocimiento permanente:** reglas de cálculo, checklist, guía DGOP de emisión de pólizas, extractos del RCOP, datos fijos de Duffco, plantillas Conosur vacías, tabla de POL conocidos, frases que limitan el cobro.
- **Material de sesión:** documentos de cada obra en `obras/<obra>/`.
- **Métricas de éxito:** tiempo por obra (antes y después); % de hallazgos confirmados por Fabiana; falsos positivos; incidentes sin respaldo = 0; observaciones de Fiscalía post-agente = 0.

## ARQUITECTURA DE CARPETAS

```
agente-polizas/
├── INSTRUCCION_INTERFAZ.txt
├── README_USUARIO.md
├── memoria/
│   ├── 00_NUCLEO.md                 capa 1: identidad, reglas duras (bloqueado)
│   ├── flujo/                       capa 2: etapa1.md, etapa2.md, etapa3.md, formatos_salida.md
│   ├── conocimiento/                reglas, checklist, guía DGOP, RCOP, datos Duffco, POL, plantillas
│   ├── criterio/                    capa 3: criterio_cotizaciones.md, registro_decisiones.md
│   ├── aprendizajes.md              capa 3: preferencias y correcciones de Fabiana
│   ├── CHANGELOG.md
│   └── _historial/
├── historico/                       histórico de primas de Fabiana (excluido de git)
└── obras/<obra>/                    (excluido de git)
    ├── 01_entrada/  02_etapa1/  03_cotizaciones/  04_polizas/  05_informes/
```

## ROI ESTIMADO

Horas: [P] hasta tener la línea base (estimación a validar: 6 a 10 h por obra hoy, de 2 a 3 h con el agente → 12 a 24 h al año). El argumento fuerte no son las horas: cada rechazo de Fiscalía bloquea estados de pago de obras de miles de millones, y el criterio de Fabiana queda documentado y transferible.

## RIESGOS Y MITIGACIONES

| Riesgo | Mitigación |
|---|---|
| Pólizas escaneadas: lectura por visión con posibles errores de dígitos | Doble lectura de montos, RUT y fechas; cada cifra se cita con su página; ante duda, "no verificado" |
| Resaltado preciso sobre PDF escaneado | Fallback: notas al margen e informe tabular; probar el lunes |
| Valor de la UF | Fuente oficial con fecha; si no hay acceso web, se pide a Fabiana y se marca |
| Reglas [P] (5% RC, día extra, UF de la FCC) | Se usan como práctica de Fabiana, etiquetadas; se confirman el lunes |
| Consumo del asiento Standard (bases de 534 páginas) | El agente nunca lee las bases completas: busca las cláusulas 5.x y el anexo complementario |
| Fabiana pide quitar un control | Capa 1 bloqueada; el agente puede agregar verificaciones, nunca quitarlas |
| Datos personales en correos y documentos | Todo en `obras/` excluido de git |

## IMPLEMENTATION NOTES

- Lunes: instalación (Claude Desktop, Cowork y carpeta), prueba de humo con la B-12, sesión de preguntas del agente a Fabiana (lista en la trazabilidad, sección 4), elección del nombre y medición de la línea base.
- Git: el repositorio en la organización de Duffco se crea al instalar; mientras tanto, el agente vive en `sayin-duffco/agentes/` (excluido del repositorio de Sayin).
- Extended Thinking apagado.

## DECISIONES QUE NECESITO DE SANTI (P1)

1. Aprobar el diseño.
2. Aprobar el diff de nivel C de auto-modificación en tres capas (anexo 03).
3. Salida de la Etapa 1: el MAESTRO en Excel más un resumen en el chat (sin HTML por ahora). ¿OK?
4. Nombre provisorio de la carpeta: `agente-polizas`. ¿OK?
