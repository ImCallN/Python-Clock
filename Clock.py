#A simple clock program that I'll just have running on the desktop
#Collin Dunkle, October 5, 2020

#This imports our time modules into the program
import time
from tkinter import *

#This is for screen resolution
import ctypes
user32 = ctypes.windll.user32

screenHeight = user32.GetSystemMetrics(0)
screenWidth = user32.GetSystemMetrics(1)
centerHeight = screenHeight/2
centerWidth = screenWidth/2

print("Screen Height: ", screenHeight)
print("Screen Width: ", screenWidth)
print("Center: ", centerHeight, centerWidth)

#creates our root
root = Tk()
root.title("Click Clack Clock")
root.geometry("500x200")
root.resizable(0,0)

#creates our label

label = Label(root, font=("Arial", 80, 'bold'), bg="black", fg="lime", bd=30)
label.grid(row=1, column=1)

def clack():
	text_input = time.strftime("%H:%M:%S")
	label.config(text=text_input)
	label.after(200, clack)
clack()
root.mainloop()
