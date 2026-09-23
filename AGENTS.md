# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Consolidación asíncrona de saldos**.

| | |
|---|---|
| Tema | servicios asincronicos con fastapi |
| Nivel | advanced-l2 |
| Chapter | Backend |
| Especialidad | Python |
| Stack | Python 3.13 / FastAPI 0.115 |
| Patron arquitectonico | arquitectura hexagonal con separación de capas asíncronas |
| Tiempo estimado | 8 horas |

## Receta del stack

Esqueleto obligatorio:

- `pyproject.toml o requirements.txt en la raiz`
- `app/main.py con la instancia de FastAPI`
- `app/domain con entidades y puertos (Protocol o ABC)`
- `app/application con casos de uso`
- `app/infrastructure con repositorios y routers`

Dependencias:

- fastapi 0.115.0
- uvicorn 0.30.1
- pydantic 2.8.2
- httpx 0.27.0
- python-dotenv 1.0.1
- pytest 8.2.0
- pytest-asyncio 0.23.7
- dependency-injector 4.42.0
- aiohttp n/a

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `pip install -r requirements.txt && python -c "import app.main"` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `pip install -r requirements.txt && python -c "import app.main"` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Consulta de saldos en una fuente**: Operación asíncrona de consulta de saldos en el core bancario con manejo explícito de errores.
- **Fase 2 — Consulta de saldos en la segunda fuente**: Operación asíncrona de consulta de saldos en el sistema de liquidación con manejo explícito de errores.
- **Fase 3 — Consolidación de saldos**: Operación asíncrona de consolidación de saldos de las dos fuentes con manejo explícito de errores.
- **Fase 4 — Exposición de la consulta de saldos consolidados**: API asíncrona para consultar saldos consolidados con manejo explícito de errores.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Superficie de practica (NO completes)

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs. No toques la logica que el reto pide completar.

- [ ] `tests/test_core_banking_adapter.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.
- [ ] `tests/test_settlement_system_adapter.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.
- [ ] `tests/test_get_consolidated_balance.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.

## Lo que falta y tenes que completar

### 1. Boilerplate del stack (1)

Sin esto el proyecto no compila ni arranca. **Es tu trabajo crearlo**, y no toca nada de lo pedagogico: es andamiaje del stack.

- [ ] **__init__.py** — Sin __init__.py, app no es un paquete importable y "import app.main" falla.

### 2. Referencias colgando (1)

Salieron de un analisis estatico del codigo que SI esta en el repo. Cada una rompe la compilacion:

- [ ] `app/api/routes/balance_routes.py` — `BalanceSchema.get`
      Se invoca `get` sobre `BalanceSchema`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

### Presentes (19)

- `pyproject.toml`
- `app/main.py`
- `app/infrastructure/config/settings.py`
- `app/domain/entities/account_balance.py`
- `app/domain/exceptions/core_banking_exception.py`
- `app/domain/exceptions/settlement_system_exception.py`
- `app/domain/exceptions/consolidation_exception.py`
- `app/domain/ports/core_banking_port.py`
- `app/domain/ports/settlement_system_port.py`
- `app/api/schemas/balance_schema.py`
- `app/api/routes/balance_routes.py`
- `__init__.py`
- `README.md`
- `app/application/use_cases/get_consolidated_balance.py`
- `app/infrastructure/adapters/core_banking_adapter.py`
- `app/infrastructure/adapters/settlement_system_adapter.py`
- `tests/test_core_banking_adapter.py`
- `tests/test_settlement_system_adapter.py`
- `tests/test_get_consolidated_balance.py`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `app`
- `app/domain`
- `app/domain/entities`
- `app/domain/exceptions`
- `app/domain/ports`
- `app/application`
- `app/application/use_cases`
- `app/infrastructure`
- `app/infrastructure/adapters`
- `app/infrastructure/config`
- `app/api`
- `tests`

## Verificacion

```bash
pip install -r requirements.txt && python -c "import app.main"
```

El comando tiene que pasar SIN implementar los archivos de la superficie de practica: solo andamiaje.

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **arquitectura hexagonal con separación de capas asíncronas**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Backend, Especialidad Desarrollador, Tecnología Python, Advanced
- Brecha que el reto ataca: Maneja operaciones de I/O sin bloquear el event loop y modela los errores del dominio de forma explicita
- Mision: Exponer la consulta de saldos consolidando dos fuentes

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
