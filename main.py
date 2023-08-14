'''#2c2c2c-greybg  #ff2400-red, text'''
from tkinter import *
from tkinter import ttk

# giving index numbers their own variable so it will be easier to call them and refer to them in code
ID = 0
NAME = 1
PHONE_NUM = 2
ADDRESS = 3
BLOOD_GROUP = 4
QTY = 5
DATE_OF_DON = 6

lastUniqueID = 0

# format:
#    ID, name, phone number, address, blood group, quantity, date donated
donors = {}

blood_groups = [
    "A+",
    "A-",
    "B+",
    "B-",
    "O+",
    "O-",
    "AB+",
    "AB-"
]

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "Septmber",
    "October",
    "November",
    "December",
]

year = []

date = []

for i in range(1, 32):
    date.append(i)

for i in range(2023, 2027):
    year.append(i)


def Welcome():

    global WMaster
    WMaster = Tk()
    WMaster.geometry("500x300+200+300")
    WMaster.title("Blood Bank Agency")
    WMaster.resizable(False, False)
    WMaster.configure(bg="#FFF")

    welcomeTextp2 = Label(WMaster, text="BlOOD BANK AGENCY", font=("", 30),fg="#000000", bg="#FFF")
    welcomeTextp2.place(x=30, y = 100)

    enter_btn =  Button(WMaster, text="Enter", font=("", 15),fg='white',bg='#ff2400', command=openHS)
    enter_btn.place(x=205, y=200)

def HomeScreen():
    global HSMaster
    HSMaster = Tk()
    HSMaster.geometry("500x400+200+300")
    HSMaster.title("Blood Bank Agency")
    HSMaster.resizable(False, False)
    HSMaster.configure(bg="#FFF")

    addentrybutton = Button(HSMaster, text="Add Entry", command=openAE)
    addentrybutton.place(x=20, y=20)

def add_entry_window():

    global AEmaster
    AEmaster = Tk()
    AEmaster.geometry("400x300+200+300")
    AEmaster.title("Blood Bank Agency")
    AEmaster.resizable(False, False)
    AEmaster.configure(bg="#FFF")

    UniqueID = Label(AEmaster, fg="#2c2c2c", bg="#FFF", text="Unique ID :" + str(lastUniqueID+1), font=("", 13))
    UniqueID.place(x=10, y=30)
    
    NameLbl = Label(AEmaster, fg="#000000", bg="#FFF", text="First Name: ", font=("", 13))
    NameLbl.place(x=10, y=70)

    NameEntry = Entry(AEmaster, bg="#ffffff")
    NameEntry.place(x = 155, y = 75)

    AmntOfBloodLbl = Label(AEmaster, fg="#000000", bg="#FFF", text="Amount of Blood(ml): ", font=("", 11))
    AmntOfBloodLbl.place(x=10, y=100)

    AmntOfBloodEntry = Entry(AEmaster, bg="#ffffff")
    AmntOfBloodEntry.place(x = 155, y = 105)


    MobileNumLbl = Label(AEmaster, fg="#000000", bg="#FFF", text="Mobile Number: ", font=("", 11))
    MobileNumLbl.place(x=10, y=130)

    MobileNumEntry = Entry(AEmaster, bg="#ffffff")
    MobileNumEntry.place(x = 155, y = 135)

    AddressLbl = Label(AEmaster, fg="#000000", bg="#FFF", text="Address: ", font=("", 11))
    AddressLbl.place(x=10, y=160)

    AddressEntry = Entry(AEmaster, bg="#ffffff", width=35)
    AddressEntry.place(x = 155, y = 165)

    BldGrpLbl = Label(AEmaster, fg="#000000", bg="#FFF", text="Blood Group: ", font=("", 11))
    BldGrpLbl.place(x=10, y=190)

    BloodGroup = OptionMenu(AEmaster, StringVar(), *blood_groups)
    BloodGroup.place(x=155, y=190)

    DateLbl = Label(AEmaster, fg="#000000", bg="#FFF", text="Date: ", font=("", 11))
    DateLbl.place(x=10, y=220)

    DateDrpDown = OptionMenu(AEmaster, StringVar(), *date)
    DateDrpDown.place(x=155, y=220)

    Month = OptionMenu(AEmaster, StringVar(), *month)
    Month.place(x=215, y=220)

    yrdrpdown = OptionMenu(AEmaster, StringVar(), *year)
    yrdrpdown.place(x=320, y=220)

    addEntryBtn = Button(AEmaster, text="Add Entry", command=add_entry)
    addEntryBtn.configure(highlightbackground="#000000")
    addEntryBtn.place(x=150, y=260)

def deleteEntry():

    global DEmaster
    DEmaster = Tk()
    DEmaster.geometry("700x600+200+300")
    DEmaster.title("Blood Bank Agency")
    DEmaster.resizable(False, False)
    DEmaster.configure(bg="#FFF")

    #options_menu(DEmaster)

    uniqueIdReq = Label(DEmaster, fg="#000000", bg="#FFF", text="Unique id: ", font=("", 40))
    uniqueIdReq.place(x=+10, y=+170)

    uniqueIdEntry = Entry(DEmaster, bg="#ffffff")
    uniqueIdEntry.place(x=+300, y=+200)

    deleteButton = Button(DEmaster, text="Delete Entry")
    deleteButton.configure(highlightbackground="#000000")
    deleteButton.place(x=+300, y=+230)

def RequestBloodDon():
    global RBDMaster
    RBDMaster = Tk()
    RBDMaster.geometry("700x600+200+300")
    RBDMaster.title("Blood Bank Agency")
    RBDMaster.resizable(False, False)
    RBDMaster.configure(bg="#FFF")

def RECIPNT():
    global Rcpmaster
    Rcpmaster = Tk()
    Rcpmaster.geometry("400x300+200+300")
    Rcpmaster.title("Blood Bank Agency")
    Rcpmaster.resizable(False, False)
    Rcpmaster.configure(bg="#FFF")

    UniqueID = Label(Rcpmaster, fg="#2c2c2c", bg="#FFF", text=" Recipient ID :" + str(lastUniqueID+1), font=("", 13))
    UniqueID.place(x=10, y=30)
    
    NameLbl = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Recipient Name: ", font=("", 13))
    NameLbl.place(x=10, y=70)

    NameEntry = Entry(Rcpmaster, bg="#ffffff")
    NameEntry.place(x = 155, y = 75)

    AmntOfBloodLbl = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Quantity recieved(ml): ", font=("", 11))
    AmntOfBloodLbl.place(x=10, y=100)

    AmntOfBloodEntry = Entry(Rcpmaster, bg="#ffffff")
    AmntOfBloodEntry.place(x = 155, y = 105)


    MobileNumLbl = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Mobile Number: ", font=("", 11))
    MobileNumLbl.place(x=10, y=130)

    MobileNumEntry = Entry(Rcpmaster, bg="#ffffff")
    MobileNumEntry.place(x = 155, y = 135)

    AddressLbl = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Hospital ID ", font=("", 11))
    AddressLbl.place(x=10, y=160)

    AddressEntry = Entry(Rcpmaster, bg="#ffffff", width=35)
    AddressEntry.place(x = 155, y = 165)

    BldGrpLbl = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Bloodgrp recieved: ", font=("", 11))
    BldGrpLbl.place(x=10, y=190)

    BloodGroup = OptionMenu(Rcpmaster, StringVar(), *BLD_GRP)
    BloodGroup.place(x=155, y=190)

    DateLbl = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Date recieved: ", font=("", 11))
    DateLbl.place(x=10, y=220)

    DateDrpDown = OptionMenu(Rcpmaster, StringVar(), *date)
    DateDrpDown.place(x=155, y=220)

    Month = OptionMenu(Rcpmaster, StringVar(), *month)
    Month.place(x=215, y=220)

    yrdrpdown = OptionMenu(Rcpmaster, StringVar(), *year)
    yrdrpdown.place(x=320, y=220)

    addEntryBtn = Button(Rcpmaster, text="Add Entry")
    addEntryBtn.configure(highlightbackground="#000000")
    addEntryBtn.place(x=150, y=260)

def HospitalDetails():

    global HDmaster
    HDmaster = Tk()
    HDmaster.geometry("350x300+200+300")
    HDmaster.title("Hospital Details")
    HDmaster.resizable(False, False)
    HDmaster.configure(bg="#FFF")

    #options_menu(DEmaster)

    NameLbl = Label(HDmaster, fg="#000000", bg="#FFF", text="hospital ID: ", font=("", 13))
    NameLbl.place(x=10, y=70)

    NameEntry = Entry(HDmaster, bg="#ffffff")
    NameEntry.place(x = 180, y = 70)

    NameLbl = Label(HDmaster, fg="#000000", bg="#FFF", text="hospitalName: ", font=("", 13))
    NameLbl.place(x=10, y=100)

    NameEntry = Entry(HDmaster, bg="#ffffff")
    NameEntry.place(x = 180, y = 105)

    NameLbl = Label(HDmaster, fg="#000000", bg="#FFF", text="Contact Person Name: ", font=("", 13))
    NameLbl.place(x=10, y=130)

    NameEntry = Entry(HDmaster, bg="#ffffff")
    NameEntry.place(x = 180, y = 135)

    NameLbl = Label(HDmaster, fg="#000000", bg="#FFF", text="Contact number: ", font=("", 13))
    NameLbl.place(x=10, y=160)

    NameEntry = Entry(HDmaster, bg="#ffffff")
    NameEntry.place(x = 180, y = 165)
    
    Proceedbtn = Button(HDmaster, text="Proceed ")
    Proceedbtn.configure(highlightbackground="#000000")
    Proceedbtn.place(x=150, y=260)


def openHS():
    WMaster.destroy()
    HomeScreen()

def openAE():
    HSMaster.destroy()
    add_entry()

Welcome()

mainloop()

HospitalDetails()
