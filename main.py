from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.api_v1.api import api_router


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)
    # FIXME: remove print statement
    print([str(origin) for origin in settings.BACKEND_CORS_ORIGINS])
    _app.add_middleware(

        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000"
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


# test
app = get_application()

app.include_router(api_router, prefix=settings.API_V1_STR)
