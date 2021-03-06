import logging

from fastapi import FastAPI

from app.api import ping, empresas, estabelecimentos
from app.db import init_db


log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(empresas.router, prefix="/empresas", tags=["empresas"])
    application.include_router(estabelecimentos.router, prefix="/estabelecimentos", tags=["estabelecimentos"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")