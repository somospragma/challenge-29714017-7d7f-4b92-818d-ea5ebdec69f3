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