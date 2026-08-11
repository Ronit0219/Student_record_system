import json

def save_students(student_list):
        with open("student_record.json", "w") as file:
            json.dump(student_list, file, indent = 4)

def load_students():
    try:
        with open("student_record.json" , "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
         return []