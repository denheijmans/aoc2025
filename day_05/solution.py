with open("day_05/input.txt") as f:
    data = f.read().split("\n\n")

# Parse ranges and IDs
rs = [
    tuple(map(int, r.split("-")))
    for r in data[0].splitlines()
]
ids = [
    int(id)
    for id in data[1].splitlines()
]

part_one = 0

# Count IDs that fall within any of the ranges
for id in ids:
    part_one += any(id >= r[0] and id <= r[1] for r in rs)

# Sort ranges by start value
rs_sorted = sorted(rs, key=lambda x: x[0])

# Merge overlapping or contained ranges
rs_merged = []
for a, b in rs_sorted:
    if not rs_merged or a > rs_merged[-1][1]:
        rs_merged.append((a, b))
    else:
        # overlap (or contained): extend the last merged range's end
        rs_merged[-1] = (rs_merged[-1][0], max(rs_merged[-1][1], b))

# Sum lengths of merged ranges
part_two = sum([r[1] - r[0] + 1 for r in rs_merged])

print(part_one)
print(part_two)
