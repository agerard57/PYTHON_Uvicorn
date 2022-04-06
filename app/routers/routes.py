from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from data.vehicles import Vehicles

app = FastAPI()
router = APIRouter()


@router.get("/")
async def api_test():
    return {"message": "API has started"}


@router.get("/vehicles")
async def get_all_cars():
    return Vehicles


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse({"error": "this page is not available"})
