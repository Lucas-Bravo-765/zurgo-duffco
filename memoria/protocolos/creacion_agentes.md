# PROTOCOLO DE CREACIÓN DE AGENTES

Versión: 1.0 (Zurgo) | Fecha: 2026-11-16 | Base: protocolo de Dr. Sayin Duffco
Se lee antes de levantar un proceso, diseñar o modificar un agente.

---

## 0. PUERTAS DE APROBACIÓN

Un agente avanza por tres puertas. Ninguna se salta.

| Puerta | Qué aprueba Lucas | Después de |
|---|---|---|
| **P1. Diseño** | Que el proceso, el alcance, el usuario y la arquitectura son correctos | Pasos 1 a 6 |
| **P2. Prototipo** | Que el agente pasa las pruebas con documentos de ejemplo | Paso 8 |
| **P3. Entrega** | Que el paquete está listo para instalar en Duffco | Protocolo de entrega |

---

## 1. LEVANTAMIENTO DEL PROCESO

Usa `plantillas/levantamiento_proceso.md`. Antes de diseñar necesitas:
- Qué se hace hoy, paso a paso, y quién lo hace.
- Documentos de entrada y de salida (con un ejemplo real en `insumos/`).
- Volumen (cuántos por semana o mes) y tiempo por unidad: **esta es la línea base del ROI**.
- Errores típicos y su costo (rechazo del MOP, retraso de un estado de pago, multa).
- Normas o bases que rigen el proceso.

**Desafía el brief.** Pregúntate:
- ¿Este es el proceso con mejor relación impacto/riesgo?
- ¿Necesita un agente o basta una plantilla, una macro o un checklist?
- ¿Qué parte debe seguir siendo 100% humana?

Si Lucas no tiene un dato, se marca [P] y se sigue; no se inventa.

---

## 2. PERFIL DEL USUARIO

Lee o crea su perfil en `usuarios/<nombre>.md` (plantilla en `plantillas/usuario.md`). Lo que define el diseño:
- Fluencia en IA: baja, media o alta.
- Autonomía técnica: ¿puede resolver un problema solo o depende de Lucas?
- Equipo y sistema operativo, plan de Claude y si ya usa Claude Desktop.
- Estilo de comunicación y nivel de formalidad.

**Por defecto, los usuarios de Duffco son perfil enterprise:** fluencia baja a media. Eso implica onboarding suave dentro del agente, mensajes de error amigables, instrucciones paso a paso y cero jerga de IA. Se sube la potencia solo si el perfil lo justifica.

---

## 3. PLATAFORMA

Por defecto: **Claude Desktop en el computador del usuario, con la cuenta de Duffco y una carpeta local conectada.** Confirma:
- Que el usuario tiene acceso a Claude Desktop con su cuenta de Duffco.
- Qué conectores o herramientas necesita el agente (y si Duffco los tiene habilitados).
- Que el agente puede operar solo dentro de su carpeta.

Si el proceso no necesita archivos locales, evalúa si basta un proyecto de Claude sin carpeta (más simple de mantener).

---

## 4. ALCANCE Y RESTRICCIONES DURAS

Define por escrito:
- **Objetivo principal:** una frase medible.
- **Hace:** lista de capacidades.
- **No hace:** lista explícita. Siempre incluye: no aprueba, no firma, no envía, no borra, no modifica originales.
- **Restricciones duras del dominio:** las reglas normativas o de bases que nunca puede violar, con su fuente.

---

## 5. ARQUITECTURA DE CONOCIMIENTO

| Tipo | Contenido | Ubicación en el agente |
|---|---|---|
| Permanente | Normativa aplicable, manuales, criterios, checklists aprobados | `memoria/conocimiento/` |
| De sesión | El documento del día, las bases de esa licitación, la póliza a revisar | `trabajo/` (excluido de git) |
| Aprendizajes | Preferencias del usuario y correcciones recurrentes | `memoria/aprendizajes.md` |

Reglas:
- Cada archivo de conocimiento permanente lleva fuente y fecha de verificación al inicio.
- Prefiere embeber el conocimiento en archivos antes que depender de búsquedas web en tiempo de uso.
- Documentos largos: convertir a Markdown limpio y dividir por unidad temática para evitar contaminación en la recuperación.
- Nada de conocimiento de otro agente.

---

## 6. NOMBRE Y PERSONALIDAD

- El nombre es parte del diseño. Un nombre con personalidad mejora la adopción. Debe ser fácil de decir en una oficina chilena y no prestarse para burla.
- La personalidad se calibra al usuario final, no a Lucas.
- Cada rasgo debe servir a la función. Ejemplo: un agente de pólizas puede ser meticuloso y desconfiado por oficio ("no le creo a ninguna póliza hasta que la leo entera"), lo que comunica rigor sin ser frío.
- Evita personalidades que distraigan en momentos de presión (cierre de una licitación, un estado de pago atrasado).

**Puerta P1:** presenta el diseño a Lucas en el formato de la sección 9 (sin el núcleo completo aún) y espera su aprobación.
Los documentos de diseño se guardan en `disenos/<agente>/` del repositorio de Zurgo, nunca dentro de la carpeta del agente.

---

## 7. CONSTRUCCIÓN

1. Copia `plantillas/agente/` a `agentes/<nombre>/`.
2. Completa `memoria/00_NUCLEO.md` del agente con las 7 secciones: Identidad, Perfil del usuario, Capacidades core, Estilo y tono, Reglas duras, Protocolo de sesión, Opener.
3. Carga el conocimiento permanente en `memoria/conocimiento/`.
4. Completa `INSTRUCCION_INTERFAZ.txt` (el texto corto que se pega en Claude Desktop).
5. Completa `README_USUARIO.md` en lenguaje simple para el usuario final.
6. Registra el agente en `registro_agentes.md` con estado "en construcción".

Reglas de redacción del núcleo del agente:
- Corto y operativo. Si una sección pasa de una pantalla, probablemente sobra algo.
- Las reglas duras van al principio de su sección, numeradas, en imperativo.
- El formato de salida se define con un ejemplo concreto.
- Sin guiones largos.

---

## 8. PRUEBAS

Antes de la puerta P2, el agente se prueba con al menos:
1. **Caso feliz:** un documento real o representativo que cumple todo.
2. **Caso con error:** un documento con al menos un incumplimiento conocido. El agente debe detectarlo y citarlo.
3. **Caso ambiguo:** un documento donde falta información. El agente debe decir "no verificado" y preguntar, nunca asumir.
4. **Caso fuera de alcance:** un pedido que el agente no debe hacer (ej. "envíalo al MOP"). Debe negarse amablemente y explicar qué sí puede hacer.
5. **Prueba de usuario novato:** simula al usuario real con poca fluencia (instrucciones vagas, errores de tipeo). El agente debe guiarlo.

Registra resultados en la bitácora: qué pasó, qué falló, qué se corrigió. Si un caso falla, se corrige y se repiten todos.

**Puerta P2:** muestra a Lucas los resultados y espera su aprobación.

---

## 9. FORMATO DE PRESENTACIÓN DEL DISEÑO

```
AGENTE: [Nombre] · [función en una línea]

ASSESSMENT INICIAL:
[Evaluación crítica del brief y mejoras sugeridas]

PROCESO Y LÍNEA BASE:
[Proceso actual, volumen, tiempo por unidad, errores típicos]

USUARIO:
[Nombre, cargo, fluencia en IA, autonomía técnica]

PERSONALITY RATIONALE:
[Por qué esta personalidad y cómo sirve al objetivo]

ESPECIFICACIONES:
- Objetivo principal: [medible]
- Capacidades core: [lista]
- No hace: [lista]
- Restricciones duras del dominio: [con fuente]
- Conocimiento permanente: [archivos]
- Material de sesión: [qué entra cada vez]
- Métricas de éxito: [KPIs con meta]

ROI ESTIMADO:
[Horas ahorradas por mes = volumen × (tiempo actual − tiempo con agente); errores evitados]

RIESGOS Y MITIGACIONES:
[Lista]

NÚCLEO DEL AGENTE:
[Solo después de P1]

IMPLEMENTATION NOTES:
[Instalación, capacitación mínima, mantención]
```

---

## 10. MÉTRICAS MÍNIMAS POR AGENTE

- Tiempo por unidad antes y después.
- Volumen procesado por mes.
- Tasa de hallazgos correctos (verificados por el humano) y de falsos positivos.
- Incidentes: casos en que el agente afirmó algo sin respaldo (meta: cero).
- Adopción: sesiones por semana del usuario.

Estas métricas son las que Lucas presenta al directorio. Sin línea base no hay ROI, y sin ROI no hay segundo agente.
