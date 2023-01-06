# Problem 2
# Even Fibonacci Numbers

def sum_even_fib(ubound: int) -> int:
    f_low:  int = 1
    f_high: int = 2
    f_new:  int = f_low + f_high
    sum: int = 2
    while (f_new < ubound):
        f_low  = f_high
        f_high = f_new
        f_new  = f_low + f_high
        if (f_new % 2 == 0):
            sum += f_new
    return sum

def main():
    ubound = 4_000_000
    print(type(ubound))
    esum = sum_even_fib(ubound)
    print(f"ubound: {ubound}, sum = {esum}")

if __name__ == "__main__":
    main()

