# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Superficie de practica — NO resuelvas

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs.

- `tests/test_core_banking_adapter.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.
- `tests/test_settlement_system_adapter.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.
- `tests/test_get_consolidated_balance.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Boilerplate del stack que falta

Sin esto no compila ni arranca. Es andamiaje, no toca nada de lo pedagogico:

- **__init__.py** — Sin __init__.py, app no es un paquete importable y "import app.main" falla.

### Referencias colgando en el codigo que si esta

Cada una rompe la compilacion:

- `app/api/routes/balance_routes.py` — `BalanceSchema.get`: Se invoca `get` sobre `BalanceSchema`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

## Como saber que terminaste

```bash
pip install -r requirements.txt && python -c "import app.main"
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Backend, Especialidad Desarrollador, Tecnología Python, Advanced

### Brecha de conocimiento
Maneja operaciones de I/O sin bloquear el event loop y modela los errores del dominio de forma explicita

### Misión / candidato
Exponer la consulta de saldos consolidando dos fuentes

### Datos adicionales
Candidato con 3 años en Python

### Reto
- Tema: servicios asincronicos con fastapi
- Seniority: advanced-l2
- Tipo: practical
- Título: Consolidación asíncrona de saldos
- Tiempo estimado: 8 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Consulta de saldos en una fuente — objetivo: Implementar la consulta de saldos en el core bancario, asegurando que la operación no bloquea el event loop. — entregable (NO resolver): Operación asíncrona de consulta de saldos en el core bancario con manejo explícito de errores.
- Fase 2: Consulta de saldos en la segunda fuente — objetivo: Implementar la consulta de saldos en el sistema de liquidación, asegurando que la operación es asíncrona y manejando los errores de forma explícita. — entregable (NO resolver): Operación asíncrona de consulta de saldos en el sistema de liquidación con manejo explícito de errores.
- Fase 3: Consolidación de saldos — objetivo: Consolidar los saldos de las dos fuentes en una única respuesta, asegurando que la operación es asíncrona y manejando los errores de forma explícita. — entregable (NO resolver): Operación asíncrona de consolidación de saldos de las dos fuentes con manejo explícito de errores.
- Fase 4: Exposición de la consulta de saldos consolidados — objetivo: Exponer la consulta de saldos consolidados a través de una API asíncrona. — entregable (NO resolver): API asíncrona para consultar saldos consolidados con manejo explícito de errores.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: pyproject.toml ===
[tool.poetry]
name = "consolidated-balance-service"
version = "0.1.0"
description = "Servicio de consolidación asíncrona de saldos entre core bancario y sistema de liquidación"
authors = ["Pragma" ]
license = "MIT"
readme = "README.md"
packages = [
    { include = "app" }
]

[tool.poetry.dependencies]
python = "^3.13"
fastapi = "0.115.0"
uvicorn = "0.30.1"
pydantic = "2.8.2"
httpx = "0.27.0"
python-dotenv = "1.0.1"
dependency-injector = "4.42.0"
aiohttp = "3.9.3"

[tool.poetry.group.dev.dependencies]
pytest = "8.2.0"
pytest-asyncio = "0.23.7"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.pytest.ini_options]
asyncio_mode = "auto"

# Configuración para ejecución con Uvicorn
[tool.uvicorn]
host = "0.0.0.0"
port = 8000
reload = true

// === ARCHIVO: app/main.py ===
"""
Entry point de la aplicación FastAPI para la consolidación asíncrona de saldos.
"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.infrastructure.config.settings import Settings
from app.api.routes.balance_routes import router as balance_router
from app.domain.exceptions.consolidation_exception import ConsolidationException
from dependency_injector import containers, providers
import logging
import asyncio

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class Container(containers.DeclarativeContainer):
    """
    Contenedor de inyección de dependencias para el servicio.
    """
    settings = providers.Configuration()
    settings.from_pydantic(Settings())
    
    # Aquí se registrarían los adaptadores y casos de uso
    # Ejemplo: core_banking_adapter = providers.Factory(CoreBankingAdapter, base_url=settings.core_banking_url)

app = FastAPI(
    title="Consolidated Balance Service",
    description="Servicio para consolidar saldos entre core bancario y sistema de liquidación",
    version="0.1.0"
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Manejador global de errores
@app.exception_handler(ConsolidationException)
async def consolidation_exception_handler(request: Request, exc: ConsolidationException):
    """
    Maneja excepciones personalizadas del dominio de consolidación.
    """
    logger.error(f"Error en consolidación: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    """
    Maneja excepciones genéricas no controladas.
    """
    logger.error(f"Error inesperado: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": "Error interno del servidor"},
    )

# Inclusión de rutas
app.include_router(balance_router, prefix="/api/v1", tags=["balances"])

@app.get("/health")
async def health_check():
    """
    Endpoint de health check para verificar que el servicio está operativo.
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )

// === ARCHIVO: app/infrastructure/config/settings.py ===
"""
Configuración centralizada para la aplicación.
"""
from pydantic_settings import BaseSettings
from pydantic import Field, AnyHttpUrl
from typing import Optional

class Settings(BaseSettings):
    """
    Configuración de la aplicación con valores por defecto y validación.
    Los valores pueden ser sobrescritos por variables de entorno.
    """
    # Configuración del core bancario
    core_banking_url: AnyHttpUrl = Field(
        default="http://localhost:8001/api/v1/balances",
        description="URL base del servicio de core bancario"
    )
    core_banking_timeout: int = Field(
        default=5,
        description="Timeout en segundos para las llamadas al core bancario"
    )
    core_banking_retry_attempts: int = Field(
        default=3,
        description="Número de reintentos para las llamadas al core bancario"
    )
    
    # Configuración del sistema de liquidación
    settlement_system_url: AnyHttpUrl = Field(
        default="http://localhost:8002/api/v1/settlements",
        description="URL base del sistema de liquidación"
    )
    settlement_system_timeout: int = Field(
        default=5,
        description="Timeout en segundos para las llamadas al sistema de liquidación"
    )
    settlement_system_retry_attempts: int = Field(
        default=3,
        description="Número de reintentos para las llamadas al sistema de liquidación"
    )
    
    # Configuración de la aplicación
    app_name: str = Field(
        default="Consolidated Balance Service",
        description="Nombre de la aplicación"
    )
    debug: bool = Field(
        default=False,
        description="Modo debug para desarrollo"
    )
    
    # Configuración de logging
    log_level: str = Field(
        default="INFO",
        description="Nivel de logging de la aplicación"
    )
    
    class Config:
        env_file = ".env"
        extra = "ignore"

# Instancia global de configuración
settings = Settings()"

// === ARCHIVO: app/domain/entities/account_balance.py ===
from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import Optional

class AccountBalance(BaseModel):
    """
    Entidad que representa el saldo consolidado de una cuenta.
    Contiene información tanto del core bancario como del sistema de liquidación.
    """
    account_id: str
    core_balance: Decimal
    core_timestamp: datetime
    settlement_balance: Decimal
    settlement_timestamp: datetime
    consolidated_balance: Decimal
    last_updated: datetime
    status: str
    core_error: Optional[str] = None
    settlement_error: Optional[str] = None

    class Config:
        json_encoders = {
            Decimal: lambda v: str(v),
            datetime: lambda v: v.isoformat()
        }

    def __init__(__pydantic_self__, **data) -> None:
        """
        Constructor que inicializa los valores por defecto para timestamps y balances.
        """
        defaults = {
            'core_balance': Decimal('0.00'),
            'core_timestamp': datetime.min,
            'settlement_balance': Decimal('0.00'),
            'settlement_timestamp': datetime.min,
            'consolidated_balance': Decimal('0.00'),
            'last_updated': datetime.min,
            'status': 'PENDING',
            'core_error': None,
            'settlement_error': None
        }
        defaults.update(data)
        super().__init__(**defaults)

    def update_core_balance(self, balance: Decimal, timestamp: datetime, error: Optional[str] = None) -> None:
        """
        Actualiza el saldo y timestamp del core bancario.
        Args:
            balance: Saldo reportado por el core bancario.
            timestamp: Momento en que se reportó el saldo.
            error: Mensaje de error si la consulta falló.
        """
        self.core_balance = balance
        self.core_timestamp = timestamp
        self.core_error = error
        self._update_consolidated()

    def update_settlement_balance(self, balance: Decimal, timestamp: datetime, error: Optional[str] = None) -> None:
        """
        Actualiza el saldo y timestamp del sistema de liquidación.
        Args:
            balance: Saldo reportado por el sistema de liquidación.
            timestamp: Momento en que se reportó el saldo.
            error: Mensaje de error si la consulta falló.
        """
        self.settlement_balance = balance
        self.settlement_timestamp = timestamp
        self.settlement_error = error
        self._update_consolidated()

    def _update_consolidated(self) -> None:
        """
        Calcula el saldo consolidado basado en los saldos disponibles.
        Prioriza el saldo más reciente si hay discrepancias.
        """
        current_time = datetime.utcnow()

        # Determinar qué balances están disponibles
        core_available = self.core_error is None
        settlement_available = self.settlement_error is None

        if core_available and settlement_available:
            # Ambos disponibles: usar el más reciente
            if self.core_timestamp > self.settlement_timestamp:
                self.consolidated_balance = self.core_balance
            else:
                self.consolidated_balance = self.settlement_balance
            self.status = 'CONSOLIDATED'
        elif core_available:
            # Solo core disponible
            self.consolidated_balance = self.core_balance
            self.status = 'PARTIAL_CORE'
        elif settlement_available:
            # Solo settlement disponible
            self.consolidated_balance = self.settlement_balance
            self.status = 'PARTIAL_SETTLEMENT'
        else:
            # Ninguno disponible
            self.consolidated_balance = Decimal('0.00')
            self.status = 'ERROR'

        self.last_updated = current_time

    def is_successful(self) -> bool:
        """Verifica si la consolidación fue exitosa (ambos sistemas respondieron sin errores)."""
        return self.status == 'CONSOLIDATED'

    def has_errors(self) -> bool:
        """Verifica si hubo errores en alguna de las fuentes."""
        return self.core_error is not None or self.settlement_error is not None

// === ARCHIVO: app/domain/exceptions/core_banking_exception.py ===
class CoreBankingException(Exception):
    """
    Excepción personalizada para errores provenientes del core bancario.
    Contiene información sobre el tipo de error y el contexto en que ocurrió.
    """
    def __init__(self, message: str, error_code: str = None, details: dict = None):
        """
        Args:
            message: Mensaje descriptivo del error.
            error_code: Código de error específico del core bancario.
            details: Detalles adicionales sobre el error.
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.details = details or {}

    def __str__(self) -> str:
        base = f"CoreBankingException: {self.message}"
        if self.error_code:
            base += f" [Code: {self.error_code}]"
        if self.details:
            base += f" Details: {self.details}"
        return base

    def to_dict(self) -> dict:
        """Convierte la excepción a un diccionario para serialización."""
        return {
            'message': self.message,
            'error_code': self.error_code,
            'details': self.details,
            'type': self.__class__.__name__
        }

// === ARCHIVO: app/domain/exceptions/settlement_system_exception.py ===
class SettlementSystemException(Exception):
    """
    Excepción personalizada para errores provenientes del sistema de liquidación.
    Contiene información sobre el tipo de error y el contexto en que ocurrió.
    """
    def __init__(self, message: str, error_code: str = None, details: dict = None):
        """
        Args:
            message: Mensaje descriptivo del error.
            error_code: Código de error específico del sistema de liquidación.
            details: Detalles adicionales sobre el error.
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.details = details or {}

    def __str__(self) -> str:
        base = f"SettlementSystemException: {self.message}"
        if self.error_code:
            base += f" [Code: {self.error_code}]"
        if self.details:
            base += f" Details: {self.details}"
        return base

    def to_dict(self) -> dict:
        """Convierte la excepción a un diccionario para serialización."""
        return {
            'message': self.message,
            'error_code': self.error_code,
            'details': self.details,
            'type': self.__class__.__name__
        }

// === ARCHIVO: app/domain/exceptions/consolidation_exception.py ===
from abc import ABC
from typing import Optional
from pydantic import ValidationError

from app.domain.exceptions.core_banking_exception import CoreBankingException
from app.domain.exceptions.settlement_system_exception import SettlementSystemException

class ConsolidationException(Exception, ABC):
    def __init__(self, message: str, error_code: Optional[str] = None, details: Optional[dict] = None):
        super().__init__(message)
        self.error_code = error_code
        self.details = details

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(message={self.args[0]}, error_code={self.error_code}, details={self.details})" if self.details else f"{self.__class__.__name__}(message={self.args[0]}, error_code={self.error_code})"

    def to_dict(self) -> dict:
        return {"error_code": self.error_code, "message": self.args[0], "details": self.details}

// === ARCHIVO: app/domain/ports/core_banking_port.py ===
from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.account_balance import AccountBalance

class CoreBankingPort(ABC):
    @abstractmethod
    async def get_balance(self, account_id: str) -> Optional[AccountBalance]:
        """Retrieves the balance for a given account ID."""
        raise NotImplementedError

// === ARCHIVO: app/domain/ports/settlement_system_port.py ===
from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.account_balance import AccountBalance

class SettlementSystemPort(ABC):
    @abstractmethod
    async def get_balance(self, account_id: str) -> Optional[AccountBalance]:
        """Retrieves the balance for a given account ID."""
        raise NotImplementedError

// === ARCHIVO: app/api/schemas/balance_schema.py ===
from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime
from typing import Optional

class BalanceSchema(BaseModel):
    account_id: str = Field(..., description="Identificador único de la cuenta.")
    core_balance: Decimal = Field(..., description="Saldo en el core bancario.")
    settlement_balance: Decimal = Field(..., description="Saldo en el sistema de liquidación.")
    consolidated_balance: Optional[Decimal] = Field(None, description="Saldo consolidado de ambas fuentes.")
    core_timestamp: Optional[datetime] = Field(None, description="Timestamp de la última actualización del saldo en el core.")
    settlement_timestamp: Optional[datetime] = Field(None, description="Timestamp de la última actualización del saldo en el sistema de liquidación.")
    core_error: Optional[str] = Field(None, description="Error en la última consulta al core bancario.")
    settlement_error: Optional[str] = Field(None, description="Error en la última consulta al sistema de liquidación.")

    def __init__(self, **data):
        super().__init__(**data)
        self._validate_invariants()

    def _validate_invariants(self):
        if self.core_balance is None and self.settlement_balance is None:
            raise ValueError("Al menos uno de los saldos debe ser proporcionado.")
        if self.core_error and not self.core_balance:
            raise ValueError("El error en el core no puede existir sin un saldo.")
        if self.settlement_error and not self.settlement_balance:
            raise ValueError("El error en el sistema de liquidación no puede existir sin un saldo.")

// === ARCHIVO: app/api/routes/balance_routes.py ===
from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from app.containers import Container
from app.application.use_cases.get_consolidated_balance import GetConsolidatedBalance
from app.api.schemas.balance_schema import BalanceSchema

router = APIRouter()

@router.get('/balances/consolidated', response_model=BalanceSchema)
@inject
async def get_consolidated_balances(
    use_case: GetConsolidatedBalance = Depends(Provide[Container.get_consolidated_balance])
):
    try:
        result = await use_case.execute()
        return BalanceSchema(**result.__dict__)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

// === ARCHIVO: __init__.py ===
"""Módulo de inicialización del paquete app."""

# Importar todos los submódulos necesarios para que el paquete sea importable.
from. import main, application, infrastructure, domain

// === ARCHIVO: README.md ===
# Servicio de Consolidación Asíncrona de Saldos

## Descripción
Este proyecto es un servicio de FastAPI que consolida saldos de dos fuentes distintas: el core bancario y el sistema de liquidación. Las consultas son asíncronas y manejan errores de forma explícita.

## Instalación
1. Clonar el repositorio.
2. Crear un entorno virtual y activarlo.
3. Instalar las dependencias con `poetry install`.

## Ejecución
1. Cargar las variables de entorno con `source.env`.
2. Iniciar el servicio con `poetry run uvicorn app.main:app --reload`.

## Estructura del Proyecto
- `app/`: Carpeta principal del proyecto.
  - `main.py`: Punto de entrada de la aplicación.
  - `application/`: Casos de uso y lógica de la aplicación.
  - `infrastructure/`: Configuración y adaptadores de la infraestructura.
  - `domain/`: Entidades y excepciones del dominio.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.

// === ARCHIVO: app/application/use_cases/get_consolidated_balance.py ===
from dependency_injector.wiring import Provide, inject
from fastapi import BackgroundTasks, Depends
from typing import Optional
from app.domain.entities.account_balance import AccountBalance
from app.domain.exceptions.core_banking_exception import CoreBankingException
from app.domain.exceptions.settlement_system_exception import SettlementSystemException
from app.domain.ports.core_banking_port import CoreBankingPort
from app.domain.ports.settlement_system_port import SettlementSystemPort


class GetConsolidatedBalanceUseCase:
    @inject
    def __init__(self,
                 core_banking_port: CoreBankingPort = Depends(Provide['core_banking_port']),
                 settlement_system_port: SettlementSystemPort = Depends(Provide['settlement_system_port'])):
        self.core_banking_port = core_banking_port
        self.settlement_system_port = settlement_system_port

    async def execute(self, account_id: str) -> AccountBalance:
        try:
            core_balance = await self.core_banking_port.get_balance(account_id)
            settlement_balance = await self.settlement_system_port.get_balance(account_id)
        except (CoreBankingException, SettlementSystemException) as e:
            raise ConsolidationException(str(e))

        consolidated_balance = AccountBalance()
        consolidated_balance.update_core_balance(core_balance, datetime.now())
        consolidated_balance.update_settlement_balance(settlement_balance, datetime.now())
        consolidated_balance._update_consolidated()

        return consolidated_balance

// === ARCHIVO: app/infrastructure/adapters/core_banking_adapter.py ===
from dependency_injector import containers, providers
from httpx import AsyncClient
from pydantic import Decimal, BaseModel, ValidationError
from app.domain.entities import AccountBalance
from app.domain.exceptions import CoreBankingException


class CoreBankingAdapter(containers.DeclarativeContainer):

    config = providers.Configuration()

    async_client = providers.Singleton(AsyncClient)

    async def get_balance(self, account_id: str) -> AccountBalance:
        try:
            response = await self.async_client().get(f"{self.config.core_banking_url}/balances/{account_id}")
            response.raise_for_status()
            data = response.json()
            balance = Decimal(data['balance'])
            timestamp = data['timestamp']
            return AccountBalance(balance=balance, timestamp=timestamp)
        except (ValidationError, httpx.HTTPStatusError) as e:
            raise CoreBankingException(f"Error retrieving balance from Core Banking: {e}")

// === ARCHIVO: app/infrastructure/adapters/settlement_system_adapter.py ===
from dependency_injector import containers, providers
from httpx import AsyncClient
from pydantic import Decimal, BaseModel, ValidationError
from app.domain.entities import AccountBalance
from app.domain.exceptions import SettlementSystemException


class SettlementSystemAdapter(containers.DeclarativeContainer):

    config = providers.Configuration()

    async_client = providers.Singleton(AsyncClient)

    async def get_balance(self, account_id: str) -> AccountBalance:
        try:
            response = await self.async_client().get(f"{self.config.settlement_system_url}/balances/{account_id}")
            response.raise_for_status()
            data = response.json()
            balance = Decimal(data['balance'])
            timestamp = data['timestamp']
            return AccountBalance(balance=balance, timestamp=timestamp)
        except (ValidationError, httpx.HTTPStatusError) as e:
            raise SettlementSystemException(f"Error retrieving balance from Settlement System: {e}")

// === ARCHIVO: tests/test_core_banking_adapter.py ===
import pytest
from app.infrastructure.adapters.core_banking_adapter import CoreBankingAdapter

@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_balance():
    adapter = CoreBankingAdapter()
    balance = await adapter.get_balance("account_id")
    assert balance is not None

// === ARCHIVO: tests/test_settlement_system_adapter.py ===
import pytest
from app.infrastructure.adapters.settlement_system_adapter import SettlementSystemAdapter

@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_balance():
    adapter = SettlementSystemAdapter()
    balance = await adapter.get_balance("account_id")
    assert balance is not None

// === ARCHIVO: tests/test_get_consolidated_balance.py ===
import pytest
from app.application.use_cases.get_consolidated_balance import GetConsolidatedBalance

@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_consolidated_balance():
    use_case = GetConsolidatedBalance()
    balance = await use_case.execute("account_id")
    assert balance is not None
```
