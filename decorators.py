import time
def time_it(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__,"tooks", str((end - start)*1000) , "miliseconds to execute")
    return inner

@time_it
def calcsum(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

array = range(1,900000)
calcsum(array)

# ==============================================================================================================

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
