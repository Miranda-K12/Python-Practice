# Define the Student Class
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        total = sum(self.grades)
        return total / len(self.grades) if self.grades else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        return f"Name: {self.name}, Grades: {self.grades}, Average: {avg_grade:.2f}"

# Define the Classroom Class
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_top_students(self):
        sorted_students = sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)
        return sorted_students[:3]

    def get_failed_students(self):
        return [student for student in self.students if student.get_average_grade() < 51]


# Create instances of Student and add grades
student1 = Student("Elene")
student1.add_grade(90)
student1.add_grade(85)
student1.add_grade(88)

student2 = Student("Nino")
student2.add_grade(50)
student2.add_grade(45)
student2.add_grade(52)

student3 = Student("Levan")
student3.add_grade(30)
student3.add_grade(35)
student3.add_grade(40)

student4 = Student("Mariam")
student4.add_grade(95)
student4.add_grade(92)
student4.add_grade(97)

student5 = Student("Tina")
student5.add_grade(78)
student5.add_grade(67)
student5.add_grade(95)

# Create a Classroom and add students
classroom = Classroom()
classroom.add_student(student1)
classroom.add_student(student2)
classroom.add_student(student3)
classroom.add_student(student4)
classroom.add_student(student5)

# Get and print the top 3 students
top_students = classroom.get_top_students()
print("Top 3 Students:")
for student in top_students:
    print(student)

# Get and print students who have failed (average grade below 51)
failed_students = classroom.get_failed_students()
print("\nFailed Students:")
for student in failed_students:
    print(student)





