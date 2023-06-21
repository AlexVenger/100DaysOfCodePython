def add(*args):
	s = 0
	for arg in args:
		s += arg
	return s


def calculate(n, **kwargs):
	n += kwargs["add"]
	n *= kwargs["multiply"]
	return n


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(calculate(3, add=3, multiply=5))


class Car:
	def __init__(self, **kwargs):
		self.make = kwargs.get("make")
		self.model = kwargs.get("model")


car = Car(make="Nissan")
print(car)
