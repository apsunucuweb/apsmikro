from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .database import Base, engine
from .routers import auth as auth_router
from .routers import branches as branches_router


def create_app() -> FastAPI:
	Base.metadata.create_all(bind=engine)
	app = FastAPI(title="APSMİKRO API", version="0.1.0", openapi_url=f"{settings.API_PREFIX}/openapi.json")
	app.add_middleware(
		CORSMiddleware,
		allow_origins=["*"],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)

	api = FastAPI()
	api.include_router(auth_router.router)
	api.include_router(branches_router.router)

	app.mount(settings.API_PREFIX, api)
	return app


app = create_app()
