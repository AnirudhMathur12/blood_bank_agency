'''#2c2c2c-greybg  #ff2400-red, text'''
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Imageg

# giving index numbers their own variable so it will be easier to call them and refer to them in code
ID = 0
NAME = 1
PHONE_NUM = 2
ADDRESS = 3
BLOOD_GROUP = 4
QTY = 5
DATE = 6
ASSOCIATED_HOSP = 7

lastUniqueID = 0

# format:
#    ID, name, phone number, address, blood group, quantity, date donated
donors = []
Recipients = []
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
# x=20,y=20,50,80,110,140,170


# home screen
def HomeScreen():
    lastUniqueID = 0
    global HSMaster
    HSMaster = Tk()
    HSMaster.geometry("500x400+200+300")
    HSMaster.title("Blood Bank Agency")
    HSMaster.resizable(False, False)
    HSMaster.configure(bg="#FFF")

    img = ImageTk.PhotoImage(Image.open("blood_bank_agency/bg.png").resize((500, 400), Image.ADAPTIVE))
    ImgLabel = Label(HSMaster, image=img)
    ImgLabel.image = img

    ImgLabel.grid(row=2)

    requestBloodDonationBtn = Button(HSMaster, text="Request Blood Donation", command=openRequestBloodDonation)
    requestBloodDonationBtn.place(x=20, y=20)

    displayrcpnt = Button(HSMaster, text="Display all recipients", command=opendisplayrecipients)
    displayrcpnt.place(x=20, y=50)

    addentrybutton = Button(HSMaster, text="Donate Blood", command=openAE)
    addentrybutton.place(x=20, y=80)

    displayDonorsBtn = Button(HSMaster, text="Display all donors", command=openDisplayDonor)
    displayDonorsBtn.place(x=20, y=110)

    registerNewHospitalBtn = Button(HSMaster, text="Register a new Hospital", command=openRegisterHosp)
    registerNewHospitalBtn.place(x=20, y=140)

    displayHospitals = Button(HSMaster, text="List of Hospitals", command=opendisplayHospitals)
    displayHospitals.place(x=20, y=170)

    print(donors)


# donate blood window
def donate_blood():
    # TODO: Add a "Associated Hospital" field and respective drop-down menu
    global AEMaster
    AEMaster = Tk()
    AEMaster.geometry("400x300+200+300")
    AEMaster.title("Blood Bank Agency")
    AEMaster.resizable(False, False)
    AEMaster.configure(bg="#FFF")

    global lastUniqueID
    UniqueID = Label(AEMaster, fg="#2c2c2c", bg="#FFF", text="Unique ID :" + str(lastUniqueID + 1), font=("", 13))
    UniqueID.place(x=10, y=30)

    NameLbl = Label(AEMaster, fg="#000000", bg="#FFF", text="First Name: ", font=("", 13))
    NameLbl.place(x=10, y=70)

    NameEntry = Entry(AEMaster, bg="#ffffff", fg="#000000")
    NameEntry.place(x=155, y=75)

    AmntOfBloodLbl = Label(AEMaster, fg="#000000", bg="#FFF", text="Amount of Blood(ml): ", font=("", 11))
    AmntOfBloodLbl.place(x=10, y=100)

    AmntOfBloodEntry = Entry(AEMaster, bg="#ffffff")
    AmntOfBloodEntry.place(x=155, y=105)

    MobileNumLbl = Label(AEMaster, fg="#000000", bg="#FFF", text="Mobile Number: ", font=("", 11))
    MobileNumLbl.place(x=10, y=130)

    MobileNumEntry = Entry(AEMaster, bg="#ffffff", fg="black")
    MobileNumEntry.place(x=155, y=135)

    AddressLbl = Label(AEMaster, fg="#000000", bg="#FFF", text="Address: ", font=("", 11))
    AddressLbl.place(x=10, y=160)

    AddressEntry = Entry(AEMaster, bg="#ffffff", width=35, fg="black")
    AddressEntry.place(x=155, y=165)

    BldGrpLbl = Label(AEMaster, fg="#000000", bg="#FFF", text="Blood Group: ", font=("", 11))
    BldGrpLbl.place(x=10, y=190)

    selected_blood_group = StringVar(AEMaster)
    BloodGroup = ttk.Combobox(AEMaster, textvariable=selected_blood_group, values=blood_groups, width=2,
                              state="readonly")
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
        lastUniqueID + 1, NameEntry.get(), MobileNumEntry.get(), AddressEntry.get(),
        selected_blood_group.get(), AmntOfBloodEntry.get(), int(selected_date.get()),
        selected_month.get(), int(selected_year.get())
    ))
    addEntryBtn.place(x=150, y=260)

    backButton = Button(AEMaster, text="Back", command=lambda: back(AEMaster))
    backButton.place(x=250, y=260)


# req blood donation window
def requestBloodDonation():
    global Rcpmaster
    Rcpmaster = Tk()
    Rcpmaster.geometry("400x300+200+300")
    Rcpmaster.title("Blood Bank Agency")
    Rcpmaster.resizable(False, False)
    Rcpmaster.configure(bg="#FFF")

    UniqueID = Label(Rcpmaster, fg="#2c2c2c", bg="#FFF", text=" Recipient ID :" + str(lastUniqueID + 1), font=("", 13))
    UniqueID.place(x=10, y=30)

    NameLbl = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Recipient Name: ", font=("", 13))
    NameLbl.place(x=10, y=70)

    NameEntry = Entry(Rcpmaster, bg="#ffffff", fg="black")
    NameEntry.place(x=155, y=75)

    AmntOfBloodLbl = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Quantity required(ml): ", font=("", 11))
    AmntOfBloodLbl.place(x=10, y=100)

    AmntOfBloodEntry = Entry(Rcpmaster, bg="#ffffff", fg="black")
    AmntOfBloodEntry.place(x=155, y=105)

    MobileNumLbl = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Mobile Number: ", font=("", 11))
    MobileNumLbl.place(x=10, y=130)

    MobileNumEntry = Entry(Rcpmaster, bg="#ffffff", fg="black")
    MobileNumEntry.place(x=155, y=135)

    HospIdLabel = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Hospital", font=("", 11))
    HospIdLabel.place(x=10, y=160)

    selected_hospital = StringVar(Rcpmaster)
    HospIDDropBox = ttk.Combobox(Rcpmaster, textvariable=selected_hospital, values=hospitals, width=7, state="readonly")
    HospIDDropBox.place(x=155, y=165)

    BldGrpLbl = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Bloodgrp recieved: ", font=("", 11))
    BldGrpLbl.place(x=10, y=190)

    selected_blood_group = StringVar(Rcpmaster)
    BloodGroup = ttk.Combobox(Rcpmaster, textvariable=selected_blood_group, values=blood_groups, width=2,
                              state="readonly")
    BloodGroup.place(x=155, y=190)

    DateLbl = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Date: ", font=("", 11))
    DateLbl.place(x=10, y=220)

    selected_date = StringVar(Rcpmaster)
    DateDrpDown = ttk.Combobox(Rcpmaster, textvariable=selected_date, values=date, width=2, state="readonly")
    DateDrpDown.place(x=155, y=220)

    selected_month = StringVar(Rcpmaster)
    Month = ttk.Combobox(Rcpmaster, textvariable=selected_month, values=month, width=7, state="readonly")
    Month.place(x=215, y=220)

    selected_year = StringVar(Rcpmaster)
    yrdrpdown = ttk.Combobox(Rcpmaster, textvariable=selected_year, values=year, width=5, state="readonly")
    yrdrpdown.place(x=320, y=220)

    requestBlood = Button(Rcpmaster, text="Request Blood", command=lambda: request_Blood(
        UniqueID, NameEntry.get(), AmntOfBloodEntry.get(), MobileNumEntry.get(),
        selected_hospital.get(), selected_blood_group.get(), int(selected_date.get()),
        selected_month.get(), int(selected_year.get())
    ))
    requestBlood.configure(highlightbackground="#000000")
    requestBlood.place(x=150, y=260)

    backButton = Button(Rcpmaster, text="Back", command=lambda: back(Rcpmaster))
    backButton.place(x=250, y=260)


# New hospital registration window
def RegisterNewHopsital():
    global HDmaster
    HDmaster = Tk()
    HDmaster.geometry("400x250+200+300")
    HDmaster.title("Hospital Details")
    HDmaster.resizable(False, False)
    HDmaster.configure(bg="#FFF")

    # options_menu(DEmaster)

    NameLbl = Label(HDmaster, fg="#000000", bg="#FFF", text="hospital ID: ", font=("", 13))
    NameLbl.place(x=10, y=70)

    NameEntry = Entry(HDmaster, bg="#ffffff")
    NameEntry.place(x=180, y=70)

    NameLbl = Label(HDmaster, fg="#000000", bg="#FFF", text="hospitalName: ", font=("", 13))
    NameLbl.place(x=10, y=100)

    hspNameEntry = Entry(HDmaster, bg="#ffffff")
    hspNameEntry.place(x=180, y=105)

    NameLbl = Label(HDmaster, fg="#000000", bg="#FFF", text="Contact Person Name: ", font=("", 13))
    NameLbl.place(x=10, y=130)

    contctNameEntry = Entry(HDmaster, bg="#ffffff")
    contctNameEntry.place(x=180, y=135)

    NameLbl = Label(HDmaster, fg="#000000", bg="#FFF", text="Contact number: ", font=("", 13))
    NameLbl.place(x=10, y=160)

    cntctnumEntry = Entry(HDmaster, bg="#ffffff")
    cntctnumEntry.place(x=180, y=165)

    Proceedbtn = Button(HDmaster, text="Proceed", command=lambda: Proceed_btn(
        NameEntry.get(), hspNameEntry.get(), contctNameEntry.get(),
        int(cntctnumEntry.get())
    ))
    Proceedbtn.configure(highlightbackground="#000000")
    Proceedbtn.place(x=150, y=200)

    backBtn = Button(HDmaster, text="Back", command=lambda: back(HDmaster))
    backBtn.place(x=250, y=200)


def openAE():
    HSMaster.destroy()
    donate_blood()


def openDisplayDonor():
    HSMaster.destroy()
    testDisplayDonors()


def openRegisterHosp():
    HSMaster.destroy()
    RegisterNewHopsital()


def openRequestBloodDonation():
    HSMaster.destroy()
    requestBloodDonation()


def opendisplayrecipients():
    HSMaster.destroy()
    displayrecipients()


def opendisplayHospitals():
    HSMaster.destroy()
    displayHospitals()


def Proceed_btn(Name, hspname, cntctname, Mobile):
    hospitals.append([str(Name), str(hspname), str(cntctname), int(Mobile)])


def add_entry(Id, Name, Mobile, Address, Blood_Group, Quantity, Date, Month, Year):
    donors.append([Id, str(Name), Mobile, Address, Blood_Group, Quantity, [Date, Month, Year]])
    global lastUniqueID
    lastUniqueID += 1


def request_Blood(Id, Name, Mobile, Address, Blood_Group, Quantity, Date, Month, Year):
    Recipients.append([Id, str(Name), Mobile, Address, Blood_Group, Quantity, [Date, Month, Year]])


def testDisplayDonors():
    global TDDMaster
    TDDMaster = Tk()
    TDDMaster.geometry("500x300+200+300")
    TDDMaster.title("Blood Bank Agency")
    TDDMaster.resizable(False, False)
    TDDMaster.configure(bg="#FFF")

    choice = StringVar(TDDMaster)
    testBox = ttk.Combobox(TDDMaster, textvariable=choice, values=["Browse", "Search"], width=4, state="readonly")
    testBox.pack()
    testBox.bind("<<ComboboxSelected>>", function)

    btn = Button(TDDMaster, text="")


def function(event):
    CmBox = event.widget.get()
    global lbl
    lbl = Label(TDDMaster, text=CmBox)
    lbl.pack()


def displayDonors():
    global DDMaster
    DDMaster = Tk()
    DDMaster.geometry("500x300+200+300")
    DDMaster.title("Blood Bank Agency")
    DDMaster.resizable(False, False)
    DDMaster.configure(bg="#FFF")

    titleLabel = Label(DDMaster, text="List of All donors")
    titleLabel.pack()

    ID_label = Label(DDMaster, text="Id")
    ID_label.place(x=20, y=45)

    Name_label = Label(DDMaster, text="Name")
    Name_label.place(x=95, y=45)

    donorsIDList = Listbox(DDMaster, width=5)
    donorsIDList.place(x=10, y=70)
    for donor in donors:
        donorsIDList.insert(END, donor[ID])

    donorsNameList = Listbox(DDMaster, width=15)
    donorsNameList.place(x=50, y=70)
    for donor in donors:
        donorsNameList.insert(END, donor[NAME])

    donorsPhoneNumberList = Listbox(DDMaster, width=9)
    donorsPhoneNumberList.place(x=185, y=70)
    for donor in donors:
        donorsPhoneNumberList.insert(END, donor[PHONE_NUM])

    backBtn = Button(DDMaster, text="Back", command=lambda: back(DDMaster))
    backBtn.pack()


def displayrecipients():
    global DRMaster
    DRMaster = Tk()
    DRMaster.geometry("400x300+200+300")
    DRMaster.title("Blood Bank Agency")
    DRMaster.resizable(False, False)
    DRMaster.configure(bg="#FFF")

    titleLabel = Label(DRMaster, text="List of All Recipients")
    titleLabel.pack()

    global RecipientList
    RecipientList = Listbox(DRMaster, width=12)
    for Recipient in Recipients:
        RecipientList.insert(END, str(Recipient[NAME]))
    RecipientList.pack()

    backBtn = Button(DRMaster, text="Back", command=lambda: back(DRMaster))
    backBtn.pack()


def displayHospitals():
    global HDMaster
    HDMaster = Tk()
    HDMaster.geometry("400x300+200+300")
    HDMaster.title("Blood Bank Agency")
    HDMaster.resizable(False, False)
    HDMaster.configure(bg="#FFF")

    titleLabel = Label(HDMaster, text="List of All Registered hospitals")
    titleLabel.pack()

    global hospitalList
    hospitalList = Listbox(HDMaster, width=50)
    for hospital in hospitals:
        hospitalList.insert(END, hospital)
    hospitalList.pack()

    backBtn = Button(HDMaster, text="Back", command=lambda: back(HDMaster))
    backBtn.pack()


def back(_from):
    _from.destroy()
    HomeScreen()


HomeScreen()

mainloop()
