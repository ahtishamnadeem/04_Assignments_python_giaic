class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # Public
        self._salary = salary      # Protected
        self.__ssn = ssn           # Private

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)

# Creating an object
emp = Employee("Ayesha", 80000, "123-45-6789")

# Accessing variables from outside
print("🌐 Public (name):", emp.name)         # ✅ Accessible
print("🔒 Protected (_salary):", emp._salary) # ⚠️ Accessible but not recommended


# Accessing private variable correctly 
print("🔐 Private (__ssn) via name mangling:", emp._Employee__ssn)

# Or use class method
print("\nFrom method:")
emp.show_details()
