import pytest
from app.application.use_cases.get_consolidated_balance import GetConsolidatedBalance

@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_consolidated_balance():
    use_case = GetConsolidatedBalance()
    balance = await use_case.execute("account_id")
    assert balance is not None