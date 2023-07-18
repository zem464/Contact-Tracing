# Import Tkinter
import tkinter
from tkinter import *

# Assign the objects of Tkinter
ct = tkinter.Tk()
# Adding the title and size of the GUI
ct.title("Contact Tracing")
ct.geometry("600x400")

# Ask for necessary entry like name, age, email, contact number, and the vaccination status

name = Label(ct, text = "Name: ")
name.place(x = 50, y = 50)
e1 = Entry(ct, width = 50)
e1.place(x = 50, y = 80)

age = Label(ct, text = "Age: ")
age.place(x = 400, y = 50)
e2 = Entry(ct, width = 25)
e2.place(x = 400, y = 80)

email = Label(ct, text = "Email: ")
email.place(x = 50, y = 120)
e3 = Entry(ct, width = 50)
e3.place(x = 50, y = 150)

number = Label(ct, text = "Contact number: ")
number.place(x = 400, y = 120)
e4 = Entry(ct, width = 25)
e4.place(x = 400, y = 150)

health = Label(ct, text = "About health:")
health.place(x = 50, y = 200)

vac = Label(ct, text = "Have you been vaccinated?")
vac.place(x = 50, y = 225)
vac1 = Checkbutton(ct, text = "Yes, first dose")
vac1.place(x = 60, y = 250)
vac2 = Checkbutton(ct, text = "Yes, second dose")
vac2.place(x = 60, y = 275)
vac3 = Checkbutton(ct, text = "Yes, booster")
vac3.place(x = 60, y = 300)
vac4 = Checkbutton(ct, text = "Not yet")
vac4.place(x = 60, y = 325)

# Create the submit button
submitting = Button(ct, text = "Submit")
submitting.place(x = 280, y = 235)

# Create the add button

# Create the search button

# Close the program