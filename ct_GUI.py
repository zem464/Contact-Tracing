# Import Tkinter
import tkinter as ct
from tkinter import *
from tkinter import messagebox
import csv

# Organize the functions in the gui using a class
class contact_tracingGUI(ct.Tk):
    def __init__(self):
        super().__init__()
        # Adding the title and size of the GUI
        self.title("Contact Tracing")
        self.geometry("600x500")
        self.configure(bg = "#DADAA5")

        search_frame = ct.Frame(self, width = "525", height = "85", bg = "#EEEEC9")
        search_frame.place(x = 35, y = 10)

        info_frame = ct.Frame(self, width = "525", height = "330", bg = "#EEEEC9")
        info_frame.place(x = 35, y = 110)

        # Creating the search bar
        here = Label(self, text = "Search here...")
        here.place(x = 50, y = 25)
        self.bar = ct.Entry(self, width = 65)
        self.bar.place(x = 50, y = 60)

        # Create the search button
        search = ct.Button(self, text = "Search", command = self.search)
        search.place(x = 470, y = 55)

        # Ask for necessary entry like name, age, email, contact number, and the vaccination status
        intro = Label(self, text = "INFORMATION")
        intro.place(x = 50, y = 125)

        name = Label(self, text = "Name: ", bg = "#EEEEC9")
        name.place(x = 50, y = 155)
        self.e1 = ct.Entry(self, width = 50)
        self.e1.place(x = 50, y = 180)
        
        age = Label(self, text = "Age: ", bg = "#EEEEC9")
        age.place(x = 380, y = 155)
        self.e2 = ct.Entry(self, width = 25)
        self.e2.place(x = 380, y = 180)
        
        email = Label(self, text = "Email: ", bg = "#EEEEC9")
        email.place(x = 50, y = 205)
        self.e3 = ct.Entry(self, width = 50)
        self.e3.place(x = 50, y = 230)
        
        number = Label(self, text = "Contact number: ", bg = "#EEEEC9")
        number.place(x = 380, y = 205)
        self.e4 = ct.Entry(self, width = 25)
        self.e4.place(x = 380, y = 230)
        
        health = Label(self, text = "ABOUT HEALTH")
        health.place(x = 50, y = 265)

        self.rad = StringVar()

        vac = Label(self, text = "Have you been vaccinated?", bg = "#EEEEC9")
        vac.place(x = 50, y = 295)
        self.vac1 = ct.Radiobutton(self, text = "Yes, first dose", value = "Partially vaccinated", variable = self.rad, indicatoron = 0, bg = "#EEEEC9")
        self.vac1.place(x = 50, y = 325)
        self.vac2 = ct.Radiobutton(self, text = "Yes, second dose", value = "Fully vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9")
        self.vac2.place(x = 150, y = 325)
        self.vac3 = ct.Radiobutton(self, text = "Yes, booster", value = "Vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9")
        self.vac3.place(x = 275, y = 325)
        self.vac4 = ct.Radiobutton(self, text = "Not yet", value = "Not vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9")
        self.vac4.place(x = 375, y = 325)

        self.exp = StringVar()

        exp = Label(self, text = "In the last 14 days, were you exposed to someone that tested positive in COVID-19?", bg = "#EEEEC9")
        exp.place(x = 50, y = 370)
        self.exp1 = ct.Radiobutton(self, text = "Yes", value = "Exposed", variable = self.exp, indicatoron = 0, bg = "#EEEEC9")
        self.exp1.place(x = 50, y = 400)
        self.exp2 = ct.Radiobutton(self, text = "No", value = "Not Exposed", variable = self.exp, indicatoron = 0, bg = "#EEEEC9")
        self.exp2.place(x = 80, y = 400)
        self.exp3 = ct.Radiobutton(self, text = "Not Sure", value = "Not Certain", variable = self.exp, indicatoron = 0, bg = "#EEEEC9")
        self.exp3.place(x = 110, y = 400)

        # Create the submit button
        submitting = Button(self, text = "Submit", command = self.sub)
        submitting.place(x = 270, y = 460)

    # Create function for the submit button
    def sub(self):
        data = ([self.e1.get(),  self.e2.get(), self.e3.get(), self.e4.get(), self.rad.get()])
        with open("ct_file.csv", "a", newline = "") as myFile:
            write_this = csv.writer(myFile)
            write_this.writerow(data)

        # Create the function to delete the inputs after being submitted
        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        self.rad.set("")
        self.exp.set("")

    # Create search button
    def search(self):
        name = self.e1.get()
        entry = []
        with open("ct_file.csv", "r") as myFile2:
            read_this = csv.reader(myFile2)
            for row in read_this:
                    entry.append(row)