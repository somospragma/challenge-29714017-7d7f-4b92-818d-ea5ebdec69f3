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