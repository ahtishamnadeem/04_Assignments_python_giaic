class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display_info(self):
        return f"{self.name} works as a {self.role}"

class Department:
    def __init__(self, dept_name, employees):
        self.dept_name = dept_name
        self.employees = employees  
    def show_department_info(self):
        print(f"Department: {self.dept_name}")
        for employee in self.employees:
            print(employee.display_info())

# Create Employee objects independently
emp1 = Employee("Alice", "Manager")
emp2 = Employee("Bob", "Engineer")
emp3 = Employee("Charlie", "Technician")

# Create a Department object and pass references to Employee objects
it_department = Department("IT Department", [emp1, emp2, emp3])

# Access the Department's method that shows Employee details
it_department.show_department_info()
