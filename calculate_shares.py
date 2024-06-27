import random


def make_polynomial(secret: int, prime: int, t: int) -> list[int]:
    """Evaluates polynomial coefficients"""
    # The last coefficient is S = f(0)
    others = random.sample(range(prime), k=t-1)
    coefficients = others + [secret]
    return coefficients


def evaluate_polynomial(coefficients: list[int], x: int, prime: int) -> int:
    """Evaluates polynomial at x,
    (A(t-1) * x + A(t-2)) mod p * x + A(t-3) mod p
    and so on..."""
    accum = 0
    for coeff in coefficients:
        accum = ((accum * x) + coeff) % prime
    return accum


def make_shares(secret: int, t: int, n: int, prime: int) -> list[int]:
    """
    Generates a random shamir pool for a given secret, returns share points.
    """
    # TODO if p is a prime raise error
    if t > n:
        raise ValueError("Error: t is bigger than n!")
    if prime <= n:  # Because you give the secret to someone
        raise ValueError("Error: the number of shares is bigger than prime!")

    coefficients = make_polynomial(secret, prime, t)

    print("=== The polynomial ===")
    for i, coeff in enumerate(coefficients):
        print(f"[({coeff}) * x^({t - i - 1})]", end=" + ")
    print()
    print("======")

    points = [(i, evaluate_polynomial(coefficients, i, prime))
              for i in range(1, n + 1)]  # Y_i's set
    return points


if __name__ == "__main__":
    S = int(input("--Please enter your Secret: "))
    t = int(input("--Please enter minimum threshold(t): "))
    n = int(input("--Please enter number of shares(n): "))
    p = int(input("--Please enter the field number(p): "))

    for share in make_shares(S, t, n, p):
        print(f"(Xi={share[0]}, Yi={share[1]})")
