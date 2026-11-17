# PROTOCOLO DE REPOSITORIOS Y DATOS

Versión: 1.0 (Zurgo) | Fecha: 2026-11-16 | Base: protocolo de Dr. Sayin Duffco v1.1
Se lee ante cualquier tema de git, GitHub, Sandia, respaldo o manejo de documentos de Duffco.

---

## 1. MODELO DE PROPIEDAD

| Qué | Dónde | Dueño | Por qué |
|---|---|---|---|
| Zurgo (núcleo, protocolos, plantillas, bitácora, diseños) | Repositorio privado `zurgo-duffco` en la **cuenta personal de GitHub de Lucas** | Lucas | Es su herramienta de trabajo |
| Cada agente entregado a Duffco | Un repositorio privado por agente en la organización de GitHub de Duffco, **`duffco-spa`** (owner: Santi, con `ssalas@duffco.cl`). Lucas pide acceso a Santi cuando construya su primer agente | Duffco | Duffco puede darle acceso a otra persona para mantenerlo |
| Coordinación con Santi | Repositorio privado **`Sandia`** (cuenta de Santi, Lucas colaborador). Carpetas `duffco/santi/` y `duffco/lucas/` | Santi y Lucas | Comunicación entre Sayin y Zurgo sin acceso a los repos privados del otro y sin conflictos de git |

---

## 1b. UBICACIÓN LOCAL

- Los repositorios viven en una carpeta **fuera de cualquier nube sincronizada** (iCloud, OneDrive, Google Drive). En Mac, por ejemplo `~/ProyectGIT/`; en Windows, `C:\Users\<usuario>\ProyectGIT\`. Nunca en Escritorio, Documentos ni Descargas: la sincronización puede subir documentos de `insumos/` a la nube y corromper la carpeta `.git`.
- `zurgo-duffco` y `Sandia` quedan lado a lado en esa carpeta.

---

## 2. QUÉ VA Y QUÉ NUNCA VA A UN REPOSITORIO

**Sí va:** instrucciones (`.md`), protocolos, plantillas, conocimiento permanente público o aprobado (normativa, manuales MOP), diseños de agentes (`disenos/`), bitácora, changelog, README. Un diseño puede citar datos de una obra (montos, fechas, RUT institucionales) porque el repositorio es privado; los documentos originales igual se quedan en `insumos/`.

**Nunca va:**
- Documentos reales de Duffco: pólizas, bases, contratos, planillas internas, Excel de presupuestos, correos.
- Datos personales de trabajadores o terceros (RUT de personas, teléfonos, direcciones).
- Credenciales, tokens, contraseñas, tickets o claves de API.
- Archivos de salida de un agente con datos reales.

En **Sandia** va todavía menos: solo reportes en Markdown, sin documentos de ningún tipo.

Regla práctica: si un archivo te haría dudar en mostrarlo a un desconocido, no va al repositorio.

---

## 3. `.gitignore`

En la raíz de `zurgo-duffco/`: `insumos/`, `entregas/`, `agentes/`, `EntradasTemporales/`, archivos del sistema y patrones de credenciales. `agentes/` se excluye porque cada agente es su propio repositorio. En cada agente, partir de `plantillas/agente/.gitignore` y el de `ejemplos/horacio/.gitignore` (excluye `obras/`, `historico/` y la bandeja de entrada).

---

## 4. FLUJO CON GITHUB DESKTOP

- **Zurgo** hace `git status`, `git log`, `git add` y `git commit` en la carpeta.
- **Lucas** hace Fetch, Pull y Push en GitHub Desktop.
- **Cowork y los `.lock`:** en Claude Desktop (Cowork) la carpeta conectada no permite borrar por defecto, y git necesita borrar sus propios archivos temporales. Si un commit deja `.git/*.lock` o `tmp_obj_*`, pide a Lucas el permiso de borrado sobre la carpeta (una vez por sesión) y elimínalos; si no, GitHub Desktop fallará con "File exists".
- **Repos anidados:** una carpeta que es su propio repositorio (como `agentes/<nombre>/`) no se respalda en el repo que la contiene. Todo lo que deba respaldarse y no sea parte del agente (diseño, trazabilidad, pruebas) va en `disenos/<agente>/`. Así se perdió casi el diseño de Horacio.
- Mensajes de commit: `<área>: <qué cambió>`, en español, cortos.

---

## 5. DOCUMENTOS DE DUFFCO

- Lucas deja los documentos solo en `EntradasTemporales/`. Zurgo los clasifica y los mueve a `insumos/<proceso>/<caso>/` con nombres claros.
- Cada uno recibe los documentos de su proceso directamente de su contraparte en Duffco. Si necesitas un documento de un proceso de Santi, lo pides por Sandia; no se copian por git.
- Para demos, anonimizar cuando sea posible.
