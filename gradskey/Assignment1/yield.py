import random

def generate_numbers_return():
    numbers = [random.randint(1, 100) for _ in range(100)]
    return numbers

def generate_numbers_yield():
    for _ in range(100):
        yield random.randint(1, 100)