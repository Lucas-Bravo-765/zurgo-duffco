# DIFF NIVEL C · memoria/protocolos/auto_modificacion.md, sección 5

Motivo: Santi decidió (2026-10-14) que los agentes entregados puedan editar parte de sus instrucciones a pedido del usuario, con límites. El texto actual bloquea todo salvo `aprendizajes.md`.
Riesgo que introduce: el usuario podría degradar un flujo sin darse cuenta. Mitigación: la capa 1 queda bloqueada y la regla "agregar sí, quitar no" protege los controles.
Nivel: C (archivo de protocolos). Versión: 1.0 → 1.1.

## Texto actual

> ## 5. AUTO-MODIFICACIÓN EN LOS AGENTES QUE ENTREGAS
>
> Los agentes de Duffco heredan el patrón, con más restricciones, porque sus usuarios no son arquitectos:
> - Su núcleo (`00_NUCLEO.md`) queda **bloqueado**: el agente no puede editarlo. Solo Santi (contigo) lo cambia, con versión y commit en el repositorio del agente.
> - El agente sí puede escribir en su `aprendizajes.md`: preferencias del usuario, correcciones recurrentes, formatos que funcionaron. Nunca reglas nuevas ni excepciones a sus reglas duras.
> - En cada mantención, revisas `aprendizajes.md` con Santi y decides qué se promueve al núcleo del agente (con el flujo de la sección 3) y qué se limpia.

## Texto propuesto

> ## 5. AUTO-MODIFICACIÓN EN LOS AGENTES QUE ENTREGAS
>
> Los agentes de Duffco se modifican en tres capas, porque sus usuarios conocen el proceso pero no son arquitectos:
>
> | Capa | Archivos | Quién la cambia | Cómo |
> |---|---|---|---|
> | **1. Reglas duras** | `memoria/00_NUCLEO.md` | Solo Santi contigo | Flujo de la sección 3, versión y commit en el repositorio del agente |
> | **2. Flujo y formatos** | `memoria/flujo/` y plantillas | El agente, a pedido explícito del usuario | Muestra el antes y el después en lenguaje simple, pide confirmación, respalda en `_historial/`, registra en `CHANGELOG.md` |
> | **3. Criterio y aprendizajes** | `memoria/criterio/`, `memoria/aprendizajes.md` | El agente, libremente | Cada entrada con fecha, origen ("Fabiana corrigió...") y etiqueta de confianza |
>
> Reglas:
> - **Agregar sí, quitar no:** en la capa 2 el agente puede agregar pasos o verificaciones; para quitar o debilitar una verificación, o cambiar algo que toque la capa 1, responde que lo anota para Santi y lo deja en `aprendizajes.md` como propuesta.
> - Ningún cambio de capa 2 o 3 puede contradecir la capa 1. Si lo hace, la capa 1 prevalece y el agente lo dice.
> - En cada mantención revisas con Santi el `CHANGELOG.md` y las capas 2 y 3: qué se consolida, qué se promueve a la capa 1 (sección 3) y qué se revierte.
