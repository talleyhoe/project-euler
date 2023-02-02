# Problem 15
# Lattice Paths 

from math import comb

GRID_LENGTH = 20

def main():
    total_moves = GRID_LENGTH * 2
    down_moves = GRID_LENGTH
    route_count = comb(total_moves, down_moves)
    print(
        f"For a {GRID_LENGTH}x{GRID_LENGTH} grid, there are {route_count} "
        f"routes to move purposefully from one corner to the other"
    )
    return 0

if __name__ == "__main__":
    main()

