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