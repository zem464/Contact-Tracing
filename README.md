## About the Project
**CONTACT TRACING**

## About the Project
A Python-based desktop application built with Tkinter to securely collect, store, and manage COVID-19 contact tracing information. 

This project simulates a real-world health declaration system, allowing administrators to seamlessly input typical contact tracing data (such as age, contact details, vaccination status, and exposure history) and permanently save it to a local CSV database. It also features a built-in search tool to quickly retrieve and display specific user entries in a clean, secondary window.

Create “your” own covid contact tracing app with GUI
	
    - Create a new repository in github
	
    - Create a program that ask user for typical information found in covid contact tracing app
	
    - Write the collected information in a file (use any format you like)
	
    - The app should be able to add and search entry
	
    - Be creative, the realistic the better.
	
    - Please don't submit downloaded program

## Technical Architecture
This application is structured using Object-Oriented Programming (OOP) principles to ensure clean, modular, and maintainable code:
* **GUI Framework:** Built using Python's standard `tkinter` library. The main application is organized within a custom class that inherits from `Tk`.
* **Data Management:** Utilizes Python's native `csv` module to handle appending new records and reading existing data safely.
* **Window Management:** Leverages `Toplevel` widgets to create dynamic pop-up windows for displaying search results without cluttering the main dashboard.
* **Event Handling:** Custom functions are bound to specific buttons, including automatic state-reset mechanisms that clear entry fields immediately after a successful submission.

## About the Program
**STEPS**

1. Create a file for the GUI and the main file for executing the GUI, and a csv file (or any format you like). 

2. Import the tkinter and create the class for the GUI and create instance for the tkinter, here the instance is *ct*.

    **NOTE** : Do not forget to initialize the class using ``super().__init__()``

3. Create the geometry, title, fonts and colors for the the window. 

4. Create the label fields and entry fields for the information needed. This includes the radiobuttons or checkbuttons that you want to create.

    **NOTE** : Do not forget the placing of the fields using either ``.pack()``, ``.grid()``, or ``.place()``

5. Create the submit function then create the submit button and use the function ``command = submit_function``.

6. Similarly, create the search function then create the search button and entry field for it using the function ``command = search_function``.

7. Under the submit button create a delete function for each of the information entries so you can add again.

8. Under the search function create the toplevel window for displaying the information you searched for. (You can also use a messagebox)

9. In the main file import the GUI and create a root and main module and close the mainloop.

## Running the Program

1. If adding: Input the necessary information in the entry fields and press the submit button.

2. If searching: Enter the full name of who you're looking for then press the search button.

## Usage & License
Feel free to use, modify, or study this repository for whatever reason—whether it is for your own personal projects, learning, or reference! All I ask is that you please provide credit to this GitHub account if you choose to use this code.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
