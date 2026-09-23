# Consolidación asíncrona de saldos

La plataforma de gestión de cuentas debe consultar saldos de dos fuentes distintas: el core bancario y el sistema de liquidación. Ambas fuentes operan con latencias diferentes y pueden fallar independientemente. El objetivo es consolidar los saldos de ambas fuentes en una única respuesta sin bloquear el event loop y manejando los errores de forma explícita.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | servicios asincronicos con fastapi |
| **Nivel** | advanced-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Consulta de saldos en una fuente

**Objetivo:** Implementar la consulta de saldos en el core bancario, asegurando que la operación no bloquea el event loop.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Diseña la operación de consulta de saldos en el core bancario.
- Asegura que la operación es asíncrona y no bloquea el event loop.
- Define y maneja los posibles errores de la operación.

**Entregable:** Operación asíncrona de consulta de saldos en el core bancario con manejo explícito de errores.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el uso de async/await para operaciones no bloqueantes.
- Piensa en cómo modelar los errores del dominio de forma explícita.

</details>

### Fase 2: Consulta de saldos en la segunda fuente

**Objetivo:** Implementar la consulta de saldos en el sistema de liquidación, asegurando que la operación es asíncrona y manejando los errores de forma explícita.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Diseña la operación de consulta de saldos en el sistema de liquidación.
- Asegura que la operación es asíncrona y no bloquea el event loop.
- Define y maneja los posibles errores de la operación.

**Entregable:** Operación asíncrona de consulta de saldos en el sistema de liquidación con manejo explícito de errores.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el uso de async/await para operaciones no bloqueantes.
- Piensa en cómo modelar los errores del dominio de forma explícita.

</details>

### Fase 3: Consolidación de saldos

**Objetivo:** Consolidar los saldos de las dos fuentes en una única respuesta, asegurando que la operación es asíncrona y manejando los errores de forma explícita.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Diseña la operación de consolidación de saldos de las dos fuentes.
- Asegura que la operación es asíncrona y no bloquea el event loop.
- Define y maneja los posibles errores de la operación.

**Entregable:** Operación asíncrona de consolidación de saldos de las dos fuentes con manejo explícito de errores.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el uso de async/await para operaciones no bloqueantes.
- Piensa en cómo modelar los errores del dominio de forma explícita.

</details>

### Fase 4: Exposición de la consulta de saldos consolidados

**Objetivo:** Exponer la consulta de saldos consolidados a través de una API asíncrona.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Diseña la API asíncrona para exponer la consulta de saldos consolidados.
- Asegura que la operación es asíncrona y no bloquea el event loop.
- Define y maneja los posibles errores de la operación.

**Entregable:** API asíncrona para consultar saldos consolidados con manejo explícito de errores.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el uso de async/await para operaciones no bloqueantes.
- Piensa en cómo modelar los errores del dominio de forma explícita.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una operación asíncrona y por qué es importante en este contexto?
- **paraQueSirve**: ¿Para qué sirve el manejo explícito de errores en este reto?
- **comoSeUsa**: ¿Cómo se usa async/await para asegurar que una operación no bloquea el event loop?
- **erroresComunes**: ¿Cuáles son los errores comunes que se deben considerar en este dominio y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones implica el diseño de una operación asíncrona en este contexto?

## Criterios de Evaluacion

- Implementación de operaciones asíncronas sin bloquear el event loop.
- Manejo explícito de errores del dominio.
- Consolidación correcta de saldos de las dos fuentes.
- Exposición de la consulta de saldos consolidados a través de una API asíncrona.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && python -c "import app.main"
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
