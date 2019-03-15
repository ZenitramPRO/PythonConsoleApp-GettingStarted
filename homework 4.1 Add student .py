students = []
add_new_student = True

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
        print(students_titlecase)
    return students_titlecase

 
def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name,student_id=332):
    student = {"name":name, "student_id": student_id}
    students.append(student)


def prompt_add_new_student():
    add_new_student = input("Do you want to add another Student? (Y/N): ")
    if add_new_student.title() == 'Y' or add_new_student.title() == 'Yes':
        add_new_student = True
    elif add_new_student.title() == 'N' or add_new_student.title() == 'No':
        add_new_student = False 
    return add_new_student
        
    
while add_new_student == True:
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    add_student(student_name, student_id)
    student_list = get_students_titlecase()
    
    add_new_student = prompt_add_new_student()
    
