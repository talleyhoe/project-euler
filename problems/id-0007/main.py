# Problem 7
# 10001st Prime

import sys, os
import math

utils = "../../utils"
path = os.path.realpath(utils)
sys.path.append(path)

from peuler_primes import sieve_erathosthenes

def check_log(value):
    if (value <= 0):
        print(f"Invalid range for log(x). Need x > 0 (x: {value})",
              file=sys.stderr)
        sys.exit(1)
    return 0

def prime_density(ubound: int) -> float:
    """
    input: ubound - the upper bound of the number line to sieve through
    output: density - estimated number of primes below ubound
    """
    check_log(ubound)
    return ( ubound / math.log(ubound) )

def prime_density_derivative(ubound: int) -> float:
    check_log(ubound)
    top = math.log(ubound) - 1
    bottom = ( math.log(ubound) )**2
    return (top / bottom)

def newtons_method(func_value, func_derivative, 
                  tolerance=20, guess=5, max_steps=200):
    point = guess
    value = func_value(point)
    
    steps: int = 0
    while ( (abs(value) > tolerance) and (steps < max_steps) ): 
        point -= ( func_value(point) / func_derivative(point) )
        value = func_value(point)
        steps += 1
    return point
    

def main():
    max_prime_cnt: int = 10_001
    ubound_stride: int = ( 1 << 10)

    root_func = lambda n: prime_density(n) - max_prime_cnt
    ubound: int = int( newtons_method(root_func, prime_density_derivative) )
    print(f"first prime pass. ubound: {ubound:,}")
    primes: list[int] = sieve_erathosthenes(ubound)
    prime_cnt: int = len(primes)
    while ( prime_cnt < max_prime_cnt ):
        primes = sieve_erathosthenes(ubound)
        prime_cnt = len(primes)
        ubound += ubound_stride

    print(f"Prime {max_prime_cnt}: {primes[max_prime_cnt - 1]:,}")
    return 0


if __name__ == "__main__":
    main()

