# Python Programming Assignments

This repository contains 21 Python assignments that cover various concepts of Python programming, including object-oriented programming, decorators, exceptions, iteration, and more. 
These assignments were created to improve and demonstrate my understanding of Python concepts.

## 1. Using `self`
Created a `Student` class with attributes `name` and `marks`, initialized using `self` keyword, and displayed student details using a `display()` method.

## 2. Using `cls`
Created a `Counter` class to keep track of how many objects have been created. Used a class method with `cls` to manage and display the count.

## 3. Public Variables and Methods
Developed a `Car` class with a public variable `brand` and a public method `start()`. Instantiated the class and accessed both from outside the class.

## 4. Class Variables and Class Methods
Built a `Bank` class with a class variable `bank_name` and a class method `change_bank_name(cls, name)` to change the bank name, affecting all instances.

## 5. Static Methods
Created a `MathUtils` class with a static method `add(a, b)` that returns the sum without using class or instance variables.

## 6. Constructors and Destructors
Developed a `Logger` class that prints a message when an object is created (constructor) and destroyed (destructor).

## 7. Access Modifiers: Public, Private, and Protected
Created an `Employee` class with a public variable `name`, a protected variable `_salary`, and a private variable `__ssn`. Tried accessing all three variables from an object and documented the results.

## 8. The `super()` Function
Created a `Person` class with a constructor that sets the name. Inherited a class `Teacher` from it, added a subject field, and used `super()` to call the base class constructor.

## 9. Abstract Classes and Methods
Used the `abc` module to create an abstract class `Shape` with an abstract method `area()`. Inherited a class `Rectangle` that implements `area()`.

## 10. Instance Methods
Created a `Dog` class with instance variables `name` and `breed`, and added an instance method `bark()` to print a message including the dog's name.

## 11. Class Methods
Created a `Book` class with a class variable `total_books`. Added a class method `increment_book_count()` to increase the count when a new book is added.

## 12. Static Methods
Developed a `TemperatureConverter` class with a static method `celsius_to_fahrenheit(c)` that returns the Fahrenheit value from Celsius.

## 13. Composition
Created an `Engine` class and a `Car` class, using composition by passing an `Engine` object to the `Car` class during initialization. Accessed a method of the `Engine` class via the `Car` class.

## 14. Aggregation
Created a `Department` class and an `Employee` class, using aggregation by having a `Department` object store a reference to an `Employee` object that exists independently.

## 15. Method Resolution Order (MRO) and Diamond Inheritance
Created a method resolution order using four classes: `A`, `B`, `C`, and `D`. Class `D` inherits from both `B` and `C`, and we observed the MRO when calling a method from class `D`.

## 16. Function Decorators
Wrote a decorator function `log_function_call` that prints "Function is being called" before a function executes. Applied it to a `say_hello()` function.

## 17. Class Decorators
Created a class decorator `add_greeting` that adds a `greet()` method to a class `Person`, returning "Hello from Decorator!". Applied it to the `Person` class.

## 18. Property Decorators: `@property`, `@setter`, and `@deleter`
Created a `Product` class with a private attribute `_price`. Used `@property` to get the price, `@price.setter` to update it, and `@price.deleter` to delete it.

## 19. `callable()` and `__call__()`
Created a `Multiplier` class with an `__init__()` method to set a factor. Defined a `__call__()` method that multiplies an input by the factor. Tested it using `callable()` and by calling the object like a function.

## 20. Creating a Custom Exception
Created a custom exception `InvalidAgeError` and wrote a function `check_age(age)` that raises this exception if the age is less than 18. Handled it using `try...except`.

## 21. Make a Custom Class Iterable
Created a `Countdown` class that implements `__iter__()` and `__next__()` methods to make it iterable, counting down to 0.

---

## Made and Managed by | CodeWithAhtii.
