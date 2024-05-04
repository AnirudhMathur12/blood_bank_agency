"""#2c2c2c-greybg  #ff2400-red, text"""

from tkinter import *
from tkinter import ttk
import mysql.connector as cnctr
import os

# giving index numbers their own variable so it will be easier to call them and refer to them in code

NAME = 0
PHONE_NUM = 1
ADDRESS = 2
BLOOD_GROUP = 3
QTY = 4
DATE = 5


# format:
#    ID, name, phone number, address, blood group, quantity, date donated
blood_groups = {
    "A+": 0,
    "A-": 0,
    "B+": 0,
    "B-": 0,
    "O+": 0,
    "O-": 0,
    "AB+": 0,
    "AB-": 0,
}

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

year = []

date = []

hospitals = [[1, "Apollo", "Anirudh", 1234]]

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
    print(blood_groups)
    global HSMaster
    HSMaster = Tk()
    HSMaster.geometry("500x400+200+300")
    HSMaster.title("Blood Bank Agency")
    HSMaster.resizable(False, False)
    HSMaster.configure(bg="#FFF")

    canvas = Canvas(HSMaster, width=500, height=400)
    canvas.pack()

    img = PhotoImage(file="bg.png")
    bg_label = Label(HSMaster, image=img)
    # bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.place()

    requestBloodDonationBtn = Button(
        HSMaster,
        text="Request Blood Donation",
        command=lambda: open(requestBloodDonation),
    )
    requestBloodDonationBtn.place(x=20, y=20)

    displayrcpnt = Button(
        HSMaster, text="Display all recipients", command=lambda: open(displayrecipients)
    )
    displayrcpnt.place(x=20, y=50)

    addentrybutton = Button(
        HSMaster, text="Donate Blood", command=lambda: open(donate_blood)
    )
    addentrybutton.place(x=20, y=80)

    displayDonorsBtn = Button(
        HSMaster, text="Display all donors", command=lambda: open(DisplayDonors)
    )
    displayDonorsBtn.place(x=20, y=110)

    registerNewHospitalBtn = Button(
        HSMaster,
        text="Register a new Hospital",
        command=lambda: open(RegisterNewHopsital),
    )
    registerNewHospitalBtn.place(x=20, y=140)

    displayHospitals = Button(
        HSMaster, text="List of Hospitals", command=lambda: open(DisplayHospitals)
    )
    displayHospitals.place(x=20, y=170)

    logoutButton = Button(HSMaster, text="Logout", command=logout)
    logoutButton.place(x=20, y=350)


def logout():
    HSMaster.destroy()
    LoginScreen()


def LoginScreen():
    global LSMaster
    LSMaster = Tk()
    LSMaster.geometry("300x150+200+300")
    LSMaster.resizable(False, False)
    LSMaster.configure(bg="#FFF")
    UsrNameLabel = Label(
        LSMaster, text="Username: ", fg="black", bg="white", font=("", 15)
    )
    UsrNameLabel.place(x=10, y=10)
    UsrNameField = Entry(LSMaster, bg="#ffffff", fg="#000000")
    UsrNameField.place(x=100, y=10)
    PssWrdLabel = Label(
        LSMaster, text="Password: ", fg="black", bg="white", font=("", 15)
    )
    PssWrdLabel.place(x=10, y=50)
    PssWrdField = Entry(LSMaster, bg="#ffffff", fg="#000000", show="*")
    PssWrdField.place(x=100, y=50)
    LoginButton = Button(
        LSMaster,
        text="Login",
        command=lambda: Login(UsrNameField.get(), PssWrdField.get(), LSMaster),
    )
    LoginButton.place(x=10, y=100)
    SignUpButton = Button(LSMaster, text="Sign Up", command=SignUpScreen)
    SignUpButton.place(x=150, y=100)


def Login(Username, Password, Master):
    login_connection = cnctr.connect(
        host="localhost", user="root", password="", db="BloodBankAgency"
    )
    cur = login_connection.cursor()
    cur.execute("SHOW TABLES")
    result = cur.fetchall()
    cur.execute(
        "SELECT UserID FROM Login_CredentialsBBA WHERE Username = %s AND Password = %s",
        (Username, Password),
    )
    result = cur.fetchall()
    if len(result) == 1:
        cur.close()
        Master.destroy()
        HomeScreen()
    elif len(result) > 1:
        MessageBox("Fatal Error. Please use a different login")
    elif len(result) == 0:
        MessageBox("Password is wrong or Username doesn't exist")


def SignUpScreen():
    LSMaster.destroy()
    global SUMaster
    SUMaster = Tk()
    SUMaster.geometry("300x150+200+300")
    SUMaster.resizable(False, False)
    SUMaster.configure(bg="#FFF")
    UsrNameLabel = Label(
        SUMaster, text="Username: ", fg="black", bg="white", font=("", 15)
    )
    UsrNameLabel.place(x=10, y=10)
    UsrNameField = Entry(SUMaster, bg="#ffffff", fg="#000000")
    UsrNameField.place(x=100, y=10)
    PssWrdLabel = Label(
        SUMaster, text="Password: ", fg="black", bg="white", font=("", 15)
    )
    PssWrdLabel.place(x=10, y=50)
    PssWrdField = Entry(SUMaster, bg="#ffffff", fg="#000000", show="*")
    PssWrdField.place(x=100, y=50)
    LoginButton = Button(
        SUMaster,
        text="Sign Up",
        command=lambda: SignUp(UsrNameField.get(), PssWrdField.get()),
    )
    LoginButton.place(x=10, y=100)


def SignUp(username, password):
    table_name = "Login_CredentialsBBA"
    """
    username_file = open('usernames.txt', 'r')
    str = username_file.read()
    usernames = str.split("\n")
    if username in usernames:
        MessageBox("Username already exists!")
        return
    username_file = open('usernames.txt', 'a')
    username_file.write(username + "\n")
    password_file = open('passwords.txt', 'a')
    password_file.write(password+'\n')
    LoginScreen()
    SUMaster.destroy()
    """
    signup_connection = cnctr.connect(
        host="localhost", user="root", password="", db="BloodBankAgency"
    )
    cur = signup_connection.cursor()
    cur.execute("SHOW TABLES")
    result = cur.fetchall()
    cur.execute("SELECT * FROM Login_CredentialsBBA WHERE Username = %s", (username,))
    result = cur.fetchall()
    if len(result) != 0:
        MessageBox("Username is already in use.")
    else:
        cur.execute(
            "INSERT INTO Login_CredentialsBBA (Username, Password) VALUES(%s, %s)",
            (username, password),
        )
        cur.execute("commit")
    cur.close()
    LoginScreen()
    SUMaster.destroy()


# donate blood window
def donate_blood():
    # TODO: Add a "Associated Hospital" field and respective drop-down menu
    global AEMaster
    AEMaster = Tk()
    AEMaster.geometry("400x300+200+300")
    AEMaster.title("Blood Bank Agency")
    AEMaster.resizable(False, False)
    AEMaster.configure(bg="#FFF")

    NameLbl = Label(
        AEMaster, fg="#000000", bg="#FFF", text="First Name: ", font=("", 13)
    )
    NameLbl.place(x=10, y=70)

    NameEntry = Entry(AEMaster, bg="#ffffff", fg="#000000")
    NameEntry.place(x=155, y=75)

    AmntOfBloodLbl = Label(
        AEMaster, fg="#000000", bg="#FFF", text="Amount of Blood(ml): ", font=("", 11)
    )
    AmntOfBloodLbl.place(x=10, y=100)

    AmntOfBloodEntry = Entry(AEMaster, bg="#ffffff")
    AmntOfBloodEntry.place(x=155, y=105)

    MobileNumLbl = Label(
        AEMaster, fg="#000000", bg="#FFF", text="Mobile Number: ", font=("", 11)
    )
    MobileNumLbl.place(x=10, y=130)

    MobileNumEntry = Entry(AEMaster, bg="#ffffff", fg="black")
    MobileNumEntry.place(x=155, y=135)

    Asch = Label(
        AEMaster, fg="#000000", bg="#FFF", text="Asociated hospitals: ", font=("", 11)
    )
    Asch.place(x=10, y=40)

    Asociated_hospitals = StringVar(AEMaster)
    hospnames = []
    for i in hospitals:
        hospnames.append(i[1])
    Associated_Hospitals = ttk.Combobox(
        AEMaster,
        textvariable=Asociated_hospitals,
        values=hospnames,
        width=5,
        state="readonly",
    )
    Associated_Hospitals.place(x=155, y=40)

    BldGrpLbl = Label(
        AEMaster, fg="#000000", bg="#FFF", text="Blood Group: ", font=("", 11)
    )
    BldGrpLbl.place(x=10, y=190)

    selected_blood_group = StringVar(AEMaster)
    BloodGroup = ttk.Combobox(
        AEMaster,
        textvariable=selected_blood_group,
        values=list(blood_groups.keys()),
        width=2,
        state="readonly",
    )
    BloodGroup.place(x=155, y=190)

    DateLbl = Label(AEMaster, fg="#000000", bg="#FFF", text="Date: ", font=("", 11))
    DateLbl.place(x=10, y=220)

    addEntryBtn = Button(
        AEMaster,
        text="Add Entry",
        command=lambda: add_entry(
            NameEntry.get(),
            MobileNumEntry.get(),
            selected_blood_group.get(),
            AmntOfBloodEntry.get(),
        ),
    )
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

    NameLbl = Label(
        Rcpmaster, fg="#000000", bg="#FFF", text="Recipient Name: ", font=("", 13)
    )
    NameLbl.place(x=10, y=70)

    NameEntry = Entry(Rcpmaster, bg="#ffffff", fg="black")
    NameEntry.place(x=155, y=75)

    AmntOfBloodLbl = Label(
        Rcpmaster,
        fg="#000000",
        bg="#FFF",
        text="Quantity required(ml): ",
        font=("", 11),
    )
    AmntOfBloodLbl.place(x=10, y=100)

    AmntOfBloodEntry = Entry(Rcpmaster, bg="#ffffff", fg="black")
    AmntOfBloodEntry.place(x=155, y=105)

    MobileNumLbl = Label(
        Rcpmaster, fg="#000000", bg="#FFF", text="Mobile Number: ", font=("", 11)
    )
    MobileNumLbl.place(x=10, y=130)

    MobileNumEntry = Entry(Rcpmaster, bg="#ffffff", fg="black")
    MobileNumEntry.place(x=155, y=135)

    HospIdLabel = Label(
        Rcpmaster, fg="#000000", bg="#FFF", text="Hospital", font=("", 11)
    )
    HospIdLabel.place(x=10, y=160)

    selected_hospital = StringVar(Rcpmaster)
    hspnames = []
    for i in hospitals:
        hspnames.append(i[1])
    HospIDDropBox = ttk.Combobox(
        Rcpmaster,
        textvariable=selected_hospital,
        values=hspnames,
        width=7,
        state="readonly",
    )
    HospIDDropBox.place(x=155, y=165)

    BldGrpLbl = Label(
        Rcpmaster, fg="#000000", bg="#FFF", text="Bloodgrp recieved: ", font=("", 11)
    )
    BldGrpLbl.place(x=10, y=190)

    selected_blood_group = StringVar(Rcpmaster)
    BloodGroup = ttk.Combobox(
        Rcpmaster,
        textvariable=selected_blood_group,
        values=list(blood_groups.keys()),
        width=2,
        state="readonly",
    )
    BloodGroup.place(x=155, y=190)

    DateLbl = Label(Rcpmaster, fg="#000000", bg="#FFF", text="Date: ", font=("", 11))
    DateLbl.place(x=10, y=220)

    selected_date = StringVar(Rcpmaster)
    DateDrpDown = ttk.Combobox(
        Rcpmaster, textvariable=selected_date, values=date, width=2, state="readonly"
    )
    DateDrpDown.place(x=155, y=220)

    selected_month = StringVar(Rcpmaster)
    Month = ttk.Combobox(
        Rcpmaster, textvariable=selected_month, values=month, width=7, state="readonly"
    )
    Month.place(x=215, y=220)

    selected_year = StringVar(Rcpmaster)
    yrdrpdown = ttk.Combobox(
        Rcpmaster, textvariable=selected_year, values=year, width=5, state="readonly"
    )
    yrdrpdown.place(x=320, y=220)

    requestBlood = Button(
        Rcpmaster,
        text="Request Blood",
        command=lambda: request_Blood(
            NameEntry.get(),
            int(AmntOfBloodEntry.get()),
            MobileNumEntry.get(),
            selected_hospital.get(),
            selected_blood_group.get(),
            int(selected_date.get()),
            selected_month.get(),
            int(selected_year.get()),
        ),
    )
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

    NameLbl = Label(
        HDmaster, fg="#000000", bg="#FFF", text="hospitalName: ", font=("", 13)
    )
    NameLbl.place(x=10, y=100)

    hspNameEntry = Entry(HDmaster, bg="#ffffff")
    hspNameEntry.place(x=180, y=105)

    ContactNameLbl = Label(
        HDmaster, fg="#000000", bg="#FFF", text="Contact Person Name: ", font=("", 13)
    )
    ContactNameLbl.place(x=10, y=130)

    contctNameEntry = Entry(HDmaster, bg="#ffffff")
    contctNameEntry.place(x=180, y=135)

    cntctNamelbl = Label(
        HDmaster, fg="#000000", bg="#FFF", text="Contact number: ", font=("", 13)
    )
    cntctNamelbl.place(x=10, y=160)

    cntctnumEntry = Entry(HDmaster, bg="#ffffff")
    cntctnumEntry.place(x=180, y=165)

    Proceedbtn = Button(
        HDmaster,
        text="Proceed",
        command=lambda: add_hosp(
            hspNameEntry.get(),
            contctNameEntry.get(),
            int(cntctnumEntry.get()),
            HDmaster,
        ),
    )
    Proceedbtn.configure(highlightbackground="#000000")
    Proceedbtn.place(x=150, y=200)

    backBtn = Button(HDmaster, text="Back", command=lambda: back(HDmaster))
    backBtn.place(x=250, y=200)


def MessageBox(Message):
    psmsg = Tk()
    psmsg.geometry("200x100+200+300")
    psmsg.resizable(False, False)
    psmsg.configure(bg="#FFF")
    psmsg.after(1, lambda: psmsg.focus_force())
    NameLbl = Label(psmsg, fg="#000000", bg="#FFF", text=Message, font=("", 13))
    NameLbl.pack(anchor=N)
    OkButton = Button(psmsg, text="Okay", command=lambda: psmsg.destroy())
    OkButton.place(x=60, y=60)


def open(fn):
    HSMaster.destroy()
    fn()


def add_hosp(hspname, cntctname, Mobile, Master):
    con = cnctr.connect(
        host="localhost", user="root", password="", db="BloodBankAgency"
    )
    cur = con.cursor()
    cur.execute(
        "INSERT INTO HospitalsBBA(Name, Representative, Mobile) VALUES(%s, %s, %s)",
        (hspname, cntctname, Mobile),
    )
    cur.execute("commit")
    cur.close()
    MessageBox("Success!")
    back(Master)


def add_entry(Name, Mobile, Blood_Group, Quantity, Master):
    con = cnctr.connect(
        host="localhost", user="root", password="", db="BloodBankAgency"
    )
    cur = con.cursor()
    cur.execute(
        "INSERT INTO Donated_BloodBBA(Name, Mobile, BloodGroup, Quantity, Date) VALUES(%s, %s, %s, %s, NOW())",
        (Name, Mobile, Blood_Group, Quantity),
    )
    cur.execute(
        "UPDATE Blood_GroupsBBA SET Amount = Amount + %s WHERE TYPE = %s",
        (Quantity, Blood_Group),
    )
    cur.execute("commit")
    MessageBox("Success!")
    cur.close()
    back(Master)


def request_Blood(Name, amntofbld, mobilenum, hosp, bldgrp, Date, Month, Year):
    con = cnctr.connect(
        host="localhost", user="root", password="", db="BloodBankAgency"
    )
    cur = con.cursor()
    cur.execute("SELECT Amount FROM Blood_GroupsBBA WHERE Type = %s", (bldgrp,))
    result = cur.fetchall()
    if result[0][0] < amntofbld:
        MessageBox("Enough blood not available!")
        back(Rcpmaster)
        return
    cur.execute(
        "INSERT INTO RequestsBBA(Name, Quantity, Mobile, BloodGroup, Date) VALUES(%s, %s, %s, %s, NOW())",
        (Name, amntofbld, mobilenum, bldgrp),
    )
    cur.execute(
        "UPDATE Blood_GroupsBBA SET Amount = Amount - %s WHERE TYPE = %s",
        (amntofbld, bldgrp),
    )
    cur.execute("commit")
    cur.close()
    MessageBox("Success!")
    back(Rcpmaster)


def DisplayDonors():
    global DDMaster
    DDMaster = Tk()
    DDMaster.geometry("500x300+200+300")
    DDMaster.title("Blood Bank Agency")
    DDMaster.resizable(False, False)
    DDMaster.configure(bg="#FFF")
    frame = Frame(DDMaster)
    frame.pack()
    backBtn = Button(DDMaster, text="Back", command=lambda: back(DDMaster))
    backBtn.pack(anchor=S)

    con = cnctr.connect(
        host="localhost", user="root", password="", db="BloodBankAgency"
    )
    cur = con.cursor()
    cur.execute("SELECT DonorID, Name FROM Donated_BloodBBA")
    result = cur.fetchall()

    lst = Listbox(frame, width=20)
    for i in result:
        _str = "ID: " + str(i[0]) + " Name: " + str(i[1])
        lst.insert(END, _str)
    lst.pack()
    if lst.size() != 0:
        btn = Button(frame, text="Access", command=lambda: fn(lst))
        btn.pack()


def fn(lst):
    donorID = lst.get(lst.curselection()[0]).split()[1]
    con = cnctr.connect(
        host="localhost", user="root", password="", db="BloodBankAgency"
    )
    print(donorID)

    cur = con.cursor()
    cur.execute("SELECT * FROM Donated_BloodBBA WHERE DonorID = %s", (donorID,))
    result = cur.fetchall()
    print(result)
    cur.close()

    global DATAMaster
    DATAMaster = Tk()
    DATAMaster.geometry("350x150+200+300")
    DATAMaster.title(result[0][1])
    DATAMaster.resizable(False, False)
    DDMaster.configure(bg="#FFF")

    nameLabel = Label(DATAMaster, text="Name:")
    nameLabel.grid(row=0, column=0, sticky="w")
    _nameLabel = Label(DATAMaster, text=result[0][1])
    _nameLabel.grid(row=0, column=1, sticky="w")

    phonenumLabel = Label(DATAMaster, text="Phone Number:")
    phonenumLabel.grid(row=1, column=0, sticky="w")
    _phonenumLabel = Label(DATAMaster, text=result[0][2])
    _phonenumLabel.grid(row=1, column=1, sticky="w")

    bldgrpLabel = Label(DATAMaster, text="Blood Group:")
    bldgrpLabel.grid(row=2, column=0, sticky="w")
    _bdlgrpLabel = Label(DATAMaster, text=result[0][3])
    _bdlgrpLabel.grid(row=2, column=1, sticky="w")

    qtyLabel = Label(DATAMaster, text="Quantity:")
    qtyLabel.grid(row=2, column=2, sticky="w")
    _qtyLabel = Label(DATAMaster, text=result[0][4])
    _qtyLabel.grid(row=2, column=3, sticky="w")

    deleteEntryBtn = Button(
        DATAMaster,
        text="Delete Entry",
        command=lambda: remove_entry(
            donorID, "Donated_BloodBBA", "DonorID", DisplayDonors, DDMaster, DATAMaster
        ),
    )
    deleteEntryBtn.grid(row=4, column=0)


def remove_entry(index, db, indexname, fn, Master, self):
    con = cnctr.connect(
        host="localhost", user="root", password="", db="BloodBankAgency"
    )
    cur = con.cursor()
    cur.execute("DELETE FROM " + db + " WHERE " + indexname + "=%s", (index,))
    cur.execute("commit")
    cur.close()
    Master.destroy()
    fn()
    self.destroy()


def displayrecipients():
    print(hospitals)
    global DRMaster
    DRMaster = Tk()
    DRMaster.geometry("500x300+200+300")
    DRMaster.title("Blood Bank Agency")
    DRMaster.resizable(False, False)
    DRMaster.configure(bg="#FFF")
    frame = Frame(DRMaster)
    frame.pack()
    backBtn = Button(DRMaster, text="Back", command=lambda: back(DRMaster))
    backBtn.pack(anchor=S)

    con = cnctr.connect(
        host="localhost", user="root", password="", db="BloodBankAgency"
    )
    cur = con.cursor()
    cur.execute("SELECT RequestID, Name FROM RequestsBBA")
    result = cur.fetchall()

    lst = Listbox(frame, width=20)
    for i in result:
        _str = "ID: " + str(i[0]) + " Name: " + str(i[1])
        lst.insert(END, _str)
    lst.pack()
    if lst.size() != 0:
        btn = Button(frame, text="Access", command=lambda: fn_forRecipient(lst))
        btn.pack()


def fn_forRecipient(lst):
    requestID = lst.get(lst.curselection()[0]).split()[1]
    con = cnctr.connect(
        host="localhost", user="root", password="", db="BloodBankAgency"
    )
    print(requestID)

    cur = con.cursor()
    cur.execute("SELECT * FROM RequestsBBA WHERE RequestID = %s", (requestID,))
    result = cur.fetchall()
    print("result", result)
    cur.close()

    global DHMaster
    DHMaster = Tk()
    DHMaster.geometry("350x150+200+300")
    DHMaster.title(result[0][1])
    DHMaster.resizable(False, False)
    # DATAMaster.configure(bg="black")

    nameLabel = Label(DHMaster, text="Name:")
    nameLabel.grid(row=0, column=0, sticky="w")
    _nameLabel = Label(DHMaster, text=result[0][1])
    _nameLabel.grid(row=0, column=1, sticky="w")

    amntbldlabel = Label(DHMaster, text="Blood Requested:")
    amntbldlabel.grid(row=1, column=0, sticky="w")
    _amntbldlabel = Label(DHMaster, text=result[0][2])
    _amntbldlabel.grid(row=1, column=1, sticky="w")

    hsplabel = Label(DHMaster, text="Contact Number:")
    hsplabel.grid(row=2, column=2, sticky="w")
    _hsplabel = Label(DHMaster, text=result[0][3])
    _hsplabel.grid(row=2, column=3, sticky="w")

    bldgrplabel = Label(DHMaster, text="Blood Group:")
    bldgrplabel.grid(row=2, column=0, sticky="w")
    _bldgrplabel = Label(DHMaster, text=result[0][4])
    _bldgrplabel.grid(row=2, column=1, sticky="w")

    deleteEntryBtn = Button(
        DHMaster,
        text="Delete Entry",
        command=lambda: remove_entry(
            requestID, "RequestsBBA", "RequestID", displayrecipients, DRMaster, DHMaster
        ),
    )
    deleteEntryBtn.grid(row=4, column=0)


def DisplayHospitals():
    print(hospitals)
    global DHMaster
    DHMaster = Tk()
    DHMaster.geometry("500x300+200+300")
    DHMaster.title("Blood Bank Agency")
    DHMaster.resizable(False, False)
    DHMaster.configure(bg="#FFF")
    frame = Frame(DHMaster)
    frame.pack()
    backBtn = Button(DHMaster, text="Back", command=lambda: back(DHMaster))
    backBtn.pack(anchor=S)

    con = cnctr.connect(
        host="localhost", user="root", password="", db="BloodBankAgency"
    )
    cur = con.cursor()
    cur.execute("SELECT HospitalID, Name FROM HospitalsBBA")
    result = cur.fetchall()

    lst = Listbox(frame, width=20)
    for i in result:
        _str = "ID: " + str(i[0]) + " Name: " + str(i[1])
        lst.insert(END, _str)
    lst.pack()
    if lst.size() != 0:
        btn = Button(frame, text="Access", command=lambda: fn_forhosp(lst))
        btn.pack()


def fn_forhosp(lst):
    hospitalID = lst.get(lst.curselection()[0]).split()[1]
    con = cnctr.connect(
        host="localhost", user="root", password="", db="BloodBankAgency"
    )
    print(hospitalID)

    cur = con.cursor()
    cur.execute("SELECT * FROM HospitalsBBA WHERE HospitalID = %s", (hospitalID,))
    result = cur.fetchall()
    cur.close()

    global DHoMaster
    DHoMaster = Tk()
    DHoMaster.geometry("350x150+200+300")
    DHoMaster.title(result[0][1])
    DHoMaster.resizable(False, False)
    # DHoMaster.configure(bg="black")

    nameLabel = Label(DHoMaster, text="Name:")
    nameLabel.grid(row=0, column=0, sticky="w")
    _nameLabel = Label(DHoMaster, text=result[0][1])
    _nameLabel.grid(row=0, column=1, sticky="w")

    reprLabel = Label(DHoMaster, text="Representative:")
    reprLabel.grid(row=2, column=0, sticky="w")
    _reprLabel = Label(DHoMaster, text=result[0][2])
    _reprLabel.grid(row=2, column=1, sticky="w")

    phnumlabel = Label(DHoMaster, text="Contact Number:")
    phnumlabel.grid(row=2, column=2, sticky="w")
    _phnumlabel = Label(DHoMaster, text=result[0][3])
    _phnumlabel.grid(row=2, column=3, sticky="w")

    deleteEntryBtn = Button(
        DHoMaster,
        text="Delete Entry",
        command=lambda: remove_entry(
            hospitalID,
            "HospitalsBBA",
            "HospitalID",
            DisplayHospitals,
            DHMaster,
            DHoMaster,
        ),
    )
    deleteEntryBtn.grid(row=4, column=0)


def remove_for_hosp(hosp_name, fn, Master, self):
    for i in hospitals:
        if hosp_name in i:
            hospitals.remove(i)
            break
    print(hospitals)
    Master.destroy()
    fn()
    self.destroy()


def back(_from):
    _from.destroy()
    HomeScreen()


def SQL_INIT():
    con = cnctr.connect(host="localhost", user="root", password="")
    cur = con.cursor()
    cur.execute("SHOW DATABASES")
    result = cur.fetchall()
    print(result)
    if ("BloodBankAgency",) not in result:
        cur.execute("CREATE DATABASE BloodBankAgency")
    cur.execute("USE BloodBankAgency")
    cur.execute("SHOW TABLES")
    result = cur.fetchall()
    if ("Blood_GroupsBBA",) not in result:
        cur.execute(
            "CREATE TABLE Blood_GroupsBBA(Type VARCHAR(5) PRIMARY KEY, Amount INT NOT NULL DEFAULT 0)"
        )
        cur.execute(
            "INSERT INTO Blood_GroupsBBA(Type) VALUES('A+'), ('A-'), ('B+'), ('B-'), ('AB+'), ('AB-'), ('O+'), ('O-')"
        )
    if ("Login_CredentialsBBA",) not in result:
        cur.execute(
            "CREATE TABLE Login_CredentialsBBA(UserID INT AUTO_INCREMENT PRIMARY KEY, Username VARCHAR(50), Password VARCHAR(50))"
        )
    if ("HospitalsBBA",) not in result:
        cur.execute(
            "CREATE TABLE HospitalsBBA(HospitalID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(30), Representative VARCHAR(30), Mobile BIGINT)"
        )
    if ("RequestsBBA",) not in result:
        cur.execute(
            "CREATE TABLE RequestsBBA(RequestID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(30), Quantity INT, Mobile BIGINT, BloodGroup VARCHAR(5), Date DATE)"
        )
    if ("Donated_BloodBBA",) not in result:
        cur.execute(
            "CREATE TABLE Donated_BloodBBA(DonorID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(30), Mobile BIGINT, BloodGroup VARCHAR(5), Quantity INT, Date DATE)"
        )

    cur.execute("commit")
    cur.close()


os.system("mysql.server start")
SQL_INIT()
# LoginScreen()
# requestBloodDonation()
HomeScreen()
mainloop()
os.system("mysql.server stop")
