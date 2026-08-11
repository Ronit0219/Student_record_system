import operations as op
import storage as st
import display as disp

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

def main():
    student_list = st.load_students()
    while True:
        main_menu()
        choice = user_choice()
        match choice:
            case 1:
                op.add_student(student_list)
            case  2:
                disp.view_all_students(student_list)
            case 3:
                op.search_student(student_list)
            case 4:
                op.update_student(student_list)
            case 5:
                op.delete_student(student_list)
            case 6:
                op.count_students(student_list)
            case 7:
                print("Exiting from the program")
                break

if __name__ == "__main__":
    main()