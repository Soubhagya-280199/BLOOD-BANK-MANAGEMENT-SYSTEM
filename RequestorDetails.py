from tkinter import *
import csv
from tkinter import messagebox

# CREATING TKINTER
root = Tk()
root.title("Requestor Details")

# CREATING CANVAS
canvas1 = Canvas(root,width=1500,height = 1500,background="gray")
canvas1.pack()


# input here
adharno = Label(text="AADHAR NUMBER",width="20",bg="blue",fg="white").place(x=400,y=300)
adhar = Entry(textvariable=adharno,width=50)
adhar.place(x=570,y=300)


## ORDERING TABLE
adharno=Label(text="AADHAR NO",font=("caliber",8),bg="yellow",fg="blue").place(x=385,y=350)

name=Label(text="NAME",font=("caliber",8),bg="yellow",fg="blue").place(x=500,y=350)

age=Label(text="AGE",font=("caliber",8),bg="yellow",fg="blue").place(x=560,y=350)

dob=Label(text="D-O-B",font=("caliber",8),bg="yellow",fg="blue").place(x=600,y=350)

bgroup=Label(text="GROUP",font=("caliber",8),bg="yellow",fg="blue").place(x=650,y=350)

phone=Label(text="PHONE",font=("caliber",8),bg="yellow",fg="blue").place(x=700,y=350)

city=Label(text="CITY",font=("caliber",8),bg="yellow",fg="blue").place(x=750,y=350)

state=Label(text="STATE",font=("caliber",8),bg="yellow",fg="blue").place(x=800,y=350)


def close():
    exit()

def search():
    ano = adhar.get()

    csv_file = csv.reader(open('RequestorRegistration.csv'))
    for row in csv_file:
        if ano == row[0]:
            label1 = Label(text=row)
            canvas1.create_window(620, 400, window=label1)
            break

# BUTTTON SUBMIT
submitbutton = Button(root,text="SUBMIT",width="20",font=("Arial Black",12,"bold"),fg="red",bg="black",command=search)
submitbutton.place(x=550,y=500)

# CLOSE BUTTON
closebutton = Button(root,text="EXIT",width="20",font=("Arial Black",12,"bold"),fg="red",bg="black",command=close)
closebutton.place(x=550,y=550)

mainloop()