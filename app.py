from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from auth.router import router as auth_router
from maps.router import router as maps_router
from auth.middleware import auth_middleware

app = FastAPI(
    routes=[
        auth_router,
        maps_router
    ],
    middleware= [
        auth_middleware
    ]
)

app.mount("/static", StaticFiles(directory="static"), name="static")
