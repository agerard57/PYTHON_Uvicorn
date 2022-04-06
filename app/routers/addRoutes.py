from data.vehicles import Vehicles
from fastapi import APIRouter, Form
from app.classes.boat import Boat
from app.classes.car import Car
from app.classes.motorbike import Motorbike
from app.classes.plane import Plane

router = APIRouter()


@router.post("/add/car")
async def add_car(
    brand: str = Form(...),
    model: str = Form(...),
    avgSpeed: float = Form(...),
    color: str = Form(...),
    year: int = Form(...),
    nbDoors: int = Form(...),
):
    objects = Car(brand, model, avgSpeed, color, year, nbDoors)
    Vehicles.append(objects)
    return {"message": "Successfully added"}


@router.post("/add/plane")
async def add_plane(
    brand: str = Form(...),
    model: str = Form(...),
    avgSpeed: float = Form(...),
    color: str = Form(...),
    year: int = Form(...),
    tankCapacity: float = Form(...),
):
    objects = Plane(brand, model, avgSpeed, color, year, tankCapacity)
    Vehicles.append(objects)
    return {"message": "Successfully added"}


@router.post("/add/boat")
async def add_boat(
    brand: str = Form(...),
    model: str = Form(...),
    avgSpeed: float = Form(...),
    color: str = Form(...),
    year: int = Form(...),
    nbPortHole: int = Form(...),
):
    objects = Boat(brand, model, avgSpeed, color, year, nbPortHole)
    Vehicles.append(objects)
    return {"message": "Successfully added"}


@router.post("/add/motorbike")
async def add_motorbike(
    brand: str = Form(...),
    model: str = Form(...),
    avgSpeed: float = Form(...),
    color: str = Form(...),
    year: int = Form(...),
    nbWheels: int = Form(...),
):
    objects = Motorbike(brand, model, avgSpeed, color, year, nbWheels)
    Vehicles.append(objects)
    return {"message": "Successfully added"}
