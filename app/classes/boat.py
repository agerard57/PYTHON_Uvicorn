from .vehicles import Vehicles


class Boat(Vehicles):
    def __init__(self, brand, model, color, avgSpeed, year, nbPortHole):
        super().__init__(brand, model, color, avgSpeed, year)
        self.nbPortHole = nbPortHole
