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
ASSOCIATED_HOSP = 7

lastUniqueID = 0

# format:
#    ID, name, phone number, address, blood group, quantity, date donated
donors = []

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

hospitals = [
    "Apollo", 
    "Fortis",
    "Narayana"
]

for i in range(1, 32):
    date.append(i)

for i in range(2023, 2027):
    year.append(i)


# def Welcome():

#     global WMaster
#     WMaster = Tk()
#     WMaster.geometry("500x300+200+300")
#     WMaster.title("Blood Bank Agency")
#     WMaster.resizable(False, False)
#     WMaster.configure(bg="#FFF")

#     welcomeTextp2 = Label(WMaster, text="BlOOD BANK AGENCY", font=("", 30),fg="#000000", bg="#FFF")
#     welcomeTextp2.place(x=30, y = 100)

#     enter_btn =  Button(WMaster, text="Enter", font=("", 15),fg='white',bg='#ff2400', command=openHS)
#     enter_btn.place(x=205, y=200)

def HomeScreen():
    global HSMaster
    HSMaster = Tk()
    HSMaster.geometry("500x400+200+300")
    HSMaster.title("Blood Bank Agency")
    HSMaster.resizable(False, False)
    HSMaster.configure(bg="#FFF")

    addentrybutton = Button(HSMaster, text="Add Entry", command=openAE)
    addentrybutton.place(x=20, y=20)

    global donorsList
    donorsList = Listbox(HSMaster)
    for donor in donors:
        donorsList.insert(END, donor)
    donorsList.pack()

    print(donors)

def donate_blood():

    #TODO: Add a "Associated Hospital" field and respective drop-down menu
    global AEMaster
    AEMaster = Tk()
    AEMaster.geometry("400x300+200+300")
    AEMaster.title("Blood Bank Agency")
    AEMaster.resizable(False, False)
    AEMaster.configure(bg="#FFF")

    UniqueID = Label(AEMaster, fg="#2c2c2c", bg="#FFF", text="Unique ID :" + str(lastUniqueID+1), font=("", 13))
    UniqueID.place(x=10, y=30)
    
    NameLbl = Label(AEMaster, fg="#000000", bg="#FFF", text="First Name: ", font=("", 13))
    NameLbl.place(x=10, y=70)

    NameEntry = Entry(AEMaster, bg="#ffffff", fg="#000000")
    NameEntry.place(x = 155, y = 75)

    AmntOfBloodLbl = Label(AEMaster, fg="#000000", bg="#FFF", text="Amount of Blood(ml): ", font=("", 11))
    AmntOfBloodLbl.place(x=10, y=100)

    AmntOfBloodEntry = Entry(AEMaster, bg="#ffffff")
    AmntOfBloodEntry.place(x = 155, y = 105)


    MobileNumLbl = Label(AEMaster, fg="#000000", bg="#FFF", text="Mobile Number: ", font=("", 11))
    MobileNumLbl.place(x=10, y=130)

    MobileNumEntry = Entry(AEMaster, bg="#ffffff")
    MobileNumEntry.place(x = 155, y = 135)

    AddressLbl = Label(AEMaster, fg="#000000", bg="#FFF", text="Address: ", font=("", 11))
    AddressLbl.place(x=10, y=160)

    AddressEntry = Entry(AEMaster, bg="#ffffff", width=35)
    AddressEntry.place(x = 155, y = 165)

    BldGrpLbl = Label(AEMaster, fg="#000000", bg="#FFF", text="Blood Group: ", font=("", 11))
    BldGrpLbl.place(x=10, y=190)

    selected_blood_group = StringVar(AEMaster)
    BloodGroup = ttk.Combobox(AEMaster, textvariable=selected_blood_group, values=blood_groups, width=2, state="readonly")
    BloodGroup.place(x=155, y=190)

    DateLbl = Label(AEMaster, fg="#000000", bg="#FFF", text="Date: ", font=("", 11))
    DateLbl.place(x=10, y=220)

    selected_date = StringVar(AEMaster)
    DateDrpDown = ttk.Combobox(AEMaster, textvariable=selected_date, values=date, width=2, state="readonly")
    DateDrpDown.place(x=155, y=220)

    selected_month = StringVar(AEMaster)
    Month = ttk.Combobox(AEMaster, textvariable=selected_month, values=month, width=7, state="readonly")
    Month.place(x=215, y=220)

    selected_year = StringVar(AEMaster)
    yrdrpdown = ttk.Combobox(AEMaster, textvariable=selected_year, values=year, width=5, state="readonly")
    yrdrpdown.place(x=320, y=220)

    addEntryBtn = Button(AEMaster, text="Add Entry", command=lambda: add_entry(
        lastUniqueID, NameEntry.get(), MobileNumEntry.get(), AddressEntry.get(),
        selected_blood_group.get(), AmntOfBloodEntry.get(), int(selected_date.get()),
        selected_month.get(), int(selected_year.get())
    ))
    addEntryBtn.place(x=150, y=260)

    backButton = Button(AEMaster, text="Back", command=lambda: back(AEMaster))
    backButton.place(x = 200, y = 260)

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

    BloodGroup = OptionMenu(Rcpmaster, StringVar(), *blood_groups)
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
    HDmaster.geometry("350x250+200+300")
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
    Proceedbtn.place(x=150, y=200)


# def openHS():
#     WMaster.destroy()
#     HomeScreen() 

def openAE():
    HSMaster.destroy()
    donate_blood()

def add_entry(Id, Name, Mobile, Address, Blood_Group, Quantity, Date, Month, Year):
    donors.append([Id, str(Name), Mobile, Address, Blood_Group, Quantity, [Date, Month, Year]])


def test(selectedBldGrp):
    print(selectedBldGrp)


def back(_from):
    _from.destroy()
    HomeScreen()

HomeScreen()

mainloop()
