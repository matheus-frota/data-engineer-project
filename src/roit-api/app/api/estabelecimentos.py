from typing import List

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.tortoise import EstabelecimentoSchema

router = APIRouter()


@router.get("/{created_at}/", response_model=List[EstabelecimentoSchema])
async def read_all_estabelecimentos_by_date(created_at: str) -> List[EstabelecimentoSchema]:
    estabelecimento = await crud.get_estabelecimentos(created_at)
    if not estabelecimento:
        raise HTTPException(status_code=404, detail=f"Estabelecimentos não encontradas para {created_at}")

    return estabelecimento