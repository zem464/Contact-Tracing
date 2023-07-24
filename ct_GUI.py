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

        # Frames
        search_frame = ct.Frame(self, width = "860", height = "75", bg = "#EEEEC9")
        search_frame.place(x = 20, y = 95)

        info_frame = ct.Frame(self, width = "860", height = "450", bg = "#EEEEC9")
        info_frame.place(x = 20, y = 175)

        # Creating the search bar
        here = Label(self, text = "Search here...", bg = "#EEEEC9", fg = "#48483D", font = ("Century Schoolbook", 11, "bold"))
        here.place(x = 50, y = 110)
        self.bar = ct.Entry(self, width = 90, font = font3)
        self.bar.place(x = 50, y = 135)

        # Create the search button
        search = ct.Button(self, text = "Search", command = self.search, fg = "#48483D", font = ("Times New Roman", 10, "normal"))
        search.place(x = 800, y = 132)

        # Ask for necessary entry like name, age, email, contact number, and the vaccination status
        intro = Label(self, text = "INFORMATION", bg = "#EEEEC9", fg = "#48483D", font = font1)
        intro.place(x = 50, y = 200)

        name = Label(self, text = "Name: ", bg = "#EEEEC9", fg = "#48483D", font = font2)
        name.place(x = 50, y = 250)
        self.e1 = ct.Entry(self, width = 65, font = font3)
        self.e1.place(x = 50, y = 280)
        
        age = Label(self, text = "Age: ", bg = "#EEEEC9", fg = "#48483D", font = font2)
        age.place(x = 610, y = 250)
        self.e2 = ct.Entry(self, width = 25, font = font3)
        self.e2.place(x = 610, y = 280)
        
        email = Label(self, text = "Email: ", bg = "#EEEEC9", fg = "#48483D", font = font2)
        email.place(x = 50, y = 320)
        self.e3 = ct.Entry(self, width = 65, font = font3)
        self.e3.place(x = 50, y = 350)
        
        number = Label(self, text = "Contact number: ", bg = "#EEEEC9", fg = "#48483D", font = font2)
        number.place(x = 610, y = 320)
        self.e4 = ct.Entry(self, width = 25, font = font3)
        self.e4.place(x = 610, y = 350)
        
        health = Label(self, text = "ABOUT HEALTH", bg = "#EEEEC9", fg = "#48483D", font = font1)
        health.place(x = 50, y = 400)

        self.rad = StringVar()

        vac = Label(self, text = "Have you been vaccinated?", bg = "#EEEEC9", fg = "#48483D", font = font2)
        vac.place(x = 50, y = 450)
        self.vac1 = ct.Radiobutton(self, text = "Yes, first dose", value = "Partially vaccinated", variable = self.rad, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.vac1.place(x = 70, y = 480)
        self.vac2 = ct.Radiobutton(self, text = "Yes, second dose", value = "Fully vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.vac2.place(x = 175, y = 480)
        self.vac3 = ct.Radiobutton(self, text = "Yes, booster", value = "Vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.vac3.place(x = 300, y = 480)
        self.vac4 = ct.Radiobutton(self, text = "Not yet", value = "Not vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.vac4.place(x = 400, y = 480)

        self.exp = StringVar()

        exp = Label(self, text = "In the last 14 days, were you exposed to someone that tested positive in COVID-19?", bg = "#EEEEC9", fg = "#48483D", font = font2)
        exp.place(x = 50, y = 530)
        self.exp1 = ct.Radiobutton(self, text = "Yes", value = "Exposed", variable = self.exp, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.exp1.place(x = 70, y = 560)
        self.exp2 = ct.Radiobutton(self, text = "No", value = "Not Exposed", variable = self.exp, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.exp2.place(x = 105, y = 560)
        self.exp3 = ct.Radiobutton(self, text = "Not Sure", value = "Not Certain", variable = self.exp, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.exp3.place(x = 140, y = 560)

        # Create the submit button
        submitting = Button(self, text = "Submit", command = self.sub, fg = "#48483D", font = font4)
        submitting.place(x = 430, y = 650)

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
        
        # Instance to look for the searched item
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

                    title = ct.Label(info, text = " ABOUT ", bg = "#8B8B75", fg = "#EEEEC9", font = font5)
                    title.place(x = 115, y = 20)
                    
                    # Strings instance
                    col1 = str(entry[x][0])
                    col2 = str(entry[x][1])
                    col3 = str(entry[x][2])
                    col4 = str(entry[x][3])
                    col5 = str(entry[x][4])
                    col6 = str(entry[x][5])

                    # Toplevel window: informations
                    name_info = ct.Label(info, text = "Name: ", bg = "#CDCDAD", font = font6)
                    name_info.place(x = 25, y = 60)

                    name_col1 = ct.Label(info, text = col1, bg = "#CDCDAD", font = font7)
                    name_col1.place(x = 90, y = 60)
                    
                    age_info = ct.Label(info, text = "Age: ", bg = "#CDCDAD", font = font6)
                    age_info.place(x = 25, y = 85)
                    age_col2 = ct.Label(info, text = col2, bg = "#CDCDAD", font = font7)
                    age_col2.place(x = 90, y = 85)
                    
                    email_info = ct.Label(info, text = "Email: ", bg = "#CDCDAD", font = font6)
                    email_info.place(x = 25, y = 110)

                    email_col3 = ct.Label(info, text = col3, bg = "#CDCDAD", font = font7)
                    email_col3.place(x = 90, y = 110)
                    
                    number_info = ct.Label(info, text = "Contact No.: ", bg = "#CDCDAD", font = font6)
                    number_info.place(x = 25, y = 135)

                    number_col4 = ct.Label(info, text = col4, bg = "#CDCDAD", font = font7)
                    number_col4.place(x = 120, y = 135)

                    vac_info = ct.Label(info, text = "Vaccination Status: ", bg = "#CDCDAD", font = font6)
                    vac_info.place(x = 25, y = 160)

                    vac_col5 = ct.Label(info, text = col5, bg = "#CDCDAD", font = font7)
                    vac_col5.place(x = 160, y = 160)

                    exp_info = ct.Label(info, text = "Exposure: ", bg = "#CDCDAD", font = font6)
                    exp_info.place(x = 25, y = 185)

                    exp_col6 = ct.Label(info, text = col6, bg = "#CDCDAD", font = font7)
                    exp_col6.place(x = 110, y = 185)
        
        # If entry is not in the list of inputs
        else:
            messagebox.showerror("Not Found", "What you're looking for is not in the system")