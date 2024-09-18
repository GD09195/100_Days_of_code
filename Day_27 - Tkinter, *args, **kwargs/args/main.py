from numpy.ma.core import multiply


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