# Contact-Tracing

**Built for :** Final Project for Object Oriented Programming.

  **Submitted to :** Prof. Danilo Madrigalejos 
  
  **A.Y :** 2022-2023

## About the Project
**CONTACT TRACING**

Create “your” own covid contact tracing app with GUI
	
    - Create a new repository in github
	
    - Create a program that ask user for typical information found in covid contact tracing app
	
    - Write the collected information in a file (use any format you like)
	
    - The app should be able to add and search entry
	
    - Be creative, the realistic the better.
	
    - Please don't submit downloaded program

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

### Contact
Zemerelin Iris M. Membrere - _zemerelinmembrere@gmail.com_

**Project Link :** https://github.com/zem464/Contact-Tracing.git

<p align="right">(<a href="#readme-top">back to top</a>)</p>