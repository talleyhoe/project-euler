# Problem 5
# Smallest Multiple

import math
import sys

PrimeCnt = dict[int,int]

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

def prime_decompositon(num: int, primes: list[int]) -> PrimeCnt:
    prime_cnt: PrimeCnt = {}
    for p in primes:
        prime_cnt[p] = 0
        while ( (num % p) == 0 ):
            prime_cnt[p] += 1
            num /= p
    return prime_cnt

def init_prime_count(primes: list[int]) -> PrimeCnt:
    prime_cnt = {}
    for p in primes:
        prime_cnt[p] = 0
    return prime_cnt

def update_prime_count(sys_cnt: PrimeCnt, num_cnt: PrimeCnt) -> PrimeCnt:
    if (sys_cnt.keys() != num_cnt.keys() ):
        print(f"Bad prime keys.\n"
              f"Sys-len: {len(sys_cnt)}, Num-len: {len(num_cnt)}",
              file=sys.stderr)
        sys.exit(1)
    for (p, c) in sys_cnt.items():
        num_pcnt = num_cnt.get(p)
        if (num_pcnt == None):
            print(f"Prime not found in num. Prime: {p}", file=sys.stderr)
            sys.exit(1)
        if (num_pcnt > c):
            sys_cnt[p] = num_pcnt
    return sys_cnt

def gen_least_multiple(prime_decomp: PrimeCnt):
    product = 1
    for (p, c) in prime_decomp.items():
        for mult in range(c):
            product *= p
    return product

def main():
    ubound: int = 20 
    primes: list[int] = sieve_erathosthenes(ubound)
    prime_cnt: PrimeCnt = init_prime_count(primes)
    for i in range(1, ubound + 1):
        num_decomp: PrimeCnt = prime_decompositon(i, primes)
        prime_cnt = update_prime_count(prime_cnt, num_decomp)
    least_multiple = gen_least_multiple(prime_cnt)
    print(f"Least multiple below {ubound:,}: {least_multiple:,}")
    return 0

if __name__ == "__main__":
    main()

