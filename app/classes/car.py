from .vehicles import Vehicles


class Car(Vehicles):
    def __init__(self, brand, model, color, avgSpeed, year, nbDoors):
        super().__init__(brand, model, color, avgSpeed, year)
        self.nbDoors = nbDoors
