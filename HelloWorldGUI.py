# Import library
import sys
from tkinter import *

# Entry point function
def main():
    root_window = Tk()
    root_window.title("Python GUI Program")
    root_window.geometry("500x500")

    message = Label(root_window, text="Hello GUI World!!! By Taufik")
    message.grid(row=0,column=0)

    root_window.mainloop()

# Call entry point function
main()

