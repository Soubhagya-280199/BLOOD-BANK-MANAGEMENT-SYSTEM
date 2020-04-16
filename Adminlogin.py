from tkinter import *
import os
import csv
from tkinter import messagebox

# DECLARING TKINTER
root = Tk()
root.title("Admin Login")

#CREATING CANVSAS
canvas1 = Canvas(root,width=1500,height = 1500,background="orange")
canvas1.pack()

#EXITING FUNCTION
def exitprgrm():
    exit()

#CALLING FILES
def callingdonorpage():
    os.system("python DonorDetails.py")

def callingrequstorpage():
    os.system("python RequestorDetails.py")

### user login criteria
def login():
    user_name = unameinput.get()
    pwd_name = pwdinput.get()

    if (user_name == "SOUBHAGYA_28"):
        if (pwd_name == "280199"):
            donordeatils = Button(root, text="DONOR\nDETAILS", width="20", font=("Arial Black", 12, "bold"), fg="red", bg="yellow", command=callingdonorpage)
            donordeatils.place(x=400, y=400)

            requestordetails = Button(root, text="REQST\nDETAILS", width="20", font=("Arial Black", 12, "bold"), fg="red", bg="yellow", command=callingrequstorpage)

            requestordetails.place(x=650, y=400)

        else:
            messagebox.showerror("Error", "Invalid Password")
    else:
        messagebox.showerror("Error","Invalid Username")

#USER NAME DECLARATION
uname = Label(text= "User Name",font=("Arial black",8),width="20",bg="blue",fg="white").place(x=400,y=180)
unameinput = Entry(textvariable=uname,width=35)
unameinput.place(x=600,y=180)

#PASSWORD DECLARATION
pwd = Label(text= "Password",font=("Arial black",8),width="20",bg="blue",fg="white").place(x=400,y=220)
pwdinput= Entry(textvariable=pwd,width=35)
pwdinput.place(x=600,y=220)

#CREATING  SUBMIT BUTTON
button1= Button(text="OK",width="15",font=("Arial black",12,"bold"),fg="red",bg="white",command=login)
button1.place(x=550,y=280)

#CREATING EXITING BUTTON
button2 =Button(text="Cancel",width="15",font=("Arial black",12,"bold"),fg="white",bg="red",command=exitprgrm).place(x=550,y=330)

mainloop()