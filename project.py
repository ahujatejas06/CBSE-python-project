import getpass
import sys
import hashlib
import mysql.connector

def establish_conn(passwd):
    global db
    global cursor
    try:
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = passwd)
        print("Server Connection Successful")
    except:
        print("Server Error. Could not connect to Server....")
        print("Exiting Program")
        sys.exit()
    db.close()
    try:
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = passwd, database = "school")
        print("Database Connection Successful")
        cursor = db.cursor(buffered=True)
    except:
        print("Database Does not exist...")
        create_database(passwd)
        
def create_database(passwd):
    try:
        global cursor
        global db
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = passwd)
        cursor = db.cursor(buffered=True)
        print("Creating Database 'school' ")
        cursor.execute("create database school")
        cursor.execute("use school")
        print("Creating Table 'students'")
        cursor.execute("create table students(admn char(8) primary key, name varchar(15) not null, class integer(2) not null, roll_no integer(2) not null, section char(1) not null, gender char(1) not null, ph_no decimal(11, 0) not null, DOB date not null)")
    except:
        print("Error while creating database")
        print("Exiting Program")
        sys.exit()

def insert_into_database(admn, name, _class, roll_no, section, gender, ph_no, DOB):
    command = "insert into students values("
    command = command + "'" + admn + "'," 
    command = command + "'" + name + "',"
    command = command + str(_class) + ","
    command = command + str(roll_no) + ","
    command = command + "'" + section + "',"
    command = command + "'" + gender + "',"
    command = command + str(ph_no) + ","
    command = command + "'" + str(DOB) + "')" 
    cursor.execute(command)
    db.commit()
    print("Record inserted")

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def remove_account():
    admn = input("Please enter admn (xxx\yy\h) : ")
    admn_copy = admn.split(sep="\\")
    while len(admn_copy) != 3:
        print("Please enter a valid admission number.")
        print("Please use backslash if you are using forward slash")
        admn = input("Please enter admn (xxx\yy\h) : ")
        admn_copy = admn.split(sep="\\")
    cursor.execute("select count(admn) from students where admn = " + "'" +str(admn_copy[0]) + "\\\\" + str(admn_copy[1]) + "\\\\" + str(admn_copy[2]) + "'")
    records = cursor.fetchone()
    if records[0] == 0:
        print("Record Not Found")
    else:
        cursor.execute("delete from students where admn = " + "'" + str(admn_copy[0]) + "\\\\" + str(admn_copy[1]) + "\\\\" + str(admn_copy[2]) + "'")
        db.commit()
        print(cursor.rowcount, "Records Deleted")

        


def update_account():
    admn = input("Please enter admn (xxx\yy\h) : ")
    admn_copy = admn.split(sep="\\")
    while len(admn_copy) != 3:
        print("Please enter a valid admission number.")
        print("Please use backslash if you are using forward slash")
        admn = input("Please enter admn (xxx\yy\h) : ")
        admn_copy = admn.split(sep="\\")
    cursor.execute("select count(admn) from students where admn = " + "'" +str(admn_copy[0]) + "\\\\" + str(admn_copy[1]) + "\\\\" + str(admn_copy[2]) + "'")
    records = cursor.fetchone()
    if records[0] == 0:
        print("Record Not Found")
    else:
        print("The fields available for updating are", "Name (Requires Password),", "Class,", "Roll No.,", "Section,",
              "Phone Number,")
        i = int(input("Enter the number of fields to edit : "))
        while i > 5 or i < 0:
            print("Please enter a number between 1 and 5 only or 0 to cancel update")
            i = int(input("Enter the number of fields to edit : "))
        for j in range(i):
            print("1", "Class")
            print("2", "Section")
            print("3", "Roll No")
            print("4", "Phone Number")
            print("5", "Name")
            edit_field = int(input("Please enter the number of field you want to edit : "))

            if edit_field == 1:
                _class = int(input("Enter updated class : "))
                while _class > 12 or _class < 1:
                    print("Please enter a valid class : ")
                    _class = int(input("Enter Class : "))
                command = "update students set class = " + str(_class)
                command = command + " where admn = " + "'" +str(admn_copy[0]) + "\\\\" + str(admn_copy[1]) + "\\\\" + str(admn_copy[2]) + "'"
                cursor.execute(command)
                update = input("Are you sure you want to update the selected field(Y/N) : ")
                while update not in ['Y', 'N']:
                    print("I don't think I understand that.")
                    update = input("Are you sure you want to update the selected field(Y/N) : ")
                if update == 'Y':
                    db.commit()
                else:
                    print("Cancelling update")
                    db.rollback()

            elif edit_field == 2:
                section = input("Enter updated section : ")
                while section not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                    print("Please enter a valid section")
                    section = input("Enter section : ")
                command = "update students set section = " + "'" + section + "'"
                command = command + " where admn = " + "'" +str(admn_copy[0]) + "\\\\" + str(admn_copy[1]) + "\\\\" + str(admn_copy[2]) + "'"
                cursor.execute(command)
                update = input("Are you sure you want to update the selected field(Y/N) : ")
                while update not in ['Y', 'N']:
                    print("I don't think I understand that.")
                    update = input("Are you sure you want to update the selected field(Y/N) : ")
                if update == 'Y':
                    db.commit()
                else:
                    print("Cancelling update")
                    db.rollback()
            elif edit_field == 3:
                roll_no = int(input("Enter updated Roll Number : "))
                command = "update students set roll_no = " + str(roll_no)
                command = command + " where admn = " + "'" +str(admn_copy[0]) + "\\\\" + str(admn_copy[1]) + "\\\\" + str(admn_copy[2]) + "'"
                cursor.execute(command)
                update = input("Are you sure you want to update the selected field(Y/N) : ")
                while update not in ['Y', 'N']:
                    print("I don't think I understand that.")
                    update = input("Are you sure you want to update the selected field(Y/N) : ")
                if update == 'Y':
                    db.commit()
                else:
                    print("Cancelling update")
                    db.rollback()
            elif edit_field == 4:
                ph_no = int(input("Enter updated Phone Number : "))
                while ph_no >= 10 ** 10 and ph_no < 10 ** 11:
                    print("Please enter a valid phone number")
                    ph_no = int(input("Enter phone number : "))
                command = "update students set ph_no = " + str(ph_no)
                command = command + " where admn = " + "'" +str(admn_copy[0]) + "\\\\" + str(admn_copy[1]) + "\\\\" + str(admn_copy[2]) + "'"
                cursor.execute(command)
                update = input("Are you sure you want to update the selected field(Y/N) : ")
                while update not in ['Y', 'N']:
                    print("I don't think I understand that.")
                    update = input("Are you sure you want to update the selected field(Y/N) : ")
                if update == 'Y':
                    db.commit()
                else:
                    print("Cancelling update")
                    db.rollback()
            elif edit_field == 5:
                passwd = getpass.getpass(prompt='Enter Program Password : ', stream=None)
                passwd = encrypt_string(passwd)
                if passwd != "2317234be85eaa1c30311c7b1cabed30c7fc5e9491daac527f03f8cfb67b791c":
                    print("Incorrect Password. Cancelling update")
                else:
                    name = (input("Enter updated name : ")).upper()
                command = "update students set name = " + "'" + name + "'"
                command = command + " where admn = " + "'" +str(admn_copy[0]) + "\\\\" + str(admn_copy[1]) + "\\\\" + str(admn_copy[2]) + "'"
                cursor.execute(command)
                update = input("Are you sure you want to update the selected field(Y/N) : ")
                while update not in ['Y', 'N']:
                    print("I don't think I understand that.")
                    update = input("Are you sure you want to update the selected field(Y/N) : ")
                if update == 'Y':
                    db.commit()
                else:
                    print("Cancelling update")
                    db.rollback()



def display_account():
    admn = input("Please enter admn (xxx\yy\h) : ")
    admn_copy = admn.split(sep="\\")
    while len(admn_copy) != 3:
        print("Please enter a valid admission number.")
        print("Please use backslash if you are using forward slash")
        admn = input("Please enter admn (xxx\yy\h) : ")
        admn_copy = admn.split(sep="\\")
    cursor.execute("select count(admn) from students where admn = " + "'" +str(admn_copy[0]) + "\\\\" + str(admn_copy[1]) + "\\\\" + str(admn_copy[2]) + "'")
    records = cursor.fetchone()
    if records[0] == 0:
        print("Record Not Found")
    else:
        cursor.execute("select * from students where admn = " + "'" +str(admn_copy[0]) + "\\\\" + str(admn_copy[1]) + "\\\\" + str(admn_copy[2]) + "'")
        details = cursor.fetchone()
        print("RECORD OF ADMISSION NUMBER : ", admn)
        print("NAME : ", details[1])
        print("CLASS : ", details[2])
        print("ROLL NO. : ", details[3])
        print("SECTION : ", details[4])
        print("GENDER : ", details[5])
        print("PHONE NUMBER : ", details[6])
        print("DOB : ", details[7])


def add_account():
    admn = input("Please enter admn (xxx\yy\h) : ")
    admn_copy = admn.split(sep="\\")
    while len(admn_copy) != 3:
        print("Please enter a valid admission number.")
        print("Please use backslash if you are using forward slash")
        admn = input("Please enter admn (xxx\yy\h) : ")
        admn_copy = admn.split(sep="\\")
    add = True
    cursor.execute("select count(admn) from students where admn = " + "'" + str(admn_copy[0]) + '\\\\' + str(admn_copy[1]) + "\\\\" + str(admn_copy[2]) + "'")
    records = cursor.fetchone()
    for j in records:
        if j > 0:
            add = False
    if add:
        admn = str(admn_copy[0]) + "\\\\" + str(admn_copy[1]) + "\\\\" + str(admn_copy[2])
        name = (input("Enter name : ")).upper()
        _class = int(input("Enter class : "))
        while _class > 12 or _class < 1:
            print("Please enter a valid class")
            _class = int(input("Enter Class : "))
        section = input("Enter Section : ")
        while section not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            print("Please enter a valid section")
            section = input("Enter Section : ")
        roll_no = int(input("Enter roll no : "))
        gender = input("Enter gender (F/M/O) : ")
        while gender not in ['F', 'M', 'O']:
            print("Please enter a valid gender")
            gender = input("Enter Gender : ")
        ph_no = int(input("Enter phone number : "))
        while ph_no < 10 ** 9 or ph_no >= 10 ** 10:
            print("Please enter a valid phone number")
            ph_no = int(input("Enter phone number : "))
        DOB = input("Please enter DOB (YYYYMMDD) : ")
        insert_into_database(admn, name, _class, roll_no, section, gender, ph_no, DOB)


def main_menu():
    print("Select an option from below")
    print("Press 0 to Exit")
    print("Press 1 to add student details")
    print("Press 2 to remove student details")
    print("Press 3 to display student details")
    print("Press 4 to update student details")
    x = int(input())
    return x

def reset_database(passwd):
    print("Removing Database 'school'")
    cursor.execute("drop database school")
    create_database(passwd)

def main():
    prev_admn = 0
    passwd = getpass.getpass(prompt='Enter Program Password : ', stream=None)
    passwd = encrypt_string(passwd)
    if passwd != "2317234be85eaa1c30311c7b1cabed30c7fc5e9491daac527f03f8cfb67b791c":
        print("Incorrect Password. Exiting Program")
        sys.exit()
    passwd = getpass.getpass(prompt='Enter MySQL Server Password : ', stream=None)
    establish_conn(passwd)
    print()
    print()
    while db.is_connected():
        cursor.execute("select count(admn) from students")
        records = cursor.fetchone()
        records = records[0]
        print(records, "Records Found")
        x = main_menu()  # call main menu to select option
        if x == 0:
            cursor.close()
            db.close()
            sys.exit()
        elif x == 1:
            add_account()
        elif x == 2:
            remove_account()
        elif x == 3:
            display_account()
        elif x == 4:
            update_account()
        elif x == 100:
            reset_database(passwd)
        else:
            print("Please select a valid option")
        print()
        print()


if __name__ == "__main__":
    main()
