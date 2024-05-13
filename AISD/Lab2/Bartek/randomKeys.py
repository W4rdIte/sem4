import random

def generate_random_keys(n):
    return [random.randint(0, 2*n-1) for _ in range(n)]
