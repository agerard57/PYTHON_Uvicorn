from fastapi import APIRouter

from data.vehicles import Vehicles


router = APIRouter()


@router.get("/count/{vType}")
async def count_item(vType: str):
    if vType not in ["car", "boat", "plane", "motorbike"]:
        return {"message": "The submitted type doesn't exist"}

    def count_occurrences():
        return str(Vehicles).count(vType)

    return "There are " + str(count_occurrences()) + " occurrences of " + vType
