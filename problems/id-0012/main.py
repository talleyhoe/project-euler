# Problem 12
# Highly divisible triangular number
#
# Ans: ~ 76,500,000
# Runtimes: sub-linear (astronomic)
# This could be faster using trial division and line search methods (linear),
# but is a better solution for larger desired divisor counts. 

import os, sys

utils = "../../utils"
path = os.path.realpath(utils)
sys.path.append(path)

from peuler_primes import *

def triangle_number(n) -> int:
    return int( ( n * (n + 1) ) / 2 )

def count_divisors(prime_decomp: PrimeCnt) -> int:
    total_divisors: int = 1
    for p_cnt in prime_decomp.values():
        total_divisors *= (p_cnt + 1)
    return total_divisors

def main():
    min_divisors: int = 500
    triangle_idx: int = 12300
    
    t_num: int = triangle_number(triangle_idx)
    primes: list[int] = sieve_erathosthenes(t_num)
    prime_cnt: PrimeCnt = prime_decomposition(t_num, primes)
    num_divisors: int = count_divisors(prime_cnt)

    while (num_divisors < min_divisors):
        t_num = triangle_number(triangle_idx)
        primes = sieve_erathosthenes(t_num)
        prime_cnt = prime_decomposition(t_num, primes)
        num_divisors = count_divisors(prime_cnt)
        # print(f"\tt-num: {t_num:3}, div_cnt: {num_divisors: 3}")
        # print(f"t_num: {t_num}, primelen: {len(primes)}, largestprime: {primes[-1]}")
        # print(f"primelen: {len(primes)}, largestprime: {primes[-1]}")
        triangle_idx += 1
    print(f"First triangle number with over {min_divisors} "
          f"divisors is: {t_num}")
    return 0


if __name__ == "__main__":
    main()

