# Define the parent class Person
class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number
    
    def walk(self):
        print(f"{self.name} is walking.")
    
    def talk(self):
        print(f"{self.name} is talking.")
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
# Define the Student class that inherits from Person
class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa
    
    def study(self):
        print(f"{self.name} is studying.")
    
    def attend_class(self):
        print(f"{self.name} is attending class.")
    
    def write_exam(self):
        print(f"{self.name} is writing an exam.")
        
# Define the Teacher class that inherits from Person
class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")
    def teach(self):
        print(f"{self.name} bearing {self.cid_number} getting salary NU.{self.salary} in {self.department} department.")
    
    def grade_students(self):
        print(f"{self.name} is grading students.")
    
    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")
        
# Creating objects
student = Student(name="Pema", age=20, cid_number="10903003183", student_id="02230221", course="ICE", year=1, gpa=10)
teacher = Teacher(name="Madam Yangchen", age=30, cid_number="123456789", subject="CSF", salary=70000, department="ICT", designation="Lecturer")

# Demonstrating the behaviors
print("Student Behaviors:")
student.walk()
student.talk()
student.eat()
student.sleep()
student.study()
student.attend_class()
student.write_exam()

print("\nTeacher Behaviors:")
teacher.walk()
teacher.talk()
teacher.eat()
teacher.sleep()
teacher.teach()
teacher.grade_students()
teacher.attend_meeting()