class Multiplier:
    def __init__(self, factor):
        self.factor = factor  

    # Define __call__ to make instances callable
    def __call__(self, value):
        return value * self.factor  # Multiply the value by the factor


# Create an instance of the Multiplier class with a factor of 5
multiply_by_5 = Multiplier(5)

# Test the callable() function
print("Is 'multiply_by_5' callable?", callable(multiply_by_5))  # This should return True

# Call the instance like a function
result = multiply_by_5(10)  # Calling the object as a function, multiplying 10 by 5
print(f"Result of calling the object with 10: {result}")
