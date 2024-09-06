class vehicle:
    def __init__(self, license_plate,vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type


class Car(vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate,"Car")

class Motorcycle(vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Motorcycle")

class Truck(vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Truck")
        