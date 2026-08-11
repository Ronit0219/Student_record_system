import validation as val
import storage as st
import display as disp

def add_student(student_list):
    roll = val.get_roll(student_list)
    name = val.get_name()
    age = val.get_age()
    course = val.get_course()
    semester = val.get_semester()
    sgpa = val.get_sgpa()
    
    student = {
        "roll" : roll,
        "name" : name,
        "age" : age,
        "course" : course,
        "semester" : semester,
        "sgpa" : sgpa
    }
    student_list.append(student)
    st.save_students(student_list)
    print("Student added successfully!\n")
    disp.display_student(student)

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
        roll = val.get_search_roll()
        student = find_student(student_list, roll)
        if not student:
            print("Student not Found!")
        else:
            disp.display_student(student)

def update_student(student_list):
    if not student_list:
        print("Student not found")
    else:
        roll = val.get_search_roll()
        student = find_student(student_list, roll)
        if not student:
            print("Student not found")
        else:
            student['name'] = val.get_name()
            student['age'] = val.get_age()
            student['course'] = val.get_course()
            student['semester'] = val.get_semester()
            student['sgpa'] = val.get_sgpa()

            st.save_students(student_list)
            disp.display_student(student)
            print("Student updated successfully!\n")

def delete_student(student_list):
    if not student_list:
        print("student not found")
    else:
        roll = val.get_search_roll()
        student = find_student(student_list, roll)
        if not student:
            print("Student not found")
        else:
            disp.display_student(student)
            response = val.deletion_confirmation()
            if response == "y":
                student_list.remove(student)
                st.save_students(student_list)
                print("Student deleted successfully\n")
            else:
                print("Deletion cancelled")

def count_students(student_list):
    if not student_list:
        print("Student not found")
    else:
        print(f"Students found: {len(student_list)}")