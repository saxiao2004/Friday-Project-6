# Susana Xiao
# Friday Project 6 GUIs
# DS 3850 Section 001
# The following code is for the place file. 
# It creates a log in page that displays the text box "Username" and "Password." There would also be entry boxes for users to type and a button that reads "Login."

# Imports all functions and variables from tkinter package.
from tkinter import *
from tkinter import ttk

# Calls a new Tk that creates a widget (new window) and assigns it the vairable name "root."
# Creates a title page "Log-In Page".
root = Tk()
root.title ("Login-In Page")

# Variable named "sampleLable1" and "sampleLabel2" assigned the value of ttk.Label to display texts.
username_label = ttk.Label (root, text = "Username:")
password_label = ttk.Label (root, text = "Password:")

# The place function provides a location for the text's pixel placement.
username_label.place (x = 0, y = 40)
password_label.place (x = 0, y = 80)

# The function creates a text box for the user to type.
username_entry = ttk.Entry(root)
password_entry = ttk.Entry (root)

# The place function provides a location for the text's pixel placement
username_entry.place (x = 60, y = 40)
password_entry.place (x = 60, y = 80)

# A button function that reads "Login."
login_button = ttk.Button (root, text = "Login")
login_button.place (x = 80, y = 115)

# The function keeps it running until the user closes the window.
root.mainloop()