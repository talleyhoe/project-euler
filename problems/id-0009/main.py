# Problem 9
# Special Pythagorean Triplet

import math
import sys

def euclid_ints(sum_target: int) -> tuple[int]:
    ubound_mn: int = int( math.sqrt(sum_target) + 1 )
    c: int = 0
    for n in range(1, ubound_mn):
        for m in range( (n + 1), ubound_mn ):
            c_val: int = int( 2 * ( (m**2) + (m * n) ) )
            if ( c_val == sum_target ):
                return (m, n)

    print(f"Didn't find a euclid match. sum_target: {sum_target}")
    sys.exit(1)

def main():
    target: int = 1000
    mn_tup = euclid_ints(target)
    m = mn_tup[0]
    n = mn_tup[1]
    a = ( (m**2) - (n**2) )
    b = ( 2 * m * n )
    c = ( (m**2) + (n**2) )
    product: int = ( a * b * c )
    print(f"Pythagorean triplet (a,b,c) = ({a},{b},{c}), Product: {product}")


if __name__ == "__main__":
    main()

