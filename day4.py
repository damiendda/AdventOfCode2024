import sys
import re

arg_input = sys.argv[1]

with open(arg_input, 'r') as f:
    data = f.readlines()

    H, W = len(data), len(data[0])-1 
    grid = {(x,y):data[x][y] for x in range(H) for y in range(W)}
    deltas = [(dy,dx) for dy in [-1,0,1] for dx in [-1,0,1] if (dx!=0 or dy!=0)]
    target = "XMAS"

    print(deltas)
    count = 0
    for x, y in grid:
        for dx, dy in deltas:
            candidate = "".join(grid.get((x+dx*i, y+dy*i), "") for i in range(len(target)))
            if candidate == target:
                count += 1
                print(candidate)
                print(f"{x} {y}")

    print(f"PART 1 : {count}")

    # Part 2 : x-MAS
    count = 0

    for x, y in grid:
        if grid[x,y] == 'A':
            top = grid.get((x-1,y-1), "")+grid.get((x+1,y+1), "")
            bot = grid.get((x+1,y-1), "")+grid.get((x-1,y+1), "")
            print(f"{x} {y} b:{bot} t:{top}")
            if (top == "MS" or top == "SM") and (bot == "MS" or bot == "SM"):
                count += 1
    print(f"PART 2 : {count}")
