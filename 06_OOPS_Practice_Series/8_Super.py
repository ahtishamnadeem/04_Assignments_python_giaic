class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person Created: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call parent class constructor
        self.subject = subject
        print(f"Teacher Assigned: {self.name} teaches {self.subject}")

# Create an object of Teacher
t1 = Teacher("Miss Amna", "Python")
