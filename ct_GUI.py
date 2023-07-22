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

        # Creating the search bar
        here = Label(self, text = "Search here...")
        here.place(x = 50, y = 20)
        self.bar = ct.Entry(self, width = 65)
        self.bar.place(x = 50, y = 40)

        # Ask for necessary entry like name, age, email, contact number, and the vaccination status
        name = Label(self, text = "Name: ")
        name.place(x = 50, y = 80)
        self.e1 = ct.Entry(self, width = 50)
        self.e1.place(x = 50, y = 110)
        
        age = Label(self, text = "Age: ")
        age.place(x = 400, y = 80)
        self.e2 = ct.Entry(self, width = 25)
        self.e2.place(x = 400, y = 110)
        
        email = Label(self, text = "Email: ")
        email.place(x = 50, y = 150)
        self.e3 = ct.Entry(self, width = 50)
        self.e3.place(x = 50, y = 180)
        
        number = Label(self, text = "Contact number: ")
        number.place(x = 400, y = 150)
        self.e4 = ct.Entry(self, width = 25)
        self.e4.place(x = 400, y = 180)
        
        health = Label(self, text = "About health:")
        health.place(x = 50, y = 220)

        self.rad = StringVar()

        vac = Label(self, text = "Have you been vaccinated?")
        vac.place(x = 50, y = 250)
        self.vac1 = ct.Radiobutton(self, text = "Yes, first dose", value = "Vaccinated once", variable = self.rad, command = self.sub, indicatoron = 0)
        self.vac1.place(x = 60, y = 280)
        self.vac2 = ct.Radiobutton(self, text = "Yes, second dose", value = "Fully vaccinated", variable= self.rad, command = self.sub, indicatoron = 0)
        self.vac2.place(x = 60, y = 300)
        self.vac3 = ct.Radiobutton(self, text = "Yes, booster", value = "Fully vaccinated", variable= self.rad, command = self.sub, indicatoron = 0)
        self.vac3.place(x = 60, y = 320)
        self.vac4 = ct.Radiobutton(self, text = "Not yet", value = "Not vaccinated", variable= self.rad, command = self.sub, indicatoron = 0)
        self.vac4.place(x = 60, y = 340)

        # Create the submit button
        submitting = Button(self, text = "Submit", command = self.sub)
        submitting.place(x = 285, y = 350)

    # Create function for the submit button
    def sub(self):
        data = ([self.e1.get(),  self.e2.get(), self.e3.get(), self.e4.get(), self.rad.get()])
        with open("ct_file.csv", "a") as myFile:
            write_this = csv.writer(myFile)
            write_this.writerow(data)

        # Create the function to delete the inputs after being submitted
        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')

# Create add button

# Create search button
