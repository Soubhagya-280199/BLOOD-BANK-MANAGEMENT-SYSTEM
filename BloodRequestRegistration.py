from tkinter import *
from tkinter import messagebox
import csv

# CREATING TKINTER
root=Tk()
root.title("Requestor Registration")

# CREATING
root.configure(background="pink")

# SHOW INFORMATION
def helpmessage():
    message = messagebox.showinfo("HELP","Fill all the Information")

def exitprgrm():
    exit()
################### Values stores at here  ##########################
def store():
    #### storing name
    name_store = nameinput.get()

    #### storing age
    age_store = ageinput.get()

    ### storing dob
    aday = date.get()
    amonth = month.get()
    ayear = year.get()

    dob_store = aday +"-"+ amonth+"-"+  ayear

    ### storing blooodgroup
    bloodgrp_store = blood.get()

    ### storing Aadharr number
    adhar_store = adharinput.get()

    ### storing phone
    phone_store = phoneinput.get()

    ### storing city
    city_store = cityinput.get()

    ### storing state
    state_store = stateinput.get()

    ### storing in csv file
    with open('RequestorRegistration.csv', 'a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([adhar_store,name_store, age_store, dob_store, bloodgrp_store, phone_store, city_store, state_store])
        csvfile.close()

    ### Submit Succesful message
    messagebox.showinfo("THANKS", " Request Successfully Submitted")


month = StringVar(root)
year = StringVar(root)
blood = StringVar(root)
date = StringVar(root)

canvas=Canvas(root,width=2000,height=4000,background="magenta")      # cyan ,magenta
canvas.grid(row=500,column=600)

heading = Label(text="Requestor Registration",font=("Arial black",30,"bold"),fg="Yellow",bg="magenta").place(x=480,y=40)


name = Label(text="Name",width="10",bg="blue",fg="white").place(x=500,y=180)
nameinput = Entry(textvariable=name,width=45)
nameinput.place(x=600,y=180)

age = Label(text="Age",width="10",bg="blue",fg="white").place(x=500,y=220)
ageinput = Entry(textvariable=age,width=45)
ageinput.place(x=600,y=220)

dob = Label(text="Date of Birth",width="10",bg="blue",fg="white").place(x=500,y=260)


datelist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
droplist0=OptionMenu(root,date,*datelist)
droplist0.config(width=4,height=1)
date.set(1)
droplist0.place(x=600,y=260)

monthlist = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
droplist = OptionMenu(root,month,*monthlist)
droplist.config(width=4,height=-3)
month.set("Jan")
droplist.place(x=680,y=260)

yearlist = [1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,
            1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,
            2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,]
droplist1=OptionMenu(root,year,*yearlist)
droplist1.config(width=4,height=1)
year.set(2020)
droplist1.place(x=750,y=260)


bloodgrp = Label(text="Select \nBlood group",width="12",bg="blue",fg="white").place(x=500,y=305)
bloodlist = ["O+ve","O-ve","A+ve","A-ve","B+ve","B-ve","AB+","AB-ve"]
droplist2 = OptionMenu(root,blood,*bloodlist)
droplist2.config(width =4, height= 1)
blood.set("O+ve")
droplist2.place(x=600,y=305)

## AADHARR NUMBER INPUT
adharno = Label(text="Aadharr\nNumber",width="12",bg="blue",fg="white").place(x=680,y=305)
adharinput = Entry(textvariable=adharno,width=18)
adharinput.place(x=775,y=310)


phone = Label(text="Phone",width="10",bg="blue",fg="white").place(x=500,y=355)
phoneinput = Entry(textvariable=phone,width=45)
phoneinput.place(x=600,y=355)

city = Label(text="City",width="10",bg="blue",fg="white").place(x=500,y=400)
cityinput = Entry(textvariable=city,width=45)
cityinput.place(x=600,y=400)

state = Label(text="State",width="10",bg="blue",fg="white").place(x=500,y=440)
stateinput = Entry(textvariable=state,width=45)
stateinput.place(x=600,y=440)


###ALL BUTTTON HERE
submitbutton = Button(root,text="SUBMIT",width="20",font=("Arial Black",12,"bold"),fg="red",bg="yellow",command=store)
submitbutton.place(x=600,y=500)

helptbutton = Button(root,text="HELP",width="8",font=("Arial Black",12,"bold"),fg="Red",bg="white",command=helpmessage)
helptbutton.place(x=600,y=550)

exittbutton = Button(root,text="EXIT",width="8",font=("Arial Black",12,"bold"),fg="Red",bg="white",command=exitprgrm)
exittbutton.place(x=698,y=550)

mainloop()