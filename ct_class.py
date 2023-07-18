# import csv
import csv

# Create class that will be used for the gui
class contact_tracing:
    def __init__(self) -> None:
        pass

    # Create the functions for appending and reading the csv file
    def sub(self, e1, e2, e3, e4):
        with open("program.csv", "a") as myFile:
            data = [e1, e2, e3, e4]
            myFile.write(data)