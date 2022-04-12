from datetime import datetime
from typing import List, Union

# from app.models.pydantic import EmpresaPayloadSchema
from app.models.tortoise import Empresa


async def get(created_at: str) -> Union[List, None]:
    empresa = await Empresa.filter(created_at=created_at).all().values()
    if empresa:
        return empresa
    return None