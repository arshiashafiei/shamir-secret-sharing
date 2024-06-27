import random


def calculate_gf(prime: int):
    # if p is a prime
    return {int(x) for x in range(prime)}


def select_random_coefficients(prime, t):
    # TODO if p is a prime raise error
    # TODO if prime is smaller than n raise error
    return random.sample(range(prime), k=t-1)


