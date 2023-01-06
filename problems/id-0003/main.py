# Problem 3
# Largest prime factor 

import math

def calc_largest_prime(num: int) -> int:
    largest_prime : int = 0
    while ((num % 2) == 0):
        largest_prime = 2
        num /= 2

    while ((num % 3) == 0):
        largest_prime = 3
        num /= 3

    prime_ubound : int = int(math.sqrt(num))
    p : int = 5
    while ( (p < prime_ubound) and (p < num) ):
        while ( (num % p) == 0 ):
            largest_prime = p
            num /= p
        while ( ( num % (p + 2) ) == 0 ):
            largest_prime = (p + 2)
            num /= (p + 2)
        p += 6
    if (num > largest_prime):
        largest_prime = num
    return largest_prime



def main():
    number: int= 600851475143
    largest_prime: int = calc_largest_prime(number)
    print(f"largest_prime: {largest_prime:,}")
    return 0


if __name__ == "__main__":
    main()

