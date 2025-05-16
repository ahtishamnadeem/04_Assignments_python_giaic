# Class decorator that adds a greet method
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Adds the greet method to the class
    return cls

# Applying the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"

# Creating an instance of the Person class
person = Person("Alice")

# Calling the introduce method
print(person.introduce())

# Calling the greet method added by the decorator
print(person.greet())
