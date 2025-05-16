# Custom exception class for invalid age
class InvalidAgeError(Exception):
    # Initialize with an optional custom message
    def __init__(self, message="Age must be 18 or older."):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        # Raise the custom exception if age is less than 18
        raise InvalidAgeError(f"Invalid age: {age}. You must be 18 or older.")
    else:
        print("Age is valid!")


try:
    # Example age input
    user_age = int(input("Enter your age: "))
    
    # Call the check_age function
    check_age(user_age)
    
except InvalidAgeError as e:
    # Handle the custom exception
    print(f"Error: {e}")
except ValueError:
    # Handle invalid input (non-integer)
    print("Invalid input! Please enter a valid number for age.")
