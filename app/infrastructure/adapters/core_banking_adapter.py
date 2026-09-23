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