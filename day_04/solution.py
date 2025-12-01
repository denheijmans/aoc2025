from copy import deepcopy


def accessible(grid, i, j):
    """
    Check if the cell at (i, j) is accessible. A cell is accessible
    if it contains '@' and has fewer than 4 adjacent '@' cells.
    """
    if grid[i][j] != "@":
        return False
    count = 0
    for y in range(-1, 2):
        for x in range(-1, 2):
            if x == 0 and y == 0:
                continue
            count += grid[i + y][j + x] == "@"
    return count < 4


with open("day_04/input.txt") as f:
    data = f.read().splitlines()

# Pad the grid with empty cells to avoid boundary checks
width = len(data[0])
height = len(data)
empty_row = ["."] * (width + 2)
grid = [empty_row]
for row in data:
    grid.append([".", *row, "."])
grid.append(empty_row)

# Part One
part_one = 0
for i in range(1, width + 1):
    for j in range(1, height + 1):
        if accessible(grid, i, j):
            part_one += 1

# Part Two
part_two = 0
new_grid = deepcopy(grid)
while True:
    count = 0
    for i in range(1, width + 1):
        for j in range(1, height + 1):
            if accessible(grid, i, j):
                part_two += 1
                count += 1
                new_grid[i][j] = "."
    grid = new_grid
    new_grid = deepcopy(grid)
    if count == 0:
        break

print(part_one)
print(part_two)
