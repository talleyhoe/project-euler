# Problem 14
# Longest Collatz Sequence

import sys

SEED_UBOUND = 1_000_000

def collatz_sequence(term: int) -> int:
    length = 1
    while (term > 1):
        if (term % 2):
            length += 2
            term = (term - 1) // 2
            term = (3 * term) + 2
        else:
            length += 1
            term = term // 2
    return length

def main():
    max_seed = 13
    max_length = 10
    for seed in range(max_seed, SEED_UBOUND):
        seed_length = collatz_sequence(seed)
        if (seed_length > max_length):
            max_seed = seed
            max_length = seed_length
    print(f"Longest collatz sequence below {SEED_UBOUND:,} is {max_seed}")

if __name__ == "__main__":
    main()

