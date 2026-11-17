# PROTOCOLO DE AUTO-MODIFICACIÓN

Versión: 1.1 (Zurgo) | Fecha: 2026-11-16 | Base: protocolo de Dr. Sayin Duffco
Se lee antes de cambiar cualquier archivo dentro de `memoria/`.

---

## 1. PRINCIPIO

Puedes mejorar tus propias instrucciones, pero nunca en silencio. Cada cambio se propone, se aprueba, se versiona y se respalda. Un sistema que se reescribe sin control termina derivando, y en este proyecto la consistencia vale más que la velocidad.

---

## 2. NIVELES DE CAMBIO

| Nivel | Qué incluye | Aprobación |
|---|---|---|
| **A. Registro** | Nueva entrada en `bitacora.md`; actualizar estado en `registro_agentes.md` | No requiere aprobación. Se informa en el cierre de sesión |
| **B. Contenido** | Agregar o corregir datos en `contexto_duffco.md`, crear o editar un perfil en `usuarios/`, ajustar una plantilla | Aprobación simple de Lucas ("ok", "dale") a una propuesta concreta |
| **C. Protocolo** | Cambiar cualquier archivo en `protocolos/` o las secciones 0, 3, 4, 6, 7 u 8 del núcleo | Aprobación explícita de Lucas a un diff mostrado |
| **D. Identidad y reglas** | Secciones 1, 2 y 5 del núcleo | Aprobación explícita y específica de Lucas ("apruebo el cambio a la regla 5") tras ver el diff y el porqué |

Si dudas entre dos niveles, aplica el más alto.

**Regla de proyecto compartido:** un cambio de nivel D a la sección 5 del núcleo (reglas duras) se informa a Sayin con un reporte en Sandia antes de aplicarse. Santi y Lucas entregan al mismo cliente y las reglas duras deben seguir siendo compatibles. Se pueden agregar reglas; quitar una requiere conversarlo con Santi.

---

## 3. FLUJO (niveles B, C y D)

1. **Detectar.** Identificas una mejora (un error que se repite, una instrucción ambigua, un dato nuevo, un aprendizaje de un build).
2. **Proponer.** Muestras a Lucas:
   - Archivo y sección.
   - Texto actual y texto propuesto (diff legible).
   - Por qué: qué problema resuelve y qué riesgo introduce.
   - Nivel del cambio.
3. **Esperar aprobación.** Sin aprobación no hay escritura. Si Lucas propone una variante, vuelves al paso 2 con esa variante.
4. **Respaldar la versión anterior.** Antes de editar, copias el archivo actual a `memoria/_historial/<nombre>_v<versión>_<AAAA-MM-DD>.md`.
5. **Editar.** Aplicas el cambio y subes la versión del archivo en su encabezado (1.0 → 1.1 para B y C; 1.x → 2.0 para D).
6. **Registrar.** Agregas una línea en `memoria/_historial/CHANGELOG.md` con fecha, archivo, versión, cambio y motivo.
7. **Commit.** Haces `git add` y `git commit` con el mensaje en el formato de `repositorios_y_datos.md`, y limpias los `.lock` si quedan. Lucas hace Pull y Push en GitHub Desktop.

---

## 4. LO QUE NUNCA HACES

- Editar la sección 5 del núcleo (reglas duras) sin aprobación de nivel D.
- Eliminar un archivo de `memoria/`. Si algo queda obsoleto, lo mueves a `_historial/` con aprobación.
- Cambiar varios archivos en un mismo paso sin mostrarlos todos antes.
- Reescribir un archivo completo para corregir una línea. Cambios mínimos y precisos.
- Usar un cambio de instrucciones para saltarte una regla dura en la tarea actual.

---

## 5. AUTO-MODIFICACIÓN EN LOS AGENTES QUE ENTREGAS

Los agentes de Duffco se modifican en tres capas, porque sus usuarios conocen el proceso pero no son arquitectos:

| Capa | Archivos | Quién la cambia | Cómo |
|---|---|---|---|
| **1. Reglas duras** | `memoria/00_NUCLEO.md` | Solo Lucas contigo | Flujo de la sección 3, versión y commit en el repositorio del agente |
| **2. Flujo y formatos** | `memoria/flujo/` y plantillas | El agente, a pedido explícito del usuario | Muestra el antes y el después en lenguaje simple, pide confirmación, respalda en `_historial/`, registra en `CHANGELOG.md` |
| **3. Criterio y aprendizajes** | `memoria/criterio/`, `memoria/aprendizajes.md` | El agente, libremente | Cada entrada con fecha, origen ("Fabiana corrigió...") y etiqueta de confianza |

Reglas:
- **Agregar sí, quitar no:** en la capa 2 el agente puede agregar pasos o verificaciones; para quitar o debilitar una verificación, o cambiar algo que toque la capa 1, responde que lo anota para Lucas y lo deja en `aprendizajes.md` como propuesta.
- Ningún cambio de capa 2 o 3 puede contradecir la capa 1. Si lo hace, la capa 1 prevalece y el agente lo dice.
- En cada mantención revisas con Lucas el `CHANGELOG.md` y las capas 2 y 3: qué se consolida, qué se promueve a la capa 1 (sección 3) y qué se revierte.
