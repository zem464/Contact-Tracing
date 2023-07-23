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
        self.geometry("900x700")
        self.configure(bg = "#8B8B73")

        # Fonts
        font1 = ("Century Schoolbook", 14, "bold")
        font2 = ("Times New Roman", 13, "normal")
        font3 = ("Times New Roman", 12, "normal")
        font4 = ("Times New Roman", 11, "normal")

        search_frame = ct.Frame(self, width = "860", height = "75", bg = "#EEEEC9")
        search_frame.place(x = 20, y = 95)

        info_frame = ct.Frame(self, width = "860", height = "450", bg = "#EEEEC9")
        info_frame.place(x = 20, y = 175)

        # Creating the search bar
        here = Label(self, text = "Search here...", bg = "#EEEEC9")
        here.place(x = 50, y = 110)
        here.configure(font = ("Century Schoolbook", 11, "bold"))
        self.bar = ct.Entry(self, width = 90)
        self.bar.place(x = 50, y = 135)
        self.bar.configure(font = font3)

        # Create the search button
        search = ct.Button(self, text = "Search", command = self.search)
        search.place(x = 800, y = 132)
        search.configure(font = ("Times New Roman", 10, "normal"))

        # Ask for necessary entry like name, age, email, contact number, and the vaccination status
        intro = Label(self, text = "INFORMATION", bg = "#EEEEC9")
        intro.place(x = 50, y = 200)
        intro.configure(font = font1)

        name = Label(self, text = "Name: ", bg = "#EEEEC9")
        name.place(x = 50, y = 250)
        name.configure(font = font2)
        self.e1 = ct.Entry(self, width = 65)
        self.e1.place(x = 50, y = 280)
        self.e1.configure(font = font3)
        
        age = Label(self, text = "Age: ", bg = "#EEEEC9")
        age.place(x = 610, y = 250)
        age.configure(font = font2)
        self.e2 = ct.Entry(self, width = 25)
        self.e2.place(x = 610, y = 280)
        self.e2.configure(font = font3)
        
        email = Label(self, text = "Email: ", bg = "#EEEEC9")
        email.place(x = 50, y = 320)
        email.configure(font = font2)
        self.e3 = ct.Entry(self, width = 65)
        self.e3.place(x = 50, y = 350)
        self.e3.configure(font = font3)
        
        number = Label(self, text = "Contact number: ", bg = "#EEEEC9")
        number.place(x = 610, y = 320)
        number.configure(font = font2)
        self.e4 = ct.Entry(self, width = 25)
        self.e4.place(x = 610, y = 350)
        self.e4.configure(font = font3)
        
        health = Label(self, text = "ABOUT HEALTH", bg = "#EEEEC9")
        health.place(x = 50, y = 400)
        health.configure(font = font1)

        self.rad = StringVar()

        vac = Label(self, text = "Have you been vaccinated?", bg = "#EEEEC9")
        vac.place(x = 50, y = 450)
        vac.configure(font = font2)
        self.vac1 = ct.Radiobutton(self, text = "Yes, first dose", value = "Partially vaccinated", variable = self.rad, indicatoron = 0, bg = "#EEEEC9")
        self.vac1.place(x = 70, y = 480)
        self.vac1.configure(font = font3)
        self.vac2 = ct.Radiobutton(self, text = "Yes, second dose", value = "Fully vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9")
        self.vac2.place(x = 175, y = 480)
        self.vac2.configure(font = font3)
        self.vac3 = ct.Radiobutton(self, text = "Yes, booster", value = "Vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9")
        self.vac3.place(x = 300, y = 480)
        self.vac3.configure(font = font3)
        self.vac4 = ct.Radiobutton(self, text = "Not yet", value = "Not vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9")
        self.vac4.place(x = 400, y = 480)
        self.vac4.configure(font = font3)

        self.exp = StringVar()

        exp = Label(self, text = "In the last 14 days, were you exposed to someone that tested positive in COVID-19?", bg = "#EEEEC9")
        exp.place(x = 50, y = 530)
        exp.configure(font = font2)
        self.exp1 = ct.Radiobutton(self, text = "Yes", value = "Exposed", variable = self.exp, indicatoron = 0, bg = "#EEEEC9")
        self.exp1.place(x = 70, y = 560)
        self.exp1.configure(font = font3)
        self.exp2 = ct.Radiobutton(self, text = "No", value = "Not Exposed", variable = self.exp, indicatoron = 0, bg = "#EEEEC9")
        self.exp2.place(x = 105, y = 560)
        self.exp2.configure(font = font3)
        self.exp3 = ct.Radiobutton(self, text = "Not Sure", value = "Not Certain", variable = self.exp, indicatoron = 0, bg = "#EEEEC9")
        self.exp3.place(x = 140, y = 560)
        self.exp3.configure(font = font3)

        # Create the submit button
        submitting = Button(self, text = "Submit", command = self.sub)
        submitting.place(x = 430, y = 650)
        submitting.configure(font = font4)

    # Create function for the submit button
    def sub(self):
        data = ([self.e1.get().title(),  self.e2.get(), self.e3.get(), self.e4.get(), self.rad.get(), self.exp.get()])
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
        name = self.bar.get().title()
        entry = []
        with open("ct_file.csv", "r") as myFile2:
            read_this = csv.reader(myFile2)
            for row in read_this:
                    entry.append(row)
        
        look = [x[0] for x in entry]
    
        if name in look:
            for x in range(0, len(entry)):
                if name == entry[x][0]:
                    info = ct.Toplevel(self)
                    info.title("Information")
                    info.geometry("300x225")
                    info.configure(bg = "#8B8B75")

                    font4 = ("MS Sans Serif", 10, "bold")
                    font5 = ("MS Sans Serif", 9, "normal")

                    frame_about = ct.Frame(info, width = 250, height = 200, bg = "#CDCDAD")
                    frame_about.place(x = 25, y = 10)

                    title = ct.Label(info, text = " ABOUT ")
                    title.place(x = 120, y = 20)
                    title.configure(font = font4)
                    
                    name_info = ct.Label(info, text = "Name: " + str(entry[x][0]), bg = "#CDCDAD")
                    name_info.place(x = 45, y = 55)
                    name_info.configure(font = font5)
                    
                    age_info = ct.Label(info, text = "Age: " + str(entry[x][1]), bg = "#CDCDAD")
                    age_info.place(x = 45, y = 80)
                    age_info.configure(font = font5)
                    
                    email_info = ct.Label(info, text = "Email: " + str(entry[x][2]), bg = "#CDCDAD")
                    email_info.place(x = 45, y = 105)
                    email_info.configure(font = font5)
                    
                    number_info = ct.Label(info, text = "Contact Number: " + str(entry[x][3]), bg = "#CDCDAD")
                    number_info.place(x = 45, y = 130)
                    number_info.configure(font = font5)

                    vac_info = ct.Label(info, text = "Vaccination Status: " + str(entry[x][4]), bg = "#CDCDAD")
                    vac_info.place(x = 45, y = 155)
                    vac_info.configure(font = font5)

                    exp_info = ct.Label(info, text = "Exposure: " + str(entry[x][5]), bg = "#CDCDAD")
                    exp_info.place(x = 45, y = 180)
                    exp_info.configure(font = font5)

        else:
            messagebox.showerror("Not Found", "What you're looking for is not in the system")