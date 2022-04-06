from fastapi import FastAPI

app = FastAPI()

from app.routers import routes
from app.routers import addRoutes
from app.routers import countRoutes

app.include_router(routes.router)
app.include_router(addRoutes.router)
app.include_router(countRoutes.router)
