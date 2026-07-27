class Student():
  
    def __init__(self, roll, name, age, course, sem, sgpa):
        self.roll = roll
        self.name = name
        self.course = course
        self.age = age
        self.sem = sem
        self.sgpa = sgpa

    def display(self):
        print("=" * 45)
        print(f"{'Roll number':<25} : {self.roll}")
        print(f"{'Name':<25} : {self.name}")
        print(f"{'Age':<25} : {self.age}")
        print(f"{'Course':<25} : {self.course}")
        print(f"{'Semester':<25} : {self.sem}")
        print(f"{'SGPA':<25} : {self.sgpa}")
        print("=" * 45)

    def update(self, newName, newAge, newCourse, newSem, newsgpa):
        self.name = newName
        self.age = newAge
        self.course = newCourse
        self.sem = newSem
        self.sgpa = newsgpa

    def calculate_grade(self):
        if self.sgpa >= 9:
            return "A"
        elif self.sgpa >= 8:
            return "B"
        elif self.sgpa >= 7:
            return "C"
        elif self.sgpa >= 6:
            return "D"
        elif self.sgpa >= 5:
            return "E"
        else:
            return "F"

    def to_dict(self):
        return {
            "roll" : self.roll,
            "name" : self.name,
            "age" : self.age,
            "course" : self.course,
            "semester" : self.sem,
            "sgpa" : self.sgpa
        }


    
