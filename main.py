import getpass
import sys
import hashlib
import datetime
from random import choice
from random import randint
student_details = dict()
class std_details_class:
    def __init__(self, name, _class, roll_no, section, gender, ph_no, DOB):
        self.name = name
        self._class = _class
        self.roll_no = roll_no
        self.section = section
        self.gender = gender
        self.ph_no = ph_no
        self.DOB = DOB

    def std_details(self):
        return (self.name, self._class, self.roll_no, self.section, self.gender, self.ph_no, self.DOB)

    def edit_name(self, name):
        self.name = name

    def edit_phno(self, ph_no):
        self.ph_no = ph_no

    def edit_section(self, section):
        self.section = section

    def edit_class(self, _class):
        self._class = _class

    def edit_roll_no(self, roll_no):
        self.roll_no = roll_no


class admission_number:
    def __init__(self, std_number, year, house):
        self.year = year
        self.std_number = std_number
        self.house = house

    def get_admn(self):
        return get3digits_as_str(self.std_number) + '\\' + get2digits_as_str(self.year) + '\\' + str(self.house)

def get3digits_as_str(num):
  if num < 100 and num >= 10:
    return ('0'+ str(num))
  elif num > 0 and num < 10:
    return ('00' + str(num))
  else:
    return str(num)

def get2digits_as_str(num):
  if num > 0 and num < 10:
    return ('0' + str(num))
  else:
    return str(num)

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
    save_key = None
    for key in student_details.keys():
        if key.get_admn() == admn:
            save_key = key
            break
    if save_key != None:
        del student_details[save_key]
        print("Account removed")
    else:
        print("Record not found")


def update_account():
    admn = input("Please enter admn (xxx\yy\h) : ")
    admn_copy = admn.split(sep="\\")
    while len(admn_copy) != 3:
        print("Please enter a valid admission number.")
        print("Please use backslash if you are using forward slash")
        admn = input("Please enter admn (xxx\yy\h) : ")
        admn_copy = admn.split(sep="\\")
    save_key = None
    for key in student_details.keys():
        if key.get_admn() == admn:
            save_key = key
            break
    if save_key != None:
        print("The fields available for updating are", "Name (Requires Password),", "Class,", "Roll No.,", "Section,",
              "Phone Number,")
        i = int(input("Enter the number of fields to edit : "))
        while i > 5 or i < 1:
            print("Please enter a number between 1 and 5 only")
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
                update = input("Are you sure you want to update the selected field(Y/N) : ")
                while update not in ['Y', 'N']:
                    print("I don't think I understand that.")
                    update = input("Are you sure you want to update the selected field(Y/N) : ")
                if update == 'Y':
                    student_details[save_key].edit_class(_class)
                else:
                    print("Cancelling update")
            elif edit_field == 2:
                section = input("Enter updated section : ")
                while section not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                    print("Please enter a valid section")
                    section = input("Enter section : ")
                update = input("Are you sure you want to update the selected field(Y/N) : ")
                while update not in ['Y', 'N']:
                    print("I don't think I understand that.")
                    update = input("Are you sure you want to update the selected field(Y/N) : ")
                if update == 'Y':
                    student_details[save_key].edit_section(section)
                else:
                    print("Cancelling update")
            elif edit_field == 3:
                roll_no = int(input("Enter updated Roll Number : "))
                update = input("Are you sure you want to update the selected field(Y/N) : ")
                while update not in ['Y', 'N']:
                    print("I don't think I understand that.")
                    update = input("Are you sure you want to update the selected field(Y/N) : ")
                if update == 'Y':
                    student_details[save_key].edit_roll_no(roll_no)
                else:
                    print("Cancelling update")
            elif edit_field == 4:
                ph_no = int(input("Enter updated Phone Number : "))
                while ph_no >= 10 ** 10 and ph_no < 10 ** 11:
                    print("Please enter a valid phone number")
                    ph_no = int(input("Enter phone number : "))
                update = input("Are you sure you want to update the selected field(Y/N) : ")
                while update not in ['Y', 'N']:
                    print("I don't think I understand that.")
                    update = input("Are you sure you want to update the selected field(Y/N) : ")
                if update == 'Y':
                    student_details[save_key].edit_phno(ph_no)
                else:
                    print("Cancelling update")
            elif edit_field == 5:
                passwd = input("Enter Password : ")
                passwd = encrypt_string(passwd)
                if passwd != "2317234be85eaa1c30311c7b1cabed30c7fc5e9491daac527f03f8cfb67b791c":
                    print("Incorrect Password. Cancelling update")
                else:
                    name = input("Enter updated name : ")

                    update = input("Are you sure you want to update the selected field(Y/N) : ")
                    while update not in ['Y', 'N']:
                        print("I don't think I understand that.")
                        update = input("Are you sure you want to update the selected field(Y/N) : ")
                    if update == 'Y':
                        student_details[save_key].edit_name(name)
                    else:
                        print("Cancelling update")

    else:
        print("Record not found")


def display_account():
    admn = input("Please enter admn (xxx\yy\h) : ")
    admn_copy = admn.split(sep="\\")
    while len(admn_copy) != 3:
        print("Please enter a valid admission number.")
        print("Please use backslash if you are using forward slash")
        admn = input("Please enter admn (xxx\yy\h) : ")
        admn_copy = admn.split(sep="\\")
    save_key = None
    for key in student_details.keys():
        if key.get_admn() == admn:
            save_key = key
            break
    if save_key != None:
        details = student_details[save_key].std_details()
        print("RECORD OF ADMISSION NUMBER : ", admn)
        print("NAME : ", details[0])
        print("CLASS : ", details[1])
        print("ROLL NO. : ", details[2])
        print("SECTION : ", details[3])
        print("GENDER : ", details[4])
        print("PHONE NUMBER : ", details[5])
        print("DOB : ", details[6])
    else:
        print("Record not found")


def add_account():
    admn = input("Please enter admn (xxx\yy\h) : ")
    admn_copy = admn.split(sep="\\")
    while len(admn_copy) != 3:
        print("Please enter a valid admission number.")
        print("Please use backslash if you are using forward slash")
        admn = input("Please enter admn (xxx\yy\h) : ")
        admn_copy = admn.split(sep="\\")
    add = True
    for key in student_details.keys():
        if key.get_admn() == admn:
            print("Record for admission number", admn, "already exists")
            print("Please proceed to the update account menu to update it")
            add = False
            break
    if add:
        admn = admission_number(int(admn_copy[0]), int(admn_copy[1]), str(admn_copy[2]))
        name = input("Enter name : ")
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
        while ph_no >= 10 ** 10 and ph_no < 10 ** 11:
            print("Please enter a valid phone number")
            ph_no = int(input("Enter phone number : "))
        DOB = input("Please enter DOB (DDMMYYYY) : ")
        student_details[admn] = std_details_class(name, _class, roll_no, section, gender, ph_no, DOB)

def new_admission(prev_admn):
    admn = prev_admn + 1
    year = str((datetime.datetime.now()).year)
    house = randint(1,4)
    print(house)
    if house == 1:
        house = 'V'
    elif house == 2:
        house = 'G'
    elif house == 3:
        house = 'K'
    else:
        house = 'D'
    admn = admission_number(admn, int(year[2:]), house)
    name = input("Enter name : ")
    _class = 1
    sequence = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    section = choice(sequence)
    gender = input("Enter gender (F/M/O) : ")
    while gender not in ['F', 'M', 'O']:
        print("Please enter a valid gender")
        gender = input("Enter Gender : ")
    ph_no = int(input("Enter phone number : "))
    while ph_no >= 10 ** 10 and ph_no < 10 ** 11:
        print("Please enter a valid phone number")
        ph_no = int(input("Enter phone number : "))
    DOB = input("Please enter DOB (DDMMYYYY) : ")
    student_details[admn] = std_details_class(name, _class, -1, section, gender, ph_no, DOB)
    print("The admission number of the student is :", admn.get_admn())
    print("The section of the student is :", section)


def main_menu():
    print("Select an option from below")
    print("Press 0 to Exit")
    print("Press 1 to add student details")
    print("Press 2 to remove student details")
    print("Press 3 to display student details")
    print("Press 4 to update student details")
    print("Press 5 for a new admission")
    x = int(input())
    return x


def main():
    prev_admn = 0
    student_details[admission_number(11, 12, 'G')] = std_details_class("Tejas Ahuja", 11, 52, 'A', 'M', 4372874347,
                                                                     '05112002')
    passwd = getpass.getpass(prompt='Enter Password : ', stream=None)
    passwd = encrypt_string(passwd)
    if passwd != "2317234be85eaa1c30311c7b1cabed30c7fc5e9491daac527f03f8cfb67b791c":
        print("Incorrect Password. Exiting Program")
        sys.exit()
    while True:
        print(student_details)
        print(len(student_details), "Records found")
        x = main_menu()  # call main menu to select option
        if x == 0:
            sys.exit()
        elif x == 1:
            add_account()
        elif x == 2:
            remove_account()
        elif x == 3:
            display_account()
        elif x == 4:
            update_account()
        elif x == 5:
            new_admission(prev_admn)
            prev_admn += 1
        else:
            print("Please select a valid option")
        print()
        print()


if __name__ == "__main__":
    main()
