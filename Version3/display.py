def display_student(student):
    print("=" * 45)
    print(f"{'Roll Number':<25}: {student['roll']}")
    print(f"{'Name':<25}: {student['name']}")
    print(f"{'Age':<25}: {student['age']}")
    print(f"{'Course':<25}: {student['course']}")
    print(f"{'Semester':<25}: {student['semester']}")
    print(f"{'sgpa':<25}: {student['sgpa']}")
    print("=" * 45)

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