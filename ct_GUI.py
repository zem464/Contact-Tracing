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
        self.font1 = ("Century Schoolbook", 14, "bold")
        self.font2 = ("Times New Roman", 13, "bold")
        self.font3 = ("Times New Roman", 12, "normal")
        self.font4 = ("Times New Roman", 11, "normal")

        # Frames (Stacked neatly below the title)
        self.search_frame = ct.Frame(self, width = dev_x - 1000, height = 100, bg = "#EEEEC9")
        self.search_frame.pack(pady=10)

        self.info_frame = ct.Frame(self, width = dev_x - 1000, height = 500, bg = "#EEEEC9")
        self.info_frame.pack(pady=10)

        self.setup_search()
        self.info()

    # ==========================================
    # SEARCH SECTION
    # ==========================================
    def setup_search(self):
        here = Label(self.search_frame, text = "Search here...", bg = "#EEEEC9", fg = "#48483D", font = ("Century Schoolbook", 11, "bold"))
        here.place(x = 50, y = 15)
        
        self.bar = ct.Entry(self.search_frame, width = 90, font = self.font3)
        self.bar.place(x = 50, y = 45)

        # FIXED: Added angle brackets
        self.bar.bind("<KeyRelease>", self.predictive_search)

        # FIXED: Changed command to self.search_button_click
        search_btn = ct.Button(self.search_frame, text = "Search", command = self.search_button_click, fg = "#48483D", font = ("Times New Roman", 10, "normal"))
        search_btn.place(x = 800, y = 42)

        self.result_list = ct.Listbox(self, height=5, font=self.font3)
        self.result_list.bind("<<ListboxSelect>>", self.on_result_select)
        
        self.current_matches = []

    def info(self):
        # ==========================================
        # INFORMATION SECTION (Parent is info_frame)
        # ==========================================
        intro = Label(self.info_frame, text = "INFORMATION", bg = "#EEEEC9", fg = "#48483D", font = self.font1)
        intro.place(x = 50, y = 20)

        name = Label(self.info_frame, text = "Name: ", bg = "#EEEEC9", fg = "#48483D", font = self.font2)
        name.place(x = 50, y = 60)
        self.e1 = ct.Entry(self.info_frame, width = 65, font = self.font3)
        self.e1.place(x = 50, y = 90)
        
        age = Label(self.info_frame, text = "Age: ", bg = "#EEEEC9", fg = "#48483D", font = self.font2)
        age.place(x = 610, y = 60)
        self.e2 = ct.Entry(self.info_frame, width = 25, font = self.font3)
        self.e2.place(x = 610, y = 90)
        
        email = Label(self.info_frame, text = "Email: ", bg = "#EEEEC9", fg = "#48483D", font = self.font2)
        email.place(x = 50, y = 130)
        self.e3 = ct.Entry(self.info_frame, width = 65, font = self.font3)
        self.e3.place(x = 50, y = 160)
        
        number = Label(self.info_frame, text = "Contact number: ", bg = "#EEEEC9", fg = "#48483D", font = self.font2)
        number.place(x = 610, y = 130)
        self.e4 = ct.Entry(self.info_frame, width = 25, font = self.font3)
        self.e4.place(x = 610, y = 160)
        
        health = Label(self.info_frame, text = "ABOUT HEALTH", bg = "#EEEEC9", fg = "#48483D", font = self.font1)
        health.place(x = 50, y = 220)

        # ==========================================
        # COLUMN 1: VACCINATION (Left Side)
        # ==========================================
        self.is_vac_var = StringVar()
        self.is_vac_var.set("") 

        vac_base = Label(self.info_frame, text = "Have you been vaccinated?", bg = "#EEEEC9", fg = "#48483D", font = self.font2)
        vac_base.place(x = 50, y = 260)
        
        # Primary Yes/No column (X = 70)
        self.base_yes = ct.Radiobutton(self.info_frame, text="Yes", value="Yes", variable=self.is_vac_var, command=self.toggle_dose_options, indicatoron=0, bg="#EEEEC9", fg="#48483D", font=self.font3)
        self.base_yes.place(x=70, y=290)
        
        self.base_no = ct.Radiobutton(self.info_frame, text="No", value="No", variable=self.is_vac_var, command=self.toggle_dose_options, indicatoron=0, bg="#EEEEC9", fg="#48483D", font=self.font3)
        self.base_no.place(x=70, y=325) 

        self.rad = StringVar() 
        self.rad.set("")

        # Secondary Dose column (Shifted right to X = 160, Y aligned with Yes/No)
        self.vac1 = ct.Radiobutton(self.info_frame, text = "First dose", value = "Partially vaccinated", variable = self.rad, state=ct.DISABLED, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = self.font3)
        self.vac1.place(x = 160, y = 290)
        
        self.vac2 = ct.Radiobutton(self.info_frame, text = "Second dose", value = "Fully vaccinated", variable= self.rad, state=ct.DISABLED, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = self.font3)
        self.vac2.place(x = 160, y = 325)
        
        self.vac3 = ct.Radiobutton(self.info_frame, text = "Booster", value = "Vaccinated", variable= self.rad, state=ct.DISABLED, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = self.font3)
        self.vac3.place(x = 160, y = 360)

        # ==========================================
        # COLUMN 2: EXPOSURE (Right Side)
        # ==========================================
        self.exp = StringVar()

        exp = Label(self.info_frame, text = "In the last 14 days, were you exposed to someone that tested positive in COVID-19?", bg = "#EEEEC9", fg = "#48483D", font = self.font2, wraplength=500, justify="left")
        exp.place(x = 350, y = 260)
        
        # Stacked vertically (Y increases, X stays at 520)
        self.exp1 = ct.Radiobutton(self.info_frame, text = "Yes", value = "Exposed", variable = self.exp, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = self.font3)
        self.exp1.place(x = 370, y = 310)
        
        self.exp2 = ct.Radiobutton(self.info_frame, text = "No", value = "Not Exposed", variable = self.exp, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = self.font3)
        self.exp2.place(x = 430, y = 310) 
        
        self.exp3 = ct.Radiobutton(self.info_frame, text = "Not Sure", value = "Not Certain", variable = self.exp, indicatoron = 0, bg = "#EEEEC9", fg = "#48483D", font = self.font3)
        self.exp3.place(x = 490, y = 310) 

        # ==========================================
        # SUBMIT BUTTON
        # ==========================================
        # Pushed down to y=480 so it clears the new vertical buttons
        submitting = Button(self.info_frame, text = "Submit", command = self.sub, fg = "#48483D", font = self.font4)
        submitting.place(x = 430, y = 420)

    def toggle_dose_options(self):
        """Enables or disables dose options based on the Yes/No selection."""
        if self.is_vac_var.get() == "Yes":
            self.vac1.configure(state=ct.NORMAL)
            self.vac2.configure(state=ct.NORMAL)
            self.vac3.configure(state=ct.NORMAL)
        else:
            self.vac1.configure(state=ct.DISABLED)
            self.vac2.configure(state=ct.DISABLED)
            self.vac3.configure(state=ct.DISABLED)
            self.rad.set("") # Clear the dose selection if they switch back to "No"

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

    # Create the function for the predictive search
    def predictive_search(self, event):
        # Runs every time a key is pressed in the search bar.
        typed = self.bar.get().strip().lower()
        
        # Hide the dropdown if the search bar is empty
        if not typed:
            self.result_list.place_forget()
            return

        self.current_matches = []
        try:
            with open("ct_file.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if not row: continue
                    
                    # Check if typed text is IN Name (0), Age (1), Email (2), or Contact (3)
                    # This allows partial matches across all those columns
                    if any(typed in str(row[i]).lower() for i in range(min(4, len(row)))):
                        self.current_matches.append(row)
        except FileNotFoundError:
            pass # Ignore silently if the database doesn't exist yet

        # Update the Listbox GUI
        self.result_list.delete(0, ct.END)
        if self.current_matches:
            
            # Set height to the exact number of matches, but cap it at 5 so it doesn't get too long
            display_count = min(len(self.current_matches), 5)
            self.result_list.configure(height=display_count)

            self.result_list.place(in_=self.bar, x=0, rely=1.0, relwidth=1.0)
            self.result_list.lift() # Force the widget to draw on top of everything else
            
            for match in self.current_matches:
                # Extract the data
                name = match[0]
                email = match[2]
                contact = match[3]

                # Smart Truncation (Limits length so it fits in the box)
                # If a name is longer than 25 chars, cut it and add "..."
                if len(name) > 25: name = name[:22] + "..."
                
                # If an email is longer than 30 chars, cut it and add "..."
                if len(email) > 30: email = email[:27] + "..."

                # Build the clean, limited-length display text
                display_text = f"{name:<25}  |  Email: {email:<30}  |  No: {contact}"
                
                self.result_list.insert(ct.END, display_text)
        else:
            self.result_list.place_forget() # Hide if no matches found

    def on_result_select(self, event):
        """Triggers when a user clicks a name in the predictive dropdown."""
        selection = self.result_list.curselection()
        if selection:
            index = selection[0]
            selected_data = self.current_matches[index]
            self.display_info_window(selected_data)
            
            # Reset the search bar after selection
            self.bar.delete(0, ct.END)
            self.result_list.place_forget()

    def search_button_click(self):
        """Fallback for the physical button."""
        if self.current_matches:
            # Show the top result if they hit the search button instead of clicking the list
            self.display_info_window(self.current_matches[0])
            self.bar.delete(0, ct.END)
            self.result_list.place_forget()
        else:
            messagebox.showerror("Not Found", "What you're looking for is not in the system")

    def display_info_window(self, entry_row):
        """Builds and displays the Toplevel window based on the selected row data."""
        info = ct.Toplevel(self)
        info.title("Information")
        info.geometry("300x225")
        info.configure(bg = "#8B8B75")

        # Fonts
        font5 = ("Century Schoolbook", 12, "bold")
        font6 = ("MS Sans Serif", 10, "bold")
        font7 = ("MS Sans Serif", 10, "normal")

        # Frame and title
        frame_about = ct.Frame(info, width = 265, height = 155, bg = "#CDCDAD")
        frame_about.place(x = 20, y = 55)

        title = ct.Label(info, text = " ABOUT ", bg = "#8B8B75", fg = "#EEEEC9", font = font5)
        title.place(x = 115, y = 20)
        
        # Display data directly from the passed row array
        labels = [
            ("Name:", entry_row[0], 25, 60, 90),
            ("Age:", entry_row[1], 25, 85, 90),
            ("Email:", entry_row[2], 25, 110, 90),
            ("Contact No.:", entry_row[3], 25, 135, 120),
            ("Vaccination:", entry_row[4], 25, 160, 160),
            ("Exposure:", entry_row[5], 25, 185, 110)
        ]

        # Generate the info labels using a loop for cleaner code
        for label_text, data_text, x1, y, x2 in labels:
            ct.Label(info, text=label_text, bg="#CDCDAD", font=font6).place(x=x1, y=y)
            ct.Label(info, text=data_text, bg="#CDCDAD", font=font7).place(x=x2, y=y)
