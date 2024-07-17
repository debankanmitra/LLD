import time
def decorator(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__,"tooks", str((end - start)*1000) , "miliseconds to execute")
    return inner

@decorator
def calcsum(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

array = range(1,900000)
calcsum(array)