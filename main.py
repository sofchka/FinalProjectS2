from ParkingLotManager import ParkingLot

def main():
    lot = ParkingLot.load_state()
    while True:
        print("\n1. Park Vehicle\n2. Exit Vehicle\n3. Show Slots\n4. Exit")
        choice = input("Enter option: ")

        if choice == '1':
            plate = input("Enter vehicle plate number: ")
            lot.park_vehicle(plate)
        elif choice == '2':
            plate = input("Enter vehicle plate number: ")
            lot.exit_vehicle(plate)
        elif choice == '3':
            lot.display_slots()
        elif choice == '4':
            lot.save_state()
            print("State saved. Exiting...")
            break

if __name__ == "__main__":
    main()