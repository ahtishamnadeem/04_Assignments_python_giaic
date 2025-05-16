# Countdown class implementing Iterable
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    # Implement __iter__ method 
    def __iter__(self):
        return self  

    # Implement __next__ method to return the next countdown value
    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop iteration when countdown reaches below 0
        value = self.current
        self.current -= 1
        return value


countdown = Countdown(5)  # Start counting down from 5
for number in countdown:
    print(number)
