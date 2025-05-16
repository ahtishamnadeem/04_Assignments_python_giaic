class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    # Getter for the price
    @property
    def price(self):
        return self._price

    # Setter to update the price
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value

    # Deleter to delete the price
    @price.deleter
    def price(self):
        print(f"Deleting price of {self.name}")
        del self._price


# Creating an instance of the Product class
product = Product("Laptop", 1000)

# Using the getter to get the price
print(f"Product Name: {product.name}")
print(f"Product Price: {product.price}")

# Using the setter to update the price
product.price = 1200
print(f"Updated Price: {product.price}")

# Trying to set a negative price
product.price = -500  

# Deleting the price
del product.price

# Trying to access the price after deletion
try:
    print(f"Product Price after deletion: {product.price}")
except AttributeError:
    print("Price has been deleted.")
