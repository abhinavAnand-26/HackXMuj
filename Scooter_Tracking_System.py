class Scooter:
    def __init__(self, manufacturer, current_location, status):
        self.manufacturer = manufacturer
        self.current_location = current_location
        self.status = status  # 0: Manufacturer, 1: Bikesetu Yard, 2: Franchise Store, 3: End Customer

class ScooterManagement:
    MAX_SCOOTERS = 100
    LOCATIONS = ["Manufacturer", "Bikesetu Yard", "Franchise Store", "End Customer"]

    def __init__(self):
        self.scooters = [Scooter("Manufacturer", "Manufacturer", 0) for _ in range(self.MAX_SCOOTERS)]

    def update_scooter_status(self, scooter_id, new_status):
        if 0 <= scooter_id < self.MAX_SCOOTERS and 0 <= new_status < len(self.LOCATIONS):
            scooter = self.scooters[scooter_id]
            scooter.status = new_status
            scooter.current_location = self.LOCATIONS[new_status]
        else:
            print("Invalid scooter_id or new_status")

    def print_scooter_status(self, scooter_id):
        if 0 <= scooter_id < self.MAX_SCOOTERS:
            scooter = self.scooters[scooter_id]
            print(f"Scooter {scooter_id} is currently at: {scooter.current_location}")
        else:
            print("Invalid scooter_id")

if __name__ == "__main__":
    management = ScooterManagement()

    # Simulate scooter journeys
    management.update_scooter_status(0, 1)  # Scooter 0 goes to Bikesetu Yard
    management.update_scooter_status(0, 2)  # Scooter 0 goes to Franchise Store
    management.update_scooter_status(0, 3)  # Scooter 0 is sold to End Customer

    # Print scooter status
    management.print_scooter_status(0)
