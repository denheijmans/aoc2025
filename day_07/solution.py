with open("day_07/input.txt") as f:
    data = f.readlines()

# Parse the input
start = data[0].index('S')
bs = set([start])
pss = [[
    i for i, c in enumerate(line) if c == '^'
] for line in data[1:]]

# Initialize counts
part_one = 0
ts = [0] * len(data[0])
ts[start] = 1

# Simulate the tachyon beam splits
for ps in pss:
    next_bs = bs.copy()
    for p in ps:
        if p in bs:
            # Split the beam
            next_bs.remove(p)
            next_bs.add(p - 1)
            next_bs.add(p + 1)

            # Count total splits
            part_one += 1

            # Update timelines
            ts[p - 1] += ts[p]
            ts[p + 1] += ts[p]
            ts[p] = 0
    bs = next_bs.copy()

# Sum up all timelines
part_two = sum(ts)

print(part_one)
print(part_two)
