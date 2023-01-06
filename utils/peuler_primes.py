# Prime Functions

import math
import sys

def prime_density(ubound: int) -> float:
    """
    input: ubound - the upper bound of the number line to sieve through
    output: density - estimated number of primes below ubound
    """
    return ( ubound / math.log(ubound) )

def sieve_erathosthenes(ubound: int, primes: list[int] = None) -> list[int]:
    if (ubound < 1):
        print(f"Invalid range. Need upper bound > 1 (ubound:= {ubound})",
              file=sys.stderr)
        sys.exit(1)
    primes_bool: list[bool] = [True for i in range(2, (ubound + 1) )]
    bool_len: int = len(primes_bool)

    if (primes is not None):
        largest_prime: int = primes[-1]
        if (largest_prime > bool_len):
            largest_prime = bool_len
        for i in range(largest_prime):
            if ( i in primes ):
                continue
            primes_bool[i] = False

    for p in range( 2, int( math.sqrt(ubound) ) ):
        p_idx = p - 2
        if ( primes_bool[p_idx] ):
            for c in range( (2 * p), (ubound + 1), p ):
                c_idx = c - 2
                primes_bool[c_idx] = False
    primes: list[int] = []
    for i in range( len(primes_bool) ):
        if ( primes_bool[i] ):
            prime = i + 2
            primes.append(prime)
    return primes

