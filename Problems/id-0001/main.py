# Problem 1
# Multiples of 3 or 5

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


def main():
    multiples = [3,5]
    ubound = 1000
    msum = sum_multiples(multiples, ubound)
    print(f"multiples: {multiples}, ubound: {ubound}\n Multiple's Sum: {msum}")

if __name__=="__main__":
    main()
