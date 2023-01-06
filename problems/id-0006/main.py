# Problem 6
# Sum Square Difference

def sum_of_square(n: int) -> int:
    product: int = n * (n + 1) * ( (2*n) + 1 )
    quotient: int = product / 6
    return quotient

def square_of_sum(n: int) -> int:
    sum_product: int = n * (n + 1)
    sum: int = sum_product / 2
    square: int = sum**2
    return square

def main():
    ubound: int = 100
    diff_sum: int = 0
    sum_square: int = sum_of_square(ubound)
    square_sum: int = square_of_sum(ubound)
    diff: int = int(square_sum - sum_square)
    print(f"Diff between the sum of the squares of the first {ubound:,} "
          f"natural numbers,\nand the square of the sum: {diff:,}")
    return 0

if __name__ == "__main__":
    main()

