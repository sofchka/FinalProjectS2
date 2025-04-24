# Makefile for Parking Lot Manager Project

run:
	python3 main.py

clean:
	rm -f parking_data.json
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.pyc' -delete

