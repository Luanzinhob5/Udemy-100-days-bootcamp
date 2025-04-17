# The problem is: the range dont count 20
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("you got it")
my_function()