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

        # Title
        title = ct.Label(self, text = "CONTACT TRACING", bg = "#8B8B73")
        title.place(x = 200, y = 20)
        title.configure(font = ("Century Schoolbook", 35, "bold"), fg = "#EEEEC9")

        # Fonts
        font1 = ("Century Schoolbook", 14, "bold")
        font2 = ("Times New Roman", 13, "bold")
        font3 = ("Times New Roman", 12, "normal")
        font4 = ("Times New Roman", 11, "normal")

        search_frame = ct.Frame(self, width = "860", height = "75", bg = "#EEEEC9")
        search_frame.place(x = 20, y = 95)

        info_frame = ct.Frame(self, width = "860", height = "450", bg = "#EEEEC9")
        info_frame.place(x = 20, y = 175)

        # Creating the search bar
        here = Label(self, text = "Search here...", bg = "#EEEEC9", fg = "#48483D")
        here.place(x = 50, y = 110)
        here.configure(font = ("Century Schoolbook", 11, "bold"))
        self.bar = ct.Entry(self, width = 90)
        self.bar.place(x = 50, y = 135)
        self.bar.configure(font = font3)

        # Create the search button
        search = ct.Button(self, text = "Search", command = self.search, fg = "#48483D")
        search.place(x = 800, y = 132)
        search.configure(font = ("Times New Roman", 10, "normal"))

        # Ask for necessary entry like name, age, email, contact number, and the vaccination status
        intro = Label(self, text = "INFORMATION", bg = "#EEEEC9", fg = "#48483D")
        intro.place(x = 50, y = 200)
        intro.configure(font = font1)

        name = Label(self, text = "Name: ", bg = "#EEEEC9", fg = "#48483D")
        name.place(x = 50, y = 250)
        name.configure(font = font2)
        self.e1 = ct.Entry(self, width = 65)
        self.e1.place(x = 50, y = 280)
        self.e1.configure(font = font3)
        
        age = Label(self, text = "Age: ", bg = "#EEEEC9", fg = "#48483D")
        age.place(x = 610, y = 250)
        age.configure(font = font2)
        self.e2 = ct.Entry(self, width = 25)
        self.e2.place(x = 610, y = 280)
        self.e2.configure(font = font3)
        
        email = Label(self, text = "Email: ", bg = "#EEEEC9", fg = "#48483D")
        email.place(x = 50, y = 320)
        email.configure(font = font2)
        self.e3 = ct.Entry(self, width = 65)
        self.e3.place(x = 50, y = 350)
        self.e3.configure(font = font3)
        
        number = Label(self, text = "Contact number: ", bg = "#EEEEC9", fg = "#48483D")
        number.place(x = 610, y = 320)
        number.configure(font = font2)
        self.e4 = ct.Entry(self, width = 25)
        self.e4.place(x = 610, y = 350)
        self.e4.configure(font = font3)
        
        health = Label(self, text = "ABOUT HEALTH", bg = "#EEEEC9", fg = "#48483D")
        health.place(x = 50, y = 400)
        health.configure(font = font1)

        self.rad = StringVar()

        vac = Label(self, text = "Have you been vaccinated?", bg = "#EEEEC9", fg = "#48483D")
        vac.place(x = 50, y = 450)
        vac.configure(font = font2)
        self.vac1 = ct.Radiobutton(self, text = "Yes, first dose", value = "Partially vaccinated", variable = self.rad, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D")
        self.vac1.place(x = 70, y = 480)
        self.vac1.configure(font = font3)
        self.vac2 = ct.Radiobutton(self, text = "Yes, second dose", value = "Fully vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D")
        self.vac2.place(x = 175, y = 480)
        self.vac2.configure(font = font3)
        self.vac3 = ct.Radiobutton(self, text = "Yes, booster", value = "Vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D")
        self.vac3.place(x = 300, y = 480)
        self.vac3.configure(font = font3)
        self.vac4 = ct.Radiobutton(self, text = "Not yet", value = "Not vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D")
        self.vac4.place(x = 400, y = 480)
        self.vac4.configure(font = font3)

        self.exp = StringVar()

        exp = Label(self, text = "In the last 14 days, were you exposed to someone that tested positive in COVID-19?", bg = "#EEEEC9", fg = "#48483D")
        exp.place(x = 50, y = 530)
        exp.configure(font = font2)
        self.exp1 = ct.Radiobutton(self, text = "Yes", value = "Exposed", variable = self.exp, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D")
        self.exp1.place(x = 70, y = 560)
        self.exp1.configure(font = font3)
        self.exp2 = ct.Radiobutton(self, text = "No", value = "Not Exposed", variable = self.exp, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D")
        self.exp2.place(x = 105, y = 560)
        self.exp2.configure(font = font3)
        self.exp3 = ct.Radiobutton(self, text = "Not Sure", value = "Not Certain", variable = self.exp, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D")
        self.exp3.place(x = 140, y = 560)
        self.exp3.configure(font = font3)

        # Create the submit button
        submitting = Button(self, text = "Submit", command = self.sub, fg = "#48483D")
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

        # If search entry is in the list of inputs
        if name in look:
            for x in range(0, len(entry)):
                if name == entry[x][0]:
                    # Open a toplevel window
                    info = ct.Toplevel(self)
                    info.title("Information")
                    info.geometry("300x225")
                    info.configure(bg = "#8B8B75")

                    # Toplevel window: fonts
                    font5 = ("Century Schoolbook", 12, "bold")
                    font6 = ("MS Sans Serif", 10, "bold")
                    font7 = ("MS Sans Serif", 10, "normal")

                    # Toplevel window: frame and title
                    frame_about = ct.Frame(info, width = 265, height = 155, bg = "#CDCDAD")
                    frame_about.place(x = 20, y = 55)

                    title = ct.Label(info, text = " ABOUT ", bg = "#8B8B75", fg = "#EEEEC9")
                    title.place(x = 115, y = 20)
                    title.configure(font = font5)
                    
                    # Strings instance
                    col1 = str(entry[x][0])
                    col2 = str(entry[x][1])
                    col3 = str(entry[x][2])
                    col4 = str(entry[x][3])
                    col5 = str(entry[x][4])
                    col6 = str(entry[x][5])

                    # Toplevel window: informations
                    name_info = ct.Label(info, text = "Name: ", bg = "#CDCDAD")
                    name_info.place(x = 25, y = 60)
                    name_info.configure(font = font6)

                    name_col1 = ct.Label(info, text = col1, bg = "#CDCDAD")
                    name_col1.place(x = 90, y = 60)
                    name_col1.configure(font = font7)
                    
                    age_info = ct.Label(info, text = "Age: ", bg = "#CDCDAD")
                    age_info.place(x = 25, y = 85)
                    age_info.configure(font = font6)

                    age_col2 = ct.Label(info, text = col2, bg = "#CDCDAD")
                    age_col2.place(x = 90, y = 85)
                    age_col2.configure(font = font7)
                    
                    email_info = ct.Label(info, text = "Email: ", bg = "#CDCDAD")
                    email_info.place(x = 25, y = 110)
                    email_info.configure(font = font6)

                    email_col3 = ct.Label(info, text = col3, bg = "#CDCDAD")
                    email_col3.place(x = 90, y = 110)
                    email_col3.configure(font = font7)
                    
                    number_info = ct.Label(info, text = "Contact No.: ", bg = "#CDCDAD")
                    number_info.place(x = 25, y = 135)
                    number_info.configure(font = font6)

                    number_col4 = ct.Label(info, text = col4, bg = "#CDCDAD")
                    number_col4.place(x = 120, y = 135)
                    number_col4.configure(font = font7)

                    vac_info = ct.Label(info, text = "Vaccination Status: ", bg = "#CDCDAD")
                    vac_info.place(x = 25, y = 160)
                    vac_info.configure(font = font6)

                    vac_col5 = ct.Label(info, text = col5, bg = "#CDCDAD")
                    vac_col5.place(x = 160, y = 160)
                    vac_col5.configure(font = font7)

                    exp_info = ct.Label(info, text = "Exposure: ", bg = "#CDCDAD")
                    exp_info.place(x = 25, y = 185)
                    exp_info.configure(font = font6)

                    exp_col6 = ct.Label(info, text = col6, bg = "#CDCDAD")
                    exp_col6.place(x = 110, y = 185)
                    exp_col6.configure(font = font7)

        # If entry is not in the list of inputs
        else:
            messagebox.showerror("Not Found", "What you're looking for is not in the system")