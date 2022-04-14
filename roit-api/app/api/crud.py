from datetime import datetime
from typing import List, Union

# from app.models.pydantic import EmpresaPayloadSchema
from app.models.tortoise import Empresa, Estabelecimento


async def get_empresas(created_at: str) -> Union[List, None]:
    empresa = await Empresa.filter(created_at=created_at).all().values()
    if empresa:
        return empresa
    return None


async def get_estabelecimentos(created_at: str) -> Union[List, None]:
    estabelecimento = await Estabelecimento.filter(created_at=created_at).all().values()
    if estabelecimento:
        return estabelecimento
    return None