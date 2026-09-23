from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from app.containers import Container
from app.application.use_cases.get_consolidated_balance import GetConsolidatedBalance
from app.api.schemas.balance_schema import BalanceSchema

router = APIRouter()

@router.get('/balances/consolidated', response_model=BalanceSchema)
@inject
async def get_consolidated_balances(
    use_case: GetConsolidatedBalance = Depends(Provide[Container.get_consolidated_balance])
):
    try:
        result = await use_case.execute()
        return BalanceSchema(**result.__dict__)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))