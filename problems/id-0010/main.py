# Problem 10
# Summation of Primes

import os, sys

utils = "../../utils"
path = os.path.realpath(utils)
sys.path.append(path)

from peuler_primes import sieve_erathosthenes

def main():
    ubound: int = 2_000_000
    primes: list[int] = sieve_erathosthenes(ubound)
    prime_sum: int = 0
    for p in primes:
        prime_sum += p

    print(f"Sum of primes below {ubound:,}: {prime_sum}")
    return 0


if __name__ == "__main__":
    main()

