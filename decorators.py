# Write a Python program to create a decorator function to measure the execution time of a function

import time

def measure_execut_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execut_time = end_time - start_time
        print(f"Execution time is: {execut_time}")
        return result
    return wrapper


@measure_execut_time
def calculate_multiply(numbers):
    tot = 1
    for i in numbers:
        tot *= i
    return tot

result = calculate_multiply([5, 4, 2, 1])
print(f"The result is: {result}")

