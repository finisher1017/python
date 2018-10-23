student_list = []


class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def average(self):
        number = len(student.marks)
        if number == 0:
            return 0

        else:
            total = sum(student.marks)
            return total / number


def create_student():
    # Ask the user for the students name
    # Create the dictionary
    # Return that dictionary

    name = input("Enter the student's name: ")
    #student = {"name": student_name, 'marks': []}
    #student_list.append(student)
    #print("{}, has been added to the list of students".format(student_name))
    student = Student(name)
    student_list.append(student)
    return student


def add_mark(student, mark):
    #student['marks'].append(mark)
    student.marks.append(mark)




def student_details(student):
    print("{}, average mark: {}.".format(student.name, student.average_mark()))


def print_students(list):
    count = 0
    for i, s in enumerate(list):
        print("ID: {}".format(i))
        student_details(student_list[count])
        count += 1

def menu():
    # Add a student (to student_list)
    # Add a mark to a student
    # Print a list of students
    # Exit the application
    print(
        """
            1.) Add student
            2.) Add a mark to a student
            3.) Print list of students
            4.) Exit application
        """
    )
    choice = None
    while choice != " ":
        choice = input("Choose an option from the menu: ")
        if choice == "1":
            create_student()
        if choice == "2":
            student_id = int(input("Enter student ID: "))
            student = student_list[student_id]
            new_mark = int(input("Enter new mark: "))
            add_mark(student, new_mark)
        if choice == "3":
            print_students(student_list)
        if choice == "4":
            exit()




menu()