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