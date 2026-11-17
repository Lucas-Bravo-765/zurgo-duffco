# APRENDIZAJES DEL PROYECTO DUFFCO

Versión: 1.0 | Fecha: 2026-11-16 | Escrito por Dr. Sayin Duffco para Zurgo
Lo que Santi y Sayin aprendieron del 12-10 al 16-11-2026, sobre todo construyendo e instalando a Horacio (agente de pólizas de Fabiana). Es experiencia, no dogma: si un caso tuyo lo contradice, gana la evidencia, y cuéntalo en Sandia.

---

## A. MÉTODO: CÓMO SE LEVANTA Y SE DISEÑA UN PROCESO

1. **La primera reunión es para aprender, no para vender.** Santi va a la oficina a tomar notas y transcribe la reunión. No se compromete forma ni plazo del agente en esa reunión. Con Fabiana y con Nicolás, la primera conversación cambió el alcance que se traía pensado.
2. **El alcance real suele ser más grande que el pedido.** Pólizas partió como "revisar pólizas antes de entregarlas al MOP" y terminó en tres etapas (montos y plazos, comparación de cotizaciones, verificación). La postulación a licitaciones resultó ser varios procesos y se partió solo por la propuesta económica. Regla: **si es grande, se divide en procesos y se cobra cada uno**.
3. **Pide un caso resuelto, no documentos sueltos.** Lo más valioso fue el paquete completo de una obra ya terminada (Ruta B-12): las entradas reales más lo que Fabiana produjo a mano. Eso sirve como especificación y como banco de pruebas a la vez: el agente "aprueba" cuando reproduce lo que hizo el humano.
4. **Trazabilidad de cada dato de salida.** Para Horacio se armó una tabla con cada dato de salida, de qué documento sale (página, cláusula) y con qué regla se calcula (ver `ejemplos/diseno-horacio/01_trazabilidad_etapa1.md`). Esto destapó qué preguntas había que hacerle al usuario.
5. **No diseñes el criterio que no conoces.** El criterio para elegir cotizaciones no se inventó: el agente lo levanta preguntándole al usuario durante la operación y lo va anotando. Fabiana aceptó que el agente parta con poco criterio y mejore.
6. **El usuario decide el orden.** Sayin propuso partir por la etapa de verificación; Santi y Fabiana decidieron construir en orden 1, 2, 3. Se hizo así.
7. **Errores sintéticos para probar verificaciones.** Como no había pólizas reales con errores a mano, Sayin diseñó 22 errores sintéticos para probar la etapa 3 y con eso ajustó 5 puntos del checklist (`ejemplos/diseno-horacio/02_checklist_y_errores_etapa3.md`). Las pruebas con errores reales quedan para cuando el agente esté instalado.
8. **Desafía el brief, pero con evidencia.** Las tres preguntas útiles: ¿es el proceso correcto?, ¿necesita un agente o basta algo más simple?, ¿qué parte queda 100% humana?
9. **Línea base desde el día uno.** Sin tiempo por unidad medido no hay ROI que mostrar. En pólizas quedó pendiente medirla y eso debilita el caso. Pídela en el levantamiento y, si no está, haz que el agente la pregunte en su primera sesión.

## B. ARQUITECTURA DE UN AGENTE ENTREGADO (lo que funcionó en Horacio)

1. **Tres capas de auto-modificación** (ver `protocolos/auto_modificacion.md`, sección 5, y `ejemplos/horacio/memoria/flujo/cambios.md`):
   - Capa 1, núcleo: bloqueado. Solo lo cambia el constructor.
   - Capa 2, flujo y formatos (`memoria/flujo/`, plantillas): el agente lo cambia a pedido del usuario, explicando antes y después, con confirmación, respaldo y changelog.
   - Capa 3, criterio (`memoria/criterio/`, `aprendizajes.md`): el agente aprende libremente.
   - **Agregar sí, quitar no:** el agente puede sumar verificaciones; quitar o debilitar una, o tocar la capa 1, queda como "Propuesta para el constructor" en `aprendizajes.md`.
2. **Estructura de carpetas que sirvió:** `memoria/` (núcleo, `conocimiento/`, `flujo/` con un archivo por etapa más `primera_sesion.md` y `cambios.md`, `criterio/`, `aprendizajes.md`, `_historial/`, `CHANGELOG.md`), `herramientas/` (scripts Python), `plantillas/`, `obras/<obra>/` con `estado.md`, `historico/`, y una bandeja `ENTRADAS/`. Ojo: el protocolo de entrega dice `trabajo/` y `salidas/`; en la práctica una carpeta por caso (`obras/<obra>/`) con subcarpetas por etapa funcionó mejor.
3. **Bandeja de entrada.** El usuario deja todo en `ENTRADAS/`; el agente clasifica, renombra (`AAAA-MM-DD_TIPO_Obra`) y mueve, dejando un `_origen.md` con el nombre original. El usuario no tiene que aprender la estructura de carpetas.
4. **Primera sesión guiada.** El agente, no el constructor, le hace al usuario las preguntas pendientes (16 en tandas de 3: nombre del agente, criterio, línea base de horas). Ver `ejemplos/horacio/memoria/flujo/primera_sesion.md`.
5. **Cálculos deterministas en código.** Montos, UF y vigencias se calculan con `herramientas/*.py`, no "de cabeza". El modelo lee y explica; el script calcula.
6. **Lenguaje de salida seguro.** Nunca "aprobada" ni "lista para el MOP": "sin hallazgos en lo que revisé; falta tu revisión de las firmas". Lo que el agente no puede validar (firmas, quién puede firmar) lo pregunta siempre.
7. **Ante la duda entre dos lecturas de un dato, la más desfavorable**, y se marca.
8. **Salidas en el formato que el usuario ya usa.** La etapa 1 llena el Excel MAESTRO y los formularios de la corredora que Fabiana ya usaba, más un resumen en el chat. No se inventaron formatos nuevos.
9. **Personalidad al servicio de la función.** Horacio es "meticuloso y desconfiado por oficio, pero colega". El nombre lo elige el usuario (en Horacio, Santi puso uno provisorio y Fabiana debía confirmarlo).
10. **Perfil enterprise por defecto:** usuarios de Duffco con fluencia baja a media. Hablar claro, explicar un término técnico la primera vez y luego usarlo normal, invitar a preguntar, sin tratar al usuario como si no entendiera.

## C. PLATAFORMA E INSTALACIÓN (aprendido instalando a Horacio el 21-10)

1. **Cuenta y plan:** el agente corre en la cuenta del usuario, nunca en la del constructor. Duffco tiene plan **Claude Team** con Santi como administrador (Fabiana con asiento Standard). Riesgo abierto: el tope de uso del asiento Standard en sesiones largas; alternativa, asiento Premium.
2. **Claude Desktop con Cowork** en el PC del usuario (Fabiana: Windows), carpeta conectada, `INSTRUCCION_INTERFAZ.txt` pegado como instrucción. Extended Thinking apagado.
3. **Capacidades de la organización:** ejecución de código activada. Red: la guía proponía permitir dominios específicos; Santi terminó habilitando "todos los dominios" el 21-10 (decisión consciente, a revisar). La UF se obtuvo del SII; mindicador.cl no respondió.
4. **Correo (Outlook):** el conector permite leer el texto de los adjuntos, no descargarlos. Solución: el usuario guarda los adjuntos en la bandeja `ENTRADAS/`.
5. **Borrar está bloqueado** en la carpeta conectada por defecto. Es correcto para el agente del usuario (no debe borrar), pero afecta a git (ver D).
6. **Ubicación:** fuera de OneDrive, Documentos y Escritorio: `C:\Users\<usuario>\AgentesDuffco\<agente>\`.
7. **Repositorio del agente** privado en `duffco-spa`; el usuario tiene cuenta de GitHub y GitHub Desktop, y hace Commit y Push de `memoria/` al terminar el día; el constructor revisa sus pushes. ZIP como respaldo de instalación.
8. **Prueba de humo con valores esperados** del caso resuelto (en Horacio: monto, plazo y montos en UF de cada póliza de la B-12). Ver `ejemplos/horacio/GUIA_INSTALACION.md`, sección D.
9. **Guía de instalación escrita para el constructor**, con la advertencia de que la interfaz de Claude Desktop cambia seguido.

## D. GIT, REPOSITORIOS Y RESPALDO

1. El constructor hace commit; el humano hace Pull y Push en GitHub Desktop.
2. **Cowork deja `.lock`:** sin permiso de borrado, git no puede limpiar sus temporales y GitHub Desktop falla después. Pedir el permiso una vez por sesión y limpiar.
3. **Repos anidados no se respaldan:** el diseño de Horacio quedó varias semanas solo en un disco porque estaba dentro de la carpeta del agente (excluida del repo del constructor) y además ignorado en el repo del agente. Desde el 16-11, el diseño va en `disenos/<agente>/` del repo del constructor.
4. **Commits sin Push se acumulan sin que nadie lo note.** Revisar `git status` al inicio de cada sesión y avisar si hay commits locales sin subir.
5. **Documentos reales nunca a git**, incluido Sandia. Los diseños pueden citar datos (repos privados), los originales no se suben.
6. **Por qué Sandia y no una memoria compartida:** se probó que dos personas editando el mismo archivo de texto (incluso líneas vecinas) generan conflictos, y que Excel y Word no se pueden mezclar (se pierde trabajo). Un archivo, un escritor.

## E. RELACIÓN CON DUFFCO Y FORMALIDADES

1. **Modelo comercial (aprobado al 100% por Duffco el 22-10):** precio fijo por proceso implementado, no por hora. Base $450.000 bruto por proceso (piso, sin rebaja). Integración a medida (por ejemplo, una API) desde +$250.000 cada una. Conectores existentes (Drive, correo) incluidos en la base. Soporte incluido mientras haya un proceso en curso o hasta 3 meses desde el último cierre. Propiedad: los agentes son de Duffco, la metodología es de quien la construye.
2. **Se cobra la implementación entregada, no el uso.** El proceso 1 se cobró con Horacio instalado aunque Fabiana aún no lo usaba; la primera obra real queda cubierta por el soporte.
3. **Catalina pide por cada proceso:** una bitácora en Word para Duffco y una carta Gantt (Santi tiene un Excel con una hoja por proceso y una plantilla: semana 1 diagnóstico, semana 2 trabajo personal, semana 3 implementación, acompañamiento, cierre y boleta, soporte 3 meses, revisión a 1 o 2 meses). Mantenerlas al día cuando haya reuniones o hitos. Pide a Santi la plantilla o arma la tuya con la misma estructura.
4. **Adopción es el riesgo más subestimado.** Horacio está instalado desde el 21-10 y Fabiana no lo ha usado por falta de tiempo. Contractualmente es su responsabilidad, pero sin uso no hay línea base ni ROI. Mitigación: ofrecer acompañamiento de 30 minutos en el primer caso real y diseñar el agente para que el primer uso sea corto.
5. **La revisión a las 2 semanas no se hizo** porque no había uso real. Agenda la revisión después del primer caso real, no por calendario.

## F. ESTADO DE LOS PROCESOS DE SANTI (al 2026-11-16)

- **Proceso 1, pólizas (Fabiana):** Horacio v0.1, en pruebas, sin uso real. Usa la B-12 como caso resuelto.
- **Proceso 2, propuesta económica y APU (Nicolás):** levantamiento inicial el 11-11. La postulación a licitaciones se divide en varios procesos y este es el primero: el armado de APU es la tarea más tediosa de Nicolás. Insumos: el "Excel Julio" (lo entrega Julio Duflock, jefe de Nicolás, como punto de partida de cada oferta; desde ahí se llega a los costos [P]), un Excel utility de Nicolás y la base de datos histórica de insumos y materiales de su plataforma de presupuestos (CTBudget [P]: sin conector ni API conocida; se trabaja por exportación a Excel). Briefing completo pendiente.
- **Otros subprocesos de la postulación** (ficha u oferta técnica, estudio de bases, admisibilidad, etc.): sin dueño. Candidatos naturales para Lucas; se reparten conversándolo.
- **API de Mercado Público** (explorada el 14-10): gratuita [V], ticket personal por ClaveÚnica, uno por persona [V], 10.000 consultas diarias [V], entrega metadatos (estado, montos, plazos, ítems, adjudicación) [V]. Que entregue los adjuntos (bases, anexos; un proyecto puede tener ~70 documentos) está en [P]: requiere prueba técnica con un código de licitación real. Postura ante Duffco: "factible, sujeto a prueba técnica". En producción, el ticket debe ser de una persona de Duffco. Nunca se escribe en un archivo.

## G. PEQUEÑAS COSAS QUE AHORRAN TIEMPO

- Santi no quiere guiones largos en ningún texto: es convención del proyecto.
- El usuario deja documentos solo en `EntradasTemporales/` (del constructor) o `ENTRADAS/` (del agente); el agente ordena.
- Etiquetar todo dato con [V]/[P]/[H] desde la primera nota evita retrabajo.
- RUT institucionales (MOP 61.202.000-0, Duffco 77.119.761-2) son públicos y pueden ir en conocimiento; RUT de personas no.
- Las bases de cada licitación pueden subir montos y plazos de las garantías: siempre mandan las bases del contrato específico.
