students = []


class Student:
    def __init__(self, name,student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(student)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.get_school_name

mark = Student('paul')

#print(students)
print(mark)