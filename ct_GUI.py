# Import Tkinter
import tkinter as ct
from tkinter import *
from tkinter import messagebox
import csv

dev_x = 1920
dev_y = 1080

# Organize the functions in the gui using a class
class contact_tracingGUI(ct.Tk):
    def __init__(self):
        super().__init__()
        # Adding the title and size of the GUI
        self.title("Contact Tracing")
        self.geometry(f"{dev_x}x{dev_y}")
        self.configure(bg = "#8B8B73")

        # Title
        title = ct.Label(self, text = "CONTACT TRACING", bg = "#8B8B73", justify = "center")
        title.configure(font = ("Century Schoolbook", 35, "bold"), fg = "#EEEEC9")
        title.pack(pady=40) # Packed at the top

        # Fonts
        font1 = ("Century Schoolbook", 14, "bold")
        font2 = ("Times New Roman", 13, "bold")
        font3 = ("Times New Roman", 12, "normal")
        font4 = ("Times New Roman", 11, "normal")

        # Frames (Stacked neatly below the title)
        search_frame = ct.Frame(self, width = dev_x - 1000, height = 100, bg = "#EEEEC9")
        search_frame.pack(pady=10)

        info_frame = ct.Frame(self, width = dev_x - 1000, height = 500, bg = "#EEEEC9")
        info_frame.pack(pady=10)

        # ==========================================
        # SEARCH SECTION (Parent is search_frame)
        # ==========================================
        here = Label(search_frame, text = "Search here...", bg = "#EEEEC9", fg = "#48483D", font = ("Century Schoolbook", 11, "bold"))
        here.place(x = 50, y = 15)
        
        self.bar = ct.Entry(search_frame, width = 90, font = font3)
        self.bar.place(x = 50, y = 45)

        # Create the search button
        search = ct.Button(search_frame, text = "Search", command = self.search, fg = "#48483D", font = ("Times New Roman", 10, "normal"))
        search.place(x = 800, y = 42)

        # ==========================================
        # INFORMATION SECTION (Parent is info_frame)
        # ==========================================
        intro = Label(info_frame, text = "INFORMATION", bg = "#EEEEC9", fg = "#48483D", font = font1)
        intro.place(x = 50, y = 20)

        name = Label(info_frame, text = "Name: ", bg = "#EEEEC9", fg = "#48483D", font = font2)
        name.place(x = 50, y = 60)
        self.e1 = ct.Entry(info_frame, width = 65, font = font3)
        self.e1.place(x = 50, y = 90)
        
        age = Label(info_frame, text = "Age: ", bg = "#EEEEC9", fg = "#48483D", font = font2)
        age.place(x = 610, y = 60)
        self.e2 = ct.Entry(info_frame, width = 25, font = font3)
        self.e2.place(x = 610, y = 90)
        
        email = Label(info_frame, text = "Email: ", bg = "#EEEEC9", fg = "#48483D", font = font2)
        email.place(x = 50, y = 130)
        self.e3 = ct.Entry(info_frame, width = 65, font = font3)
        self.e3.place(x = 50, y = 160)
        
        number = Label(info_frame, text = "Contact number: ", bg = "#EEEEC9", fg = "#48483D", font = font2)
        number.place(x = 610, y = 130)
        self.e4 = ct.Entry(info_frame, width = 25, font = font3)
        self.e4.place(x = 610, y = 160)
        
        health = Label(info_frame, text = "ABOUT HEALTH", bg = "#EEEEC9", fg = "#48483D", font = font1)
        health.place(x = 50, y = 220)

        self.rad = StringVar()

        vac = Label(info_frame, text = "Have you been vaccinated?", bg = "#EEEEC9", fg = "#48483D", font = font2)
        vac.place(x = 50, y = 260)
        self.vac1 = ct.Radiobutton(info_frame, text = "Yes, first dose", value = "Partially vaccinated", variable = self.rad, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.vac1.place(x = 70, y = 290)
        self.vac2 = ct.Radiobutton(info_frame, text = "Yes, second dose", value = "Fully vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.vac2.place(x = 175, y = 290)
        self.vac3 = ct.Radiobutton(info_frame, text = "Yes, booster", value = "Vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.vac3.place(x = 300, y = 290)
        self.vac4 = ct.Radiobutton(info_frame, text = "Not yet", value = "Not vaccinated", variable= self.rad, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.vac4.place(x = 400, y = 290)

        self.exp = StringVar()

        exp = Label(info_frame, text = "In the last 14 days, were you exposed to someone that tested positive in COVID-19?", bg = "#EEEEC9", fg = "#48483D", font = font2)
        exp.place(x = 50, y = 340)
        self.exp1 = ct.Radiobutton(info_frame, text = "Yes", value = "Exposed", variable = self.exp, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.exp1.place(x = 70, y = 370)
        self.exp2 = ct.Radiobutton(info_frame, text = "No", value = "Not Exposed", variable = self.exp, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.exp2.place(x = 105, y = 370)
        self.exp3 = ct.Radiobutton(info_frame, text = "Not Sure", value = "Not Certain", variable = self.exp, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = font3)
        self.exp3.place(x = 140, y = 370)

        # Create the submit button (Moved up slightly to fit in the new 500px high frame)
        submitting = Button(info_frame, text = "Submit", command = self.sub, fg = "#48483D", font = font4)
        submitting.place(x = 430, y = 440)

    # Create function for the submit button
    def sub(self):
        data = [self.e1.get().title(), self.e2.get(), self.e3.get(), self.e4.get(), self.rad.get(), self.exp.get()]
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
        try:
            with open("ct_file.csv", "r") as myFile2:
                read_this = csv.reader(myFile2)
                for row in read_this:
                    if row: # Make sure row is not empty
                        entry.append(row)
        except FileNotFoundError:
            messagebox.showerror("Error", "No database found. Please submit an entry first.")
            return
        
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