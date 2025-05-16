class Engine:
    def start(self):
        return "Engine started!"

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Composition: Car contains an Engine object

    def drive(self):
        return f"{self.model} is driving with: {self.engine.start()}"

# Create an Engine object
engine = Engine()

# Create a Car object and pass the Engine object to it
my_car = Car("Tesla Model S", engine)

# Access the Engine's method via the Car class
print(my_car.drive())
