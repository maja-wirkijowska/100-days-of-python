def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(3, 4, 5, 6, 7, 8))
print(add(67, 54, 43))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["mult"]
    return n


print(calculate(2, add=3, mult=5))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


car = Car(make="Nissan")
print(car.model)
print(car.make)
