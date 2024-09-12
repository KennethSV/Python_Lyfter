'''
School Management System
'''

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def breath(self):
        pass

class Student(Person):
    def __init__(self, name, age, address, grade_average):
        Person.__init__(self, name, age, address)
        self.grade_average = grade_average

    def study(self):
        pass

class Teacher(Person):
    def __init__(self, name, age, address, course, salary):
        Person.__init__(self, name, age, address)
        self.course = course
        self.salary = salary

    def teach(self):
        pass

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, address, grade_average, course, salary):
        Student.__init__(self, name, age, address, grade_average)
        Teacher.__init__(self, name, age, address, course, salary)


bob = TeachingAssistant('bob', 16, 'San Francisco', 75, 'math', 0)
print(f"The teacher's assistant {bob.name}, is {bob.age} years old. Has an average score of {bob.grade_average}, and helps on the {bob.course} class")