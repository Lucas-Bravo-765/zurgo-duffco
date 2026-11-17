# Zurgo · cómo instalarlo (para Lucas)

Semilla preparada por Dr. Sayin Duffco el 2026-11-16. Zurgo ya viene adaptado a ti: solo falta instalarlo y hacer su primera activación.

## 1. Carpeta y repositorio
1. Descomprime `zurgo-duffco/` en una carpeta **fuera de iCloud, OneDrive o Google Drive** (Mac: `~/ProyectGIT/zurgo-duffco`; Windows: `C:\Users\<usuario>\ProyectGIT\zurgo-duffco`).
2. En GitHub Desktop: File → Add Local Repository → elige la carpeta → "create a repository" → Publish **como privado** en tu cuenta.
3. Acepta la invitación de Santi al repo **Sandia** y clónalo al lado: `.../ProyectGIT/Sandia`.

## 2. Claude Desktop
1. Crea un Project llamado "Zurgo" y pega el contenido de `INSTRUCCION_INTERFAZ.txt` como instrucciones.
2. Conecta las carpetas `zurgo-duffco` y `Sandia`.
3. Revisa en la configuración de privacidad de tu cuenta que **no** esté activado el uso de tus chats para entrenar modelos (vas a trabajar con información de Duffco).
4. Extended Thinking: a tu criterio para Zurgo; apagado en los agentes que entregues.

## 3. Primera activación
Abre una conversación en el Project y escribe "Hola Zurgo". Debe leer su núcleo, la carta de bienvenida en Sandia y los aprendizajes del proyecto, y después hacerte preguntas sobre cómo te gusta trabajar. Con eso completa tu perfil (sección 2 del núcleo).

## Qué trae
- `memoria/`: núcleo 1.0, aprendizajes del proyecto, contexto de Duffco v1.2, protocolos (creación, entrega e instalación, auto-modificación, repositorios y datos), plantillas, registro y bitácora con la sesión 0.
- `ejemplos/`: Horacio completo (núcleo, flujo, conocimiento, criterio, herramientas, guía de instalación), su diseño (P1, trazabilidad, checklist con errores de prueba, diff de auto-modificación) y el perfil de Fabiana como ejemplo de perfil de usuario. Es referencia: no lo modifiques ni lo instales.

## Qué conversar con Santi antes de cambiar
- Las reglas duras (sección 5 del núcleo): puedes agregar; quitar se conversa.
- Dónde viven los agentes entregados (`duffco-spa`) y las formalidades para Catalina (bitácora y Gantt por proceso).
