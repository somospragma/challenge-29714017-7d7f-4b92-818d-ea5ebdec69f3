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