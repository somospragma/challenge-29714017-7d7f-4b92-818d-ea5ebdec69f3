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