import json
from datetime import datetime

class Vehicle:
    def __init__(self, plate_number, slot_id):
        self.plate_number = plate_number
        self.slot_id = slot_id
        self.entry_time = datetime.now()

class Transaction:
    def __init__(self, vehicle, exit_time):
        self.vehicle = vehicle
        self.exit_time = exit_time
        self.duration = self.exit_time - vehicle.entry_time
        self.charge = self.calculate_charge()

    def calculate_charge(self):
        hours = self.duration.total_seconds() / 3600
        hours = int(hours) + 1
        daily_max = 10
        hourly_rate = 2
        cost = min(daily_max, hours * hourly_rate)
        return cost

class ParkingLot:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.slots = {i: None for i in range(1, total_slots + 1)}

    def find_available_slot(self):
        for slot_id, vehicle in self.slots.items():
            if vehicle is None:
                return slot_id
        return None

    def park_vehicle(self, plate_number):
        slot_id = self.find_available_slot()
        if slot_id is None:
            print("Parking Full!")
            return
        vehicle = Vehicle(plate_number, slot_id)
        self.slots[slot_id] = vehicle
        print(f"Vehicle {plate_number} parked at slot {slot_id} at {vehicle.entry_time}")

    def exit_vehicle(self, plate_number):
        for slot_id, vehicle in self.slots.items():
            if vehicle and vehicle.plate_number == plate_number:
                transaction = Transaction(vehicle, datetime.now())
                print(f"Vehicle {plate_number} exited. Duration: {transaction.duration}. Charge: ${transaction.charge}")
                self.slots[slot_id] = None
                return
        print("Vehicle not found.")

    def display_slots(self):
        for slot, vehicle in self.slots.items():
            status = vehicle.plate_number if vehicle else "Empty"
            print(f"Slot {slot}: {status}")

    def save_state(self, filename="parking_data.json"):
        data = {
            "slots": {
                str(slot): {
                    "plate_number": v.plate_number,
                    "entry_time": v.entry_time.isoformat()
                } if v else None
                for slot, v in self.slots.items()
            }
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod     #Python decorator that defines a method inside a class that doesn’t use self/cls (without an instance)
    def load_state(filename="parking_data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return ParkingLot(10)
        lot = ParkingLot(len(data["slots"]))
        for slot, v in data["slots"].items():
            if v:
                vehicle = Vehicle(v["plate_number"], int(slot))
                vehicle.entry_time = datetime.fromisoformat(v["entry_time"])
                lot.slots[int(slot)] = vehicle
        return lot