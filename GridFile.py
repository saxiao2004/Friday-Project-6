# Susana Xiao
# Friday Project 6 GUIs
# DS 3850 Section 001
# The following code is for the Grid File. 
# It creates a sign up page which would display text boxes that say "Name, Email, and Passwaord." There would also be a button that says "Sign Up Now."

# Imports all functions and variables from tkinter package.
from tkinter import *
from tkinter import ttk

# Calls a new Tk that creates a widget (new window) and assigns it the vairable name "root."
# Creates a title page "Sign-Up Page".
root = Tk()
root.title ("Sign-Up Page")

# Three variable named button and assigned the value of ttk.Label. The grid function provides a location for the text's rows and columns.
name_label = ttk.Label(root, text = "Name:")
name_label.grid(row = 0, column = 0)
email_label = ttk.Label(root, text = "Email:")
email_label.grid(row = 1, column = 0)
password_label = ttk.Label(root, text = "Password:")
password_label.grid(row = 2, column = 0)

# Three variable named entry and assigned the value of ttk.Entry. The grid function provides a location for the text's rows and columns.
name_label = ttk.Entry(root)
name_label.grid(row = 0, column = 1)
email_label = ttk.Entry(root)
email_label.grid (row = 1, column = 1)
password_label = ttk.Entry(root)
password_label.grid(row = 2, column = 1)

# A button function that reads "Sign Up Now."
button = ttk.Button (root, text = "Sign Up Now")
button.grid (row = 3, column = 1)

# The function keeps it running until the user closes the window.
root.mainloop()