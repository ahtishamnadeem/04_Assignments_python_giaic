class Counter:
    count = 0  # class variable to track object count

    def __init__(self):
        Counter.count += 1  # increment count when object is created

    @classmethod
    def display_count(cls):
        print("Total objects created:", cls.count)

# usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()
