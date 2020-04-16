from tkinter import *
import os
import sys
from tkinter import messagebox

#DECLARING TKINTER
root =Tk()
root.title("WELCOME TO BLOOD BANK")

# Creating a canvas setup for more atrractive background
canvas1 = Canvas(root,width=1500,height = 1500,background="yellow")
canvas1.pack()

# Declaring title of the User Interface #
root.title("Home Page")

# Declaring root library here
root.geometry

###### Caliin all python files #########

def Donorregistration():
    os.system('python DonorRegistration.py')

def Adminlogin():
    os.system('python Adminlogin.py')

def Bloodrequest():
    os.system('python BloodRequestRegistration.py')

def exitprgm():
    exit()





# Header line NEW LIFE BLOOD BANK
heading =Label(text="NEW LIFE BLOOD BANK",font=("Arial Black",30,"bold"),fg="purple",bg="yellow")           #tan ,navy indigo silver gold
heading.place(x=410,y=90)

# Donor Resistration button
donorbutton = Button(root,text="Donor Registration",width="30",font=("Arial Black",12,"bold"),fg="white",bg="blue",command=Donorregistration)
donorbutton.place(x=500,y=250)

# Request Blood button
requestbutton = Button(root,text="Blood Request Registration",width="30",font=("Arial Black",12,"bold"),fg="white",bg="blue",command=Bloodrequest)
requestbutton.place(x=500,y=300)

# Admin login button
adminbutton = Button(root,text="Admin Login",width="30",font=("Arial Black",12,"bold"),fg="white",bg="blue",command=Adminlogin)
adminbutton.place(x=500,y=350)

# Exit button
exitbutton = Button(root,text="Exit",width="15",font=("Arial Black",12,"bold"),fg="cyan",bg="red",command=exitprgm)
exitbutton.place(x=900,y=550)





mainloop()
