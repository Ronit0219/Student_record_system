from Studentclass import Student
import validation as val
import storage_ver4 as st

def add_student(student_list):
    roll = val.get_roll(student_list)
    name = val.get_name()
    age = val.get_age()
    course = val.get_course()
    sem = val.get_sem()
    sgpa = val.get_sgpa()

    student = Student(roll, name, age, course, sem, sgpa)
    student_list.append(student)
    st.save_student(student_list)
    student.display()
    print("Student saved successfully!")

def find_student(student_list, roll):
    for student in student_list:
        if student.roll == roll:
            return student
    else:
        return None

def search_student(student_list):
    if not student_list:
        print("No record found")
    else:
        roll = val.get_search_roll()
        student = find_student(student_list, roll)
        if not student:
            print("No record found")
        else:
            student.display()

def view_all_students(student_list):
    if not student_list:
        print("No record found")
    else:
        for student in student_list:
            student.display()

def update_student(student_list):
    if not student_list:
        print("No record found")
    else:
        roll = val.get_search_roll()
        student = find_student(student_list, roll)
        if not student:
            print("No record found")
        else:
            name = val.get_name()
            age = val.get_age()
            course = val.get_course()
            sem = val.get_sem()
            sgpa = val.get_sgpa()
            student.update(name, age, course, sem, sgpa)
            st.save_student(student_list)
            student.display()
            print("Record updated successfully")

def delete_student(student_list):
    if not student_list:
        print("No record found")
    else:
        roll = val.get_search_roll()
        student = find_student(student_list, roll)
        if not student:
            print("No record found")
        else:
            student.display()
            response = val.delete_confirmation()
            if response == "y":
                student_list.remove(student)
                st.save_student(student_list)
                print("Record delted successfully")
            else:
                print("Deletion cancelled!")


def count_students(student_list):
    if not student_list:
        print("Student not found")
    else:
        print(f"Total students : {len(student_list)}")
