#Python 3.10.6 or a newer Version is required
import csv
import hashlib
from datetime import date


#To switch the user 
def SwitchUser(level,ID):
    match level:
        case 0:
            AdminController()
        case 1:
            DoctorController()
        case 2:
            NurseController()
        case 3:
            PharmacistController()
        case 4:
            PatientController(ID)
        case _:
            print("Invalid User Name or PassWord\n")

#To get the Drug Details
def getDrugDetails(ID):
    with open('DrugDetails.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            if(int(row['ID'])==ID):
                print(row)
            else: continue

#To get the Sickness Details
def getSickDetails(ID):
    with open('SicknessDetails.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            if(int(row['ID'])==ID):
                print(row)
            else: continue

#To get the Lab Test Details
def getLabDetails(ID):
    with open('Labtest.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            if(int(row['ID'])==ID):
                print(row)
            else: continue

# To Get all the patient Details at once
def getAllPatientDetails():
    ID = getUserID()
    getLabDetails(ID)
    getSickDetails(ID)
    getDrugDetails(ID)
    getPatientDetails(ID)

# to get usr details for login
def getUserdetails():
    name = str(input("Enter UserName: "))
    pwd = str(input("Enter Password: "))
    result = hashlib.md5(pwd.encode())
    password = result.hexdigest()
    with open('UserDetails.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            if(row['UserName']==name and row['password']!=password):
                print("Invalid User Name or PassWord\n")
            elif(row['UserName']==name and row['password']==password):
                SwitchUser(int(row['level']),int(row['ID']))
            else: continue
        
# to get the user id
def getUserID():
    name = str(input("Enter Patient Name : "))
    with open('PersonalDetails.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            if(row['Name']==name):
                return int(row['ID'])
            else: continue
    return 0

# to get the total user count    
def getUserCount():
    with open('UserDetails.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        count = 0
        for row in csvreader:
            count+=1
        return count+1

# to add a new doctor to the system
def addDoctor():
    name = str(input("Enter Doctor Name: "))
    pwd = str(input("Enter Password: "))
    Utype = "DOCTOR"
    Privilege = 1
    result = hashlib.md5(pwd.encode())
    password = result.hexdigest()
    ID  = getUserCount()
    with open('UserDetails.csv', 'a') as file:
        data = [ID,name,password,Utype,Privilege]
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)
        print("New Doctor Added")

#
def addAdmin():
    name = str(input("Enter Admin Name: "))
    pwd = str(input("Enter Password: "))
    Utype = "ADMIN"
    Privilege = 0
    result = hashlib.md5(pwd.encode())
    password = result.hexdigest()
    ID  = getUserCount()
    with open('UserDetails.csv', 'a') as file:
        data = [ID,name,password,Utype,Privilege]
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)

#to add sickness details
def addSickDetails():
    ID = getUserID()
    if (ID>0):
        sick = str(input("Sickness Details : "))
        with open('SicknessDetails.csv', 'a') as file:
            data = [ID,sick]
            csv_writer = csv.writer(file)
            csv_writer.writerow(data)
            print("Details Added")
    else: print("Invalid patient")

# to add drug prescriptions
def addDrugDetails():
    ID = getUserID()
    if (ID>0):
        drug = str(input("Enter Drug : "))
        details = str(input("Enter Details : "))
        with open('DrugDetails.csv', 'a') as file:
            data = [ID,drug,details]
            csv_writer = csv.writer(file)
            csv_writer.writerow(data)
            print("Details Added")
    else: print("Invalid patient")

# to add Lab test details
def addLabTestDetails():
    ID = getUserID()
    if (ID>0):
        today = date.today()
        tests = str(input("Test : "))
        results = str(input("Results : "))
        with open('Labtest.csv', 'a') as file:
            data = [ID,tests,results,today]
            csv_writer = csv.writer(file)
            csv_writer.writerow(data)
            print("Details Added")
    else: print("Invalid patient")

#to add a new nurse
def addNurse():
    name = str(input("Enter Nurse Name: "))
    pwd = str(input("Enter Password: "))
    Utype = "NURSE"
    Privilege = 2
    result = hashlib.md5(pwd.encode())
    password = result.hexdigest()
    ID  = getUserCount()
    with open('UserDetails.csv', 'a') as file:
        data = [ID,name,password,Utype,Privilege]
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)
        print("New Nurse Added")

#to add a new Pharmacist
def addPharmacist():
    name = str(input("Enter Pharmacist Name: "))
    pwd = str(input("Enter Password: "))
    Utype = "Pharmacist"
    Privilege = 3
    result = hashlib.md5(pwd.encode())
    password = result.hexdigest()
    ID  = getUserCount()
    with open('UserDetails.csv', 'a') as file:
        data = [ID,name,password,Utype,Privilege]
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)
        print("New Pharmacist Added")

#to add persional details of patient
def addPatientDetails(ID,name):
    age = str(input("Enter Patient Age: "))
    phoneNo = str(input("Enter Phone Number: "))
    address = str(input("Enter Address: "))
    with open('PersonalDetails.csv', 'a') as file:
        data = [ID,name,phoneNo,age,address]
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)
        print("New Patient Added")

#to add a new patient
def addPatient():
    name = str(input("Enter Patient Name: "))
    pwd = str(input("Enter Password: "))
    Utype = "PATIENT"
    Privilege = 4
    result = hashlib.md5(pwd.encode())
    password = result.hexdigest()
    ID  = getUserCount()
    addPatientDetails(ID,name)
    with open('UserDetails.csv', 'a') as file:
        data = [ID,name,password,Utype,Privilege]
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)
        
    




# to get patients personal details
def getPatientDetails(ID):
    with open('PersonalDetails.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            if(int(row['ID'])==ID):
                print(row)
            else: continue


# to do login
def doLogin():
    getUserdetails()

# controlls the admin usecases
def AdminController():
    while True:
        print("Select An Option")
        print("-------------------------------")
        print("Add Doctor - 1")
        print("Add Nurse - 2")
        print("Add Pharmacist - 3")
        print("Logout - 4")
        print("-------------------------------")
        argument = int(input("Select Option : "))
        match argument:
            case 1:
                addDoctor()
                continue
            case 2:
                addNurse()
                continue
            case 3:
                addPharmacist()
                continue
            case 4:
                break
            case _:
                print("Invalid Option\n")
                continue

# to controls the patient use cases
def PatientController(ID):
    while True:
        print("Select An Option")
        print("-------------------------------")
        print("View Details - 1")
        print("View Sickness Details- 2")
        print("View Drug Prescriptions- 3")
        print("Logout- 4")
        print("-------------------------------")
        argument = int(input("Select Option : "))
        match argument:
            case 1:    
                getPatientDetails(ID)
                continue
            case 2:
                getSickDetails(ID)
                continue
            case 3:
                getDrugDetails(ID)
                continue
            case 4:
                break
            case _:
                print("Invalid Option\n")
                continue


# to control the doctor usecases
def DoctorController():
    while True:
        print("Select An Option")
        print("-------------------------------")
        print("View All Patient Details - 1")
        print("View Lab Test Prescriptions - 2")
        print("View Drug Prescriptions - 3 ")
        print("View Sickness Details - 4 ")
        print("ADD Lab Test Prescriptions - 5")
        print("ADD Drug Prescriptions - 6 ")
        print("ADD Sickness Details - 7 ")
        print("Logout - 8 ")
        print("-------------------------------")
        argument = int(input("Select Option : "))
        match argument:
            case 1:
                getAllPatientDetails()
                continue
            case 2:
                ID = getUserID()
                getLabDetails(ID)
                continue
            case 3:
                ID = getUserID()
                getDrugDetails(ID)
                continue
            case 4:
                ID = getUserID()
                getSickDetails(ID)
                continue
            case 5:
                addLabTestDetails()
                continue
            case 6:
                addDrugDetails()
                continue
            case 7:
                addSickDetails()
                continue
            case 8:
                break
            case _:
                print("Invalid Option\n")
                continue

# to control the nurse usecases
def NurseController():
    while True:
        print("Select An Option")
        print("-------------------------")
        print("View Patient Details - 1")
        print("view Lab Test Prescriptions - 2")
        print("view Drug Prescriptions - 3 ")
        print("Add New Patient - 4 ")
        print("Add Lab Test Details - 5 ")
        print("Logout - 6 ")
        print("-------------------------")
        argument = int(input("Select Option : "))
        match argument:
            case 1:
                ID = getUserID()
                getPatientDetails(ID)
                continue
            case 2:
                ID = getUserID()
                getLabDetails(ID)
                continue
            case 3:
                ID = getUserID()
                getDrugDetails(ID)
                continue
            case 4:
                addPatient()
                continue
            case 5:
                addLabTestDetails()
                continue
            case 6:
                break
            case _:
                print("Invalid Option\n")


#to control the Pharmacist usecases
def PharmacistController():
    while True:
        print("Select An Option")
        print("-------------------------------")
        print("View Patient Details - 1")
        print("View Drug Prescriptions - 2")
        print("Logout - 3")
        print("-------------------------------")
        argument = int(input("Select Option : "))
        match argument:
            case 1:
                ID = getUserID()
                getPatientDetails(ID)
                continue
            case 2:
                ID = getUserID()
                getDrugDetails(ID)
                continue
            case 3:
                break
            case _:
                print("Invalid Option\n")

while True:
    print("------------------------------\n")
    print("Please Login To The System\n")
    doLogin()
    print("------------------------------\n")
