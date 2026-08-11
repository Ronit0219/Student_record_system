import sys

def main_menu():
    print("=" * 15, "Student Record Management System", "=" * 15)
    print("1. Add Student\n2. View all Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Count Students\n7. Exit\n")

def user_choice():
    while True:
        try:
            x = int(input("Enter your choice from the given menu: "))
            if x in range(1,8):
                return x
            print("You can only enter from 1 to 7")
        except ValueError:
            print("Enter an integer value")

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

def display_student(student):
    print("=" * 45)
    print(f"{'Roll Number':<25}: {student['roll']}")
    print(f"{'Name':<25}: {student['name']}")
    print(f"{'Age':<25}: {student['age']}")
    print(f"{'Course':<25}: {student['course']}")
    print(f"{'Semester':<25}: {student['semester']}")
    print(f"{'sgpa':<25}: {student['sgpa']}")
    print("=" * 45)
        
def add_student(student_list):
    roll = get_roll(student_list)
    name = get_name()
    age = get_age()
    course = get_course()
    semester = get_semester()
    sgpa = get_sgpa()
    
    student = {
        "roll" : roll,
        "name" : name,
        "age" : age,
        "course" : course,
        "semester" : semester,
        "sgpa" : sgpa
    }
    student_list.append(student)
    print("Student added successfully!\n")
    display_student(student)
    
def view_all_students(student_list):
    if not student_list:
        print("Student not Found")
    else:
        print("=" * 20, "Student Record System", "=" * 20)
        header = (f"{'Roll Number':<15}"
                f"{'Name':<15}"
                f"{'Age':<15}"
                f"{'Course':<15}"
                f"{'Sem':<15}"
                f"{'sgpa'}")
        print(header)
        print("=" * len(header))
        for student in student_list:
            print(f"{student['roll']:<15}"
                  f"{student['name']:<15}"
                  f"{student['age']:<15}"
                  f"{student['course']:<15}"
                  f"{student['semester']:<15}"
                  f"{student['sgpa']}") 
        print("=" * len(header))

def get_search_roll():
    while True:
        try:
            search_roll = int(input("Enter student's Roll Number: "))
            if search_roll > 0:
                return search_roll
            print("Enter a valid roll number")
        except ValueError:
            print("Error! Please enter an integer value")

def find_student(student_list,roll):
    for student in student_list:
        if student['roll'] == roll:
            return student
    else:
        return None
            
def search_student(student_list):
    if not student_list:
        print("Student not found")
    else: 
        roll = get_search_roll()
        student = find_student(student_list, roll)
        if not student:
            print("Student not Found!")
        else:
            display_student(student)

def update_student(student_list):
    if not student_list:
        print("Student not found")
    else:
        roll = get_search_roll()
        student = find_student(student_list, roll)
        if not student:
            print("Student not found")
        else:
            student['name'] = get_name()
            student['age'] = get_age()
            student['course'] = get_course()
            student['semester'] = get_semester()
            student['sgpa'] = get_sgpa()

            display_student(student)
            print("Student updated successfully!\n")

def deletion_confirmation():
    while True:
        response = input("Do you want to delete this student's record?\nEnter y if yes\t\tEnter n if no\n").strip().lower()
        if response in ("y", "n"):
            return response
        print("You can only enter y and n")

def delete_student(student_list):
    if not student_list:
        print("student not found")
    else:
        roll = get_search_roll()
        student = find_student(student_list, roll)
        if not student:
            print("Student not found")
        else:
            display_student(student)
            response = deletion_confirmation()
            if response == "y":
                student_list.remove(student)
                print("Student deleted successfully\n")
            else:
                print("Deletion cancelled")

def count_students(student_list):
    if not student_list:
        print("Student not found")
    else:
        print(f"Students found: {len(student_list)}")


def main():
    student_list = []
    while True:
        main_menu()
        choice = user_choice()
        match choice:
            case 1:
                add_student(student_list)
            case  2:
                view_all_students(student_list)
            case 3:
                search_student(student_list)
            case 4:
                update_student(student_list)
            case 5:
                delete_student(student_list)
            case 6:
                count_students(student_list)
            case 7:
                print("Exiting from the program")
                break

if __name__ == "__main__":
    main()