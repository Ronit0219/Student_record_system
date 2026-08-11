import operation_ver4 as op
import storage_ver4 as st
import os
print(os.getcwd())

def main_menu():
    print("=" * 15, "Student Record Management System", "=" * 15)
    print("1. Add Student\n2. View all Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Count Students\n7. Exit\n")

def get_choice():
    while True:
        try:
            x = int(input("Enter your choice from the given menu: "))
            if x in range(1,8):
                return x
            print("You can only enter from 1 to 7")
        except ValueError:
            print("Enter an integer value")

def main():
    student_list = st.load_student()
    while True:
        main_menu()
        choice = get_choice()
        match choice:
            case 1:
                op.add_student(student_list)
            case 2:
                op.view_all_students(student_list)
            case 3:
                op.search_student(student_list)
            case 4:
                op.update_student(student_list)
            case 5:
                op.delete_student(student_list)
            case 6:
                op.count_students(student_list)
            case 7:
                st.save_student(student_list)
                print("Exiting from the program")
                break

if __name__ == "__main__":
    main()
