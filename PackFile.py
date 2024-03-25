# Susana Xiao
# Friday Project 6 GUIs
# DS 3850 Section 001
# The following code is for the Pack File. 
# It creates a simple calculator. There would be an entry box on top with numbers. Below would be a text box

# Imports all functions and variables from tkinter package.
from tkinter import *
from tkinter import ttk

# Calls a new Tk that creates a widget (new window) and assigns it the vairable name "root."
# Creates a title page "Calculator".
root = Tk()
root.title ("Simple Calculator")

entry_frame = ttk.Frame(root)
entry_frame.pack()
entry = ttk.Entry(entry_frame, state='disabled')
entry.pack()


button_frame1 = ttk.Frame(root)
button_frame1.pack()

# Create buttons and place them in the frame
button7 = ttk.Button(button_frame1, text="7")
button7.pack(side="left")

button8 = ttk.Button(button_frame1, text="8")
button8.pack(side="left")

button9 = ttk.Button(button_frame1, text="9")
button9.pack(side="left")


button_frame2 = ttk.Frame(root)
button_frame2.pack()

button4 = ttk.Button(button_frame2, text="4")
button4.pack(side="left")

button5 = ttk.Button(button_frame2, text="5")
button5.pack(side="left")

button6 = ttk.Button(button_frame2, text="6")
button6.pack(side="left")

button_frame3 = ttk.Frame(root)
button_frame3.pack()

button1 = ttk.Button(button_frame3, text="1")
button1.pack(side="left")

button2 = ttk.Button(button_frame3, text="2")
button2.pack(side="left")

button3 = ttk.Button(button_frame3, text="3")
button3.pack(side="left")

button_frame4 = ttk.Frame(root)
button_frame4.pack()

button0 = ttk.Button(button_frame4, text="0")
button0.pack(side="left")

sub  = ttk.Button(button_frame4, text="-")
sub.pack(side="left")

add = ttk.Button(button_frame4, text="+")
add.pack(side="left")

button_frame5 = ttk.Frame(root)
button_frame5.pack()

mult = ttk.Button(button_frame5, text="x")
mult.pack(side="left")

div = ttk.Button(button_frame5, text="/")
div.pack(side="left")

equal = ttk.Button(button_frame5, text="=")
equal.pack(side="left")



root.mainloop()