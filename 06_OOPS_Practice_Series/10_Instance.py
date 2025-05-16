class Dog:
    def __init__(self, name, breed):
        self.name = name      # instance variable for dog's name
        self.breed = breed    # instance variable for dog's breed

    def bark(self):
        print(f"{self.name} says: Woof! 🐾")

# Creating an object of Dog
my_dog = Dog("Buddy", "Golden Retriever")

# Calling the instance method
my_dog.bark()
