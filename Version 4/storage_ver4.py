import json
from Studentclass import Student
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "Student_record_ver4.json")

def save_student(student_list):
    with open(FILE_PATH, "w") as file:
        new_list = []
        for student in student_list:
            new_list.append(student.to_dict())
        json.dump(new_list, file, indent = 4)

def load_student():
    try:
        with open(FILE_PATH, "r") as file:
            student_list = []
            data = json.load(file)
            for student_data in data:
                new_student = Student(student_data["roll"],
                                      student_data["name"],
                                      student_data["age"],
                                      student_data["course"],
                                      student_data["semester"],
                                      student_data["sgpa"])
                student_list.append(new_student)
            return student_list
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return [] 
