from typing import List

from fastapi import APIRouter, HTTPException

from app.api import crud
# from app.models.pydantic import EmpresaPayloadSchema, EmpresaResponseSchema
from app.models.tortoise import EmpresaSchema

router = APIRouter()


@router.get("/{created_at}/", response_model=List[EmpresaSchema])
async def read_all_empresas_by_date(created_at: str) -> List[EmpresaSchema]:
    empresa = await crud.get(created_at)
    if not empresa:
        raise HTTPException(status_code=404, detail=f"Empresas não encontradas para {created_at}")

    return empresa