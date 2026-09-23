from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.account_balance import AccountBalance

class SettlementSystemPort(ABC):
    @abstractmethod
    async def get_balance(self, account_id: str) -> Optional[AccountBalance]:
        """Retrieves the balance for a given account ID."""
        raise NotImplementedError