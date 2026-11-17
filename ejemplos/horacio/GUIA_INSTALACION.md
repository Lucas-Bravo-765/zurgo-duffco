# GUÍA DE INSTALACIÓN · Asistente de pólizas (para Santi)

Versión 0.1 · 2026-10-21. La interfaz de Claude Desktop cambia seguido: si un botón no se llama igual, busca el equivalente.

## A. Claude Team de Duffco (en tu computador o en el de ella)

1. Contrata el plan Team en claude.ai con `ssalas@duffco.cl` (tú: administrador). Invita a Fabiana con su correo de Duffco (asiento Standard).
2. En **Organization settings > Capabilities**:
   - "Code execution and file creation": **activado**.
   - "Allow network egress": **"Package managers and specific domains"**, agregando `mindicador.cl`, `www.sii.cl` y `www.cmfchile.cl` (UF y consulta de pólizas). Sin esto, el agente le pedirá la UF a Fabiana: funciona igual, pero con un paso manual.
   - Cowork viene activado por defecto en Team; verifica que siga así.

## B. GitHub de Duffco

1. Cuenta de GitHub con `ssalas@duffco.cl` → **New organization → Free** → "A business or institution: Duffco Ingeniería y Construcción SpA".
2. Repositorio **privado** `agente-polizas`, vacío.
3. En tu Mac, desde la carpeta `sayin-duffco/agentes/agente-polizas`: inicializa el repositorio y súbelo (Sayin lo prepara; tú haces el Push).
4. Fabiana crea su cuenta de GitHub; la invitas a la organización con permiso de escritura en `agente-polizas`. Recomendado: un segundo owner de Duffco.

## C. En el computador de Fabiana (Windows, con SU cuenta)

1. Instala **Claude Desktop** desde claude.com/download e inicia sesión con su cuenta de Duffco.
2. Instala **GitHub Desktop**, inicia sesión con su cuenta y clona `duffco-ingenieria/agente-polizas` en:
   `C:\Users\<usuario>\AgentesDuffco\agente-polizas`
   **No en Documentos ni en el Escritorio** (suelen sincronizarse con OneDrive).
   Alternativa sin GitHub: descomprime el ZIP en esa misma ruta.
3. En Claude Desktop, abre **Cowork**, conecta la carpeta `agente-polizas` y pega el contenido de `INSTRUCCION_INTERFAZ.txt` como instrucciones (del proyecto o del espacio de trabajo).
4. Extended Thinking: apagado.
5. Copia el Excel de histórico de primas de Fabiana a `historico/`.

## D. Prueba de humo (10 minutos, contigo al lado)

1. Abre una conversación nueva: el agente debe leer su núcleo y saludar con el opener de primera vez.
2. Pídele: "Abre una obra de prueba llamada Prueba B-12". Debe crear la carpeta en `obras/`.
3. Copia en `obras/Prueba B-12/01_entrada/` la resolución y el acta técnica de la Ruta B-12, y pídele que arme la ficha. Debe dar: monto $5.478.886.204, plazo 420 días, tramitación 20-03-2025, apertura técnica 24-07-2024.
4. Pídele que calcule. Resultado esperado: FCC 4.374,73 UF hasta el 16-05-2028; RC 7.088,20 UF hasta el 16-05-2027; TRC 141.764 UF hasta el 15-05-2026; garantía adicional no aplica.
5. Si `herramientas/` falla por librerías, pídele que instale `herramientas/requirements.txt`.
6. Copia la póliza FCC de la B-12 en `04_polizas/v1/` y pídele que la revise: no debe encontrar errores críticos; debe marcar como LEVE la mención de cuotas y preguntar por la firma del apoderado.

## E. Primera sesión con Fabiana

Dile: "Ahora el asistente te va a hacer unas preguntas para aprender cómo trabajas". El agente sigue `memoria/flujo/primera_sesion.md` (16 preguntas en tandas de 3, incluido el nombre y la línea base de horas). Lo que responda queda en `memoria/aprendizajes.md`.

## F. Después

- Al terminar el día, en GitHub Desktop (en el PC de Fabiana): Commit + Push de `memoria/` (los documentos de `obras/` e `historico/` no se suben: están excluidos).
- Avisa a Sayin: revisamos `aprendizajes.md` y "Propuestas para Santi" y actualizamos el conocimiento.
