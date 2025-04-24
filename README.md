# FinalProjectS2

# 🚗 Parking Lot Manager

A simple Python-based terminal Parking Lot Management System.

## Features

- Efficient slot assignment (first available)
- Entry and exit time tracking
- Charge calculation ($2/hour, max $10/day)
- JSON-based persistent storage
- Terminal-based interface
- Auto-loads previous state on startup

## Requirements

- Python 3.x

## Usage

```bash
make run
```
## Options Available:

    Park a vehicle (assigns to lowest available slot)

    Exit a vehicle (calculates charge)

    Show current slot statuses

    Exit and auto-save current state

## Clear saved parking data and cache:

```bash
make clean
```

## File Structure

```bash
├── main.py                # Entry point
├── ParkingLotManager.py  # Core logic
├── parking_data.json     # Stored vehicle data (auto-generated)
├── Makefile              # Run and clean commands
└── README.md             # You're reading it!
```

## Example Charges

    1 hour = $2

    3.5 hours = $8

    8 hours = $10 (daily cap)

## Notes

    Data is saved in parking_data.json on exit and auto-loaded next time you run the app.
