#Define an unlimited amount of positional arguments
#args will be a tuple
def add(*args):
    print(args)
    print(type(args))

    return sum(args)

print(add(1, 3, 4, 5))


#Define an unlimited amount of keyword arguments
#kwargs will be a Dictionary
def calculate(base, **kwargs):
    print(kwargs)
    print(type(kwargs))
    result: int = base
    result += kwargs["add"]
    result *= kwargs["multiply"]
    return result

print(calculate(2, add=3, multiply=5))

#Creating a class with **kwargs
class Car:
    def __init__(self, **kwargs):
        #Accesing dictionaries with squares brackets

        #self.make = kwargs['make']
        #self.model = kwargs['model']

        #Accessing dictionaries with .get() function
        #If the key doesnt exists, .get() would return None
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')

my_car = Car(make="Nissan", model="1995")
print(my_car.make)
print(my_car.model)