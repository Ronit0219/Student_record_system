def get_name():
    while True:
        name = input("Enter name: ").strip()
        if not name:
            print("Name cannot be empty!")
        else:
            return name.title()

def get_roll(student_list):
    while True:
        try:
            roll = int(input("Enter roll number: "))
            if roll > 0:
                for student in student_list:
                    if student.roll == roll:
                        print("Student already exists")
                        break
                else:
                    return roll
            else:
                print("Please enter a valid roll number!")
        except ValueError:
            print("Please enter a valid roll number!")

def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if 16 <= age <= 100:
                return age
            print("Student must be 16 to 100 years old")
        except ValueError:
            print("Please enter valid age!")


def get_course():
    while True:
        course = input("Enter course name: ").strip()
        if not course:
            print("Course name cannot be empty!")
        else:
            return course.capitalize()

def get_sem():
    while True:
        try:
            sem = int(input("Enter semester: "))
            if sem in range(1,9):        
                return sem
            print("Please enter a valid semester")
        except ValueError:
            print("Error! please neter an integer value")

def get_sgpa():
    while True:
        try:
            sgpa = float(input("Enter sgpa: "))
            if 0 <= sgpa <= 10:
                return sgpa
            print("Please enter a valid sgpa between 0 to 10")
        except:
            print("Please enter a valid value")

def get_search_roll():
    while True:
        try:
            roll = int(input("Enter roll number : "))
            if roll > 0:
                return roll
            print("Enter a valid roll number")
        except ValueError:
            print("Please enter an integer value")

def delete_confirmation():
    while True:
        response = input("Do you eant to delete the student information?\n if yeas enter y\t if no enter n\n").strip().lower()
        if response in ("y", "n"):
            return response
        print("Please enter a valid choice")
        