class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

# Create an object of class D
obj = D()

# Call the show() method
obj.show()

# Check the MRO (Method Resolution Order)
print("Method Resolution Order:", D.__mro__)
