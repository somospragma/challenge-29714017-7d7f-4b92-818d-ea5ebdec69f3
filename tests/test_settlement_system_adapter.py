import pytest
from app.infrastructure.adapters.settlement_system_adapter import SettlementSystemAdapter

@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_balance():
    adapter = SettlementSystemAdapter()
    balance = await adapter.get_balance("account_id")
    assert balance is not None