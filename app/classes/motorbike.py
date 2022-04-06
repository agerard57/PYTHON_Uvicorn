from .vehicles import Vehicles


class Motorbike(Vehicles):
    def __init__(self, brand, model, color, avgSpeed, year, nbWheels):
        super().__init__(brand, model, color, avgSpeed, year)
        self.nbWheels = nbWheels
