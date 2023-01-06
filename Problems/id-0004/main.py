# Problem 4
# Largest Palindrome Product

def is_palindrome(n: int) -> bool:
    str_num = str(n)
    length = len(str_num)
    for i in range(length):
        char_l2r = str_num[i]
        char_r2l = str_num[length - 1 - i]
        if (char_l2r != char_r2l):
            return False
    return True

# This would be faster if we checked from top down instead of bottom up
def largest_palindrome_product(digits: int):
    largest_palindrome = 0

    lbound = 10**(digits - 1)
    ubound = 10**(digits)
    for l in range(lbound, ubound):
        for u in range(l, ubound):
            prod = l * u
            if (prod > largest_palindrome):
                if ( is_palindrome(prod) ):
                    largest_palindrome = prod
    return largest_palindrome

    

def main():
    for digits in [2,3]:
        largest_palindrome = largest_palindrome_product(digits)
        print(f"digits: {digits}, largest_palindrome: {largest_palindrome:,}")

            
if __name__ == "__main__":
    main()

