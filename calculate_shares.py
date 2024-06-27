import random


def calculate_gf(prime: int):
    # if p is a prime
    return {int(x) for x in range(prime)}


def select_random_coefficients(prime, t):
    # TODO if p is a prime raise error
    # TODO if prime is smaller than n raise error
    return random.sample(range(prime), k=t-1)


def make_polynomial(secret, prime, t):
    """Evaluates polynomial coefficients"""
    # The last coefficient is S = f(0)
    coefficients = select_random_coefficients(prime, t) + [secret]
    return coefficients


def evaluate_polynomial(coefficients, x, prime):
    """Evaluates polynomial at x,
    (A(t-1) * x + A(t-2)) mod p * x + A(t-3) mod p
    and so on..."""
    accum = 0
    for coeff in coefficients:
        accum *= x
        accum += coeff
        accum %= prime
    return accum
