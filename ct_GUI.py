# Import Tkinter
import tkinter as ct
from tkinter import *
import csv

# Organize the functions in the gui using a class
class contact_tracingGUI(ct.Tk):
    def __init__(self):
        super().__init__()
        # Adding the title and size of the GUI
        self.title("Contact Tracing")
        self.geometry("600x400")

        # Ask for necessary entry like name, age, email, contact number, and the vaccination status
        name = Label(self, text = "Name: ")
        name.place(x = 50, y = 50)
        self.e1 = ct.Entry(self, width = 50)
        self.e1.place(x = 50, y = 80)

        age = Label(self, text = "Age: ")
        age.place(x = 400, y = 50)
        self.e2 = Entry(self, width = 25)
        self.e2.place(x = 400, y = 80)

        email = Label(self, text = "Email: ")
        email.place(x = 50, y = 120)
        self.e3 = Entry(self, width = 50)
        self.e3.place(x = 50, y = 150)

        number = Label(self, text = "Contact number: ")
        number.place(x = 400, y = 120)
        self.e4 = Entry(self, width = 25)
        self.e4.place(x = 400, y = 150)

        health = Label(self, text = "About health:")
        health.place(x = 50, y = 200)

        vac = ct.Label(self, text = "Have you been vaccinated?")
        vac.place(x = 50, y = 225)
        self.vac1 = Checkbutton(self, text = "Yes, first dose")
        self.vac1.place(x = 60, y = 250)
        self.vac2 = Checkbutton(self, text = "Yes, second dose")
        self.vac2.place(x = 60, y = 275)
        self.vac3 = Checkbutton(self, text = "Yes, booster")
        self.vac3.place(x = 60, y = 300)
        self.vac4 = Checkbutton(self, text = "Not yet")
        self.vac4.place(x = 60, y = 325)

        # Create the submit button
        submitting = Button(self, text = "Submit", command = self.sub)
        submitting.place(x = 280, y = 235)

    def sub(self):
        with open("ct_file.csv", "a") as myFile:
            data = ([self.e1.get(),  self.e2.get(), self.e3.get(), self.e4.get()])
            write_this = csv.writer(myFile)
            write_this.writerow(data)

    # Create the add button

    # Create the search button