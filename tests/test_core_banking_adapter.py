import pytest
from app.infrastructure.adapters.core_banking_adapter import CoreBankingAdapter

@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_balance():
    adapter = CoreBankingAdapter()
    balance = await adapter.get_balance("account_id")
    assert balance is not None