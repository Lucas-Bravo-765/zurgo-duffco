# BITÁCORA

Una entrada por sesión, solo con el delta: decisiones, archivos tocados, pendientes y próximo paso. La entrada más reciente va arriba.

---

## 2026-11-16 · Sesión 1 (primera activación)

**Decisiones**
- Repo `zurgo-duffco` publicado como privado en la cuenta `Lucas-Bravo-765`. El primer intento quedó en la cuenta equivocada (`LucasPython01`); su `.git` se movió a `ZURGO-DUFFCO/_git_viejo_LucasPython01` y el repo remoto viejo sigue en GitHub (borrarlo después).
- Perfil de Lucas completado (núcleo 2.0, nivel D aprobado por Lucas).
- Lucas no participa del proceso 2 (de Santi): la regla 11 se mantiene sin cambios.
- Sandia clonado en `ZURGO-DUFFCO/Sandia` (cuenta `Lucas-Bravo-765`). Leídos: bienvenida, estado inicial y "Hola, Zurgo" de Sayin.
- Primer reporte en Sandia: `duffco/lucas/2026-11-16_general_presentacion-zurgo.md` (presentación, perfil de Lucas con su acuerdo, 5 preguntas a Santi, inconsistencia de commits a Sayin).
- Respuesta de Santi (`duffco/santi/2026-11-16_general_respuestas-a-zurgo.md`): Lucas en **etapa de acompañamiento**, observador del proceso 2 junto a Santi; sin proceso propio. Mientras dure, Zurgo no levanta, no diseña ni numera procesos. El primer proceso de Lucas se define al terminar el acompañamiento; a Duffco irá para el levantamiento de su propio proceso.
- Commits: los hace Zurgo (git add y commit, limpieza de `.lock` con permiso de borrado una vez por sesión); Lucas hace Pull y Push. Decisión de Lucas; `auto_modificacion.md` 1.1 alineado con el núcleo y `repositorios_y_datos.md`.

**Archivos creados o modificados**
- Carpetas creadas: `disenos/`, `agentes/`, `insumos/`, `entregas/`, `EntradasTemporales/`.
- `memoria/00_NUCLEO.md` 1.0 → 2.0 (sección 2); respaldo en `_historial/00_NUCLEO_v1.0_2026-11-16.md`; línea en `_historial/CHANGELOG.md`.
- `README.md`: GitHub Desktop lo reemplazó al crear el repo; restaurado con el texto original que pasó Santi.
- `memoria/contexto_duffco.md` 1.2 → 1.3 (cargo de Fabiana Pañella, organización `duffco-spa`), nivel B aprobado.
- `memoria/protocolos/auto_modificacion.md` 1.0 → 1.1 (paso 7: commit lo hace Zurgo), nivel C aprobado. Respaldos en `_historial/`.

**Pendientes**
- [ ] Lucas: acompañar a Santi en el briefing del proceso 2 como observador.
- [ ] Lucas y Santi: definir el primer proceso de Lucas al terminar el acompañamiento (candidatos [H]: estudio de bases, admisibilidad, API de Mercado Público tras la prueba técnica).
- [ ] Lucas: confirmar con Santi que el único colaborador de Sandia sea `Lucas-Bravo-765` (quitar `LucasPython01` si quedó invitado).
- [ ] Santi: pasar a Lucas las plantillas de Gantt y bitácora (Excel y Word, fuera de Sandia) cuando arranque su primer proceso.
- [ ] Lucas: cambiar la carpeta conectada `Documents/SANDIA` (no existe) por `ZURGO-DUFFCO/Sandia`, o quitarla, en el Project de Claude.
- [ ] Lucas: revisar que su cuenta de Claude no use los chats para entrenar modelos.
- [ ] Lucas: confirmar si iCloud sincroniza "Escritorio y Documentos"; si sí, mover la carpeta fuera de `Documents`.
- [x] Identidad de git corregida: desde el segundo commit firma `Lucas-Bravo-765` (el commit inicial queda como `LucasPython01`).
- [ ] Más adelante: borrar el repo viejo `LucasPython01/zurgo-duffco`, la carpeta `_git_viejo_LucasPython01`, la descarga `ZURGO-DUFFCO/Sandia-main` y el primer clon de Sandia (probablemente en `Documents/GitHub/Sandia`).

**Próximo paso**
- Briefing del proceso 2 con Lucas como observador; leer el reporte de levantamiento formal de Santi cuando llegue y usarlo como caso de estudio.

---

## 2026-11-16 · Sesión 0 (semilla, preparada por Dr. Sayin Duffco)

**Decisiones**
- Santi suma a Lucas al proyecto Duffco. Cada uno trabaja procesos distintos con su propio agente constructor y su propio repositorio. El agente de Lucas se llama **Zurgo** (nombre puesto por Santi y Lucas).
- Zurgo nace como gemelo de Dr. Sayin Duffco: misma metodología, protocolos adaptados a Lucas, contexto de Duffco v1.2 y los aprendizajes del proyecto hasta esta fecha.
- Coordinación solo por el repositorio Sandia: Zurgo escribe en `duffco/lucas/` y lee `duffco/santi/`.
- Lucas puede ver todo lo que ve Santi; trabaja con su cuenta personal de Claude; Catalina autorizó su acceso a documentos de Duffco a modo de prueba.

**Archivos creados**
- Núcleo 1.0, `aprendizajes_proyecto.md`, `contexto_duffco.md` (copia de la v1.2 de Sayin), protocolos adaptados, plantillas, registro, esta bitácora, `ejemplos/` (Horacio completo, su diseño y el perfil de Fabiana).

**Pendientes**
- [ ] Lucas: crear el repositorio privado `zurgo-duffco` con esta carpeta (ver `LEEME_PRIMERO.md`).
- [ ] Zurgo: primera activación según la sección 6 del núcleo (bienvenida en Sandia, aprendizajes, perfil de Lucas, primer reporte).
- [ ] Lucas y Santi: definir el primer proceso de Lucas y su número.
- [ ] Lucas: pedir a Santi acceso a `duffco-spa` cuando construya su primer agente.

**Próximo paso**
- Primera activación de Zurgo.
