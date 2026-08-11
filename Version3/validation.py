def get_roll(student_list):
    while True:
        try:
            roll = int(input("Enter roll number: "))
            if roll > 0:
                for student in student_list:
                    if student["roll"] == roll:
                        print("This roll no. already exists")
                        break
                else:
                    return roll
            else:
                print("Error! Enter a valid roll number")
        except ValueError:
            print("You can only enter an integer")

def get_name():
    while True:
        name = input("Enter name: ").strip()
        if not name:
            print("Error name cannot be empty!")
        else:
            return name.title()
        
def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age in range(16,101):
                return age
            print("Age must be between 16 and 100")
        except ValueError:
            print("Error! enter an integer only")

def get_course():
    while True:
        course = input("Enter your course name: ").strip()
        if not course:
            print("Enter a valid course name!")
        else:
            return course.title()
        
def get_semester():
    while True:
        try:
            sem = int(input("Enter the semester(1 to 8): "))
            if sem in range(1,9):
                return sem
            print("You have to enter a valid semester")
        except ValueError:
            print("Error! you can only enter integer value")

def get_sgpa():
    while True:
        try:
            sgpa = float(input("Enter sgpa: "))
            if 0 <= sgpa <= 10:
                return sgpa
            print("Enter sgpa between 0 to 10 only!")
        except ValueError:
            print("Error! please enter valid value")

def deletion_confirmation():
    while True:
        response = input("Do you want to delete this student's record?\nEnter y if yes\t\tEnter n if no\n").strip().lower()
        if response in ("y", "n"):
            return response
        print("You can only enter y and n")

def get_search_roll():
    while True:
        try:
            search_roll = int(input("Enter student's Roll Number: "))
            if search_roll > 0:
                return search_roll
            print("Enter a valid roll number")
        except ValueError:
            print("Error! Please enter an integer value")