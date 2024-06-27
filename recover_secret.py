from calculate_shares import make_shares


def mod_inverse(a: int, prime: int) -> int:
    """
    Inverse of A can be computed via the extended Euclidean algorithm.
    """
    x = 0
    last_x = 1
    old_prime = prime
    while prime != 0:
        quot = a // prime
        a, prime = prime, a % prime
        x, last_x = last_x - quot * x, x
        # r_i+1 = r_i-1 - r_i * q_i not exactly this but you get the point.
    return last_x % old_prime


def recover_secret(shares: list[tuple[int, int]], prime: int) -> int:
    """Recover the secret from share points
    (points (x,y) on the polynomial).
    """
    if len(shares) < 3:
        raise ValueError("need at least three shares")
    sigma = 0
    for x, y in shares:
        pi = y % prime  # Y_i * ...
        # print(f"--Y= {y}")
        for j in range(len(shares)):
            if x != shares[j][0]:  # j != i
                # X_j / (X_j - X_i)
                # print(f"X_j= {shares[j][0]}")
                # print(f"(X_j - X_i)= {shares[j][0] - x}")
                # print(mod_inverse(shares[j][0] - x, prime))
                pi *= (shares[j][0]
                       * mod_inverse((shares[j][0] - x), prime)) % prime
                # print(pi % prime)
        sigma += pi % prime
    return sigma % prime


def main():
    t = int(input("--Please enter number of shares(t): "))
    prime = int(input("--Please enter the field number(p): "))
    shares = []
    for _ in range(t):
        x = int(input("--Please enter X_i: "))
        y = int(input("--Please enter Y_i: "))
        shares.append((x, y))

    print("Recovered Secret:")
    print(recover_secret(shares, prime))


def test_secret_finding_full_shares():
    S = int(input("--Please enter your Secret: "))
    t = int(input("--Please enter minimum threshold(t): "))
    n = int(input("--Please enter number of shares(n): "))
    p = int(input("--Please enter the field number(p): "))

    precomputed_shares = make_shares(S, t, n, p)

    for share in precomputed_shares:
        print(f"(Xi={share[0]}, Yi={share[1]})")

    print("Recovered Secret:")
    print(recover_secret(precomputed_shares, p))


def test_secret_finding_input_as_shares():
    S = int(input("--Please enter your Secret: "))
    t = int(input("--Please enter minimum threshold(t): "))
    n = int(input("--Please enter number of shares(n): "))
    p = int(input("--Please enter the field number(p): "))

    precomputed_shares = make_shares(S, t, n, p)

    for share in precomputed_shares:
        print(f"(Xi={share[0]}, Yi={share[1]})")

    t = int(input("--Please enter number of shares(t): "))
    shares = []
    for _ in range(t):
        x = int(input("--Please enter X_i: "))
        y = int(input("--Please enter Y_i: "))
        shares.append((x, y))

    print("Recovered Secret:")
    print(recover_secret(shares, p))


if __name__ == "__main__":
    main()
    # test_secret_finding_full_shares()
    # test_secret_finding_input_as_shares()
