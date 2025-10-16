from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from user.logger.log_config import configure_logging
from user.middlewares.log_middleware import LogMiddleware

configure_logging()



app = FastAPI(
    title='User microservice',
    description=''
)

app.add_middleware(LogMiddleware)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/ping',
        summary="Проверка работоспособности микросервиса",
        description='Этот эндпоинт выполняет простую проверку состояния микросервиса.',
        tags=['Health Check'],
        )
async def ping():
    return 'Server is running'