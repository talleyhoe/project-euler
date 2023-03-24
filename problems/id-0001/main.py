# Problem 1
# Multiples of 3 or 5
#   Note: ubound is exclusive, like n in range(n)

Multiples = list[int]

# O(n)
def sum_multiples(multiples: Multiples, ubound: int) -> int:
    sum = 0
    for i in range(ubound):
        for m in multiples:
            if (i % m == 0):
                sum += i
                break
    return sum

def triangle_sum(ubound: int) -> int:
    return ( ubound * (ubound + 1) ) // 2 # Good conditioning

def get_quotient(ubound: int, modulus: int):
    ubound -= 1 
    return ubound // modulus

def optimized_sum(ubound: int) -> int:
    M3  =  3 * triangle_sum(get_quotient(ubound,  3))
    M5  =  5 * triangle_sum(get_quotient(ubound,  5))
    M15 = 15 * triangle_sum(get_quotient(ubound, 15))
    return M3 + M5 - M15



def main():
    multiples = [3,5]
    ubound = 1000
    msum = sum_multiples(multiples, ubound)
    opt_sum = optimized_sum(ubound)
    print(f"Loops:\n\tmultiples: {multiples}, ubound: {ubound}\n"
          f"\tMultiple's Sum: {msum}")
    print(f"Triangle Optimization:\n\tmultiples: [3, 5], ubound: {ubound}\n"
          f"\tMultiple's Sum: {opt_sum}")

if __name__=="__main__":
    main()
