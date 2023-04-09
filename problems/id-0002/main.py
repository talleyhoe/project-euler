# Problem 2
# Even Fibonacci Numbers

def sum_even_fib(ubound):
    f_0 = 2
    f_3 = 8
    f_6 = f_0 + 4*f_3
    sum = 10
    while (f_6 < ubound):
        sum += f_6 # No need to check if even
        f_0 = f_3
        f_3 = f_6
        f_6 = f_0 + 4*f_3
    return sum

def main():
    ubound = 4_000_000
    print(type(ubound))
    esum = sum_even_fib(ubound)
    print(f"ubound: {ubound}, sum = {esum}")

if __name__ == "__main__":
    main()

