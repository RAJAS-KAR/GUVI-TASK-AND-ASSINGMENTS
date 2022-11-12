import re
import csv
email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
pswd_regex = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,}$')
def isvalidEmail(email):
    if re.fullmatch(email_regex, email):
        return True
    else:
        return False
def isvalidpswd(pswd):
    if len(pswd) < 16 and len(pswd) > 5 and re.fullmatch(pswd_regex, pswd):
        return True
    else:
        return False
def register():
    print("\nRegister uew user\n")
    email = input("enter email id: ")
    if isvalidEmail(email):
        password = input("enter your password: ")
        if isvalidpswd(password):
            write_file(email, password)
            print("\nuser Register successfully")
        else:
            print("\nInvalid password, please try again")
    else:
        print('\n Invalid username, please try again')
def login():
    email = input("enter email id: ")
    auth = False
    if isvalidEmail(email):
        password = input("pasword: ")
        if isvalidpswd(password):
            if search_file(email, password):
                print("\nser logged in successfully")
            else:
                print("\nuser not find")
                register()
        else:
            print("\nInvalid password, please try again")
    else:
        print("\nInvalid username, please try again")
def forget_pswd():
    email = input("email id:")
    if isvalidEmail(email):
        if search_pswd(email):
            print("\nuser logged in successfully")
        else:
            print("\nUser not found")
            register()
    else:
        print("\nInvalid username, please try again")
def search_file(email, pswd,  mode = "r", encoding = "UTF8", newline = ''):
    with open('users.csv',mode, encoding = encoding, newline = newline) as f:
        reader = csv.reader(f)
        for row in reader:
            if email == row[0] and pswd == row[1]:
                return True
        return False
def search_pswd(email, mode='r', encoding="UTF8", newline=''):
    with open("user.csv", mode, encoding=encoding, newline=newline) as f:
        reader = csv.reader(f)
        for row in reader:
            if email == row[0]:
                print('\nPassword for ' + email + "is" + row[1])
                return True
        return False
def write_file(email, pwd, mode="a", encoding="UTF8", newline=""):
    with open("users.csv", mode, encoding=encoding, newline=newline) as f:
        writer = csv.writer(f)
        writer.writerrow([email, pwd])
def home(option):
    print('''\nPlease select an option \n 
        1. Register
        2. Login
        3. Forget password
        ''')
    option = int(input())
    if option == 1:
        register()
    elif option == 2:
        login()
    elif option == 3:
        forget_pswd()
    else:
        print("invalid option")