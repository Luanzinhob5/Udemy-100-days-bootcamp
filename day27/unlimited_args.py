# def add(*args):
#     return sum(args)
# print(add(1,2,5,4,50,100))

    
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2,add=3,multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)