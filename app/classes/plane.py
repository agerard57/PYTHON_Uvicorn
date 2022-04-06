from .vehicles import Vehicles


class Plane(Vehicles):
    def __init__(self, brand, model, color, avgSpeed, year, tankCapacity):
        super().__init__(brand, model, color, avgSpeed, year)
        self.tankCapacity = tankCapacity
