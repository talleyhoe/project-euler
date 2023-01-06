# Prime Functions

import math
import sys

def sieve_erathosthenes(ubound: int) -> list[int]:
    if (ubound < 1):
        print(f"Invalid range. Need upper bound > 1 (ubound:= {ubound})",
              file=sys.stderr)
        sys.exit(1)
    primes_bool: list[bool] = [True for i in range(2, (ubound + 1) )]
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

