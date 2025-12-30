import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as router_tasks
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_tasks)


origins = [
    "http://localhost:5173",  # Vite
    "http://127.0.0.1:5173",
    "https://your-frontend-domain.com",  # якщо буде прод
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # або ["*"] для тестів
    allow_credentials=True,
    allow_methods=["*"],          # GET, POST, PUT, DELETE
    allow_headers=["*"],          # Authorization, Content-Type
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)