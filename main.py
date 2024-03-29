from fastapi import FastAPI

from router import router
from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print("База создана")
    yield
    print("Выключение приложения")


app = FastAPI(lifespan=lifespan)
app.include_router(router)
