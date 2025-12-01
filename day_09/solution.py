def get_area(c1, c2):
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)


with open("day_09/input.txt") as f:
    data = f.readlines()

# Parse coordinates
coords = [tuple(map(int, i.split(','))) for i in data]

# Part One
part_one = 0
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        area = get_area(coords[i], coords[j])
        if area > part_one:
            part_one = area

# Part Two
UPPER = 248
LOWER = 249
MIDDLE = 50000

# Find max area for upper section
max_y = min([
    c for c in coords
    if c[0] < coords[UPPER][0]
    and c[0] > MIDDLE
    and c[1] >= coords[UPPER][1]
], key=lambda x: x[1])[1]
upper_candidates = [
    c for c in coords
    if c[0] < MIDDLE
    and c[1] >= coords[UPPER][1]
    and c[1] <= max_y
]
upper_candidates = [
    c for c in upper_candidates
    if not any(
        other[1] < c[1] and other[0] > c[0]
        for other in upper_candidates
    )
]
max_upper_area = max(
    get_area(coords[UPPER], c)
    for c in upper_candidates
)

# Find max area for lower section
min_y = max([
    c for c in coords
    if c[0] < coords[LOWER][0]
    and c[0] > MIDDLE
    and c[1] <= coords[LOWER][1]
], key=lambda x: x[1])[1]
lower_candidates = [
    c for c in coords
    if c[0] < MIDDLE
    and c[1] <= coords[LOWER][1]
    and c[1] >= min_y
]
lower_candidates = [
    c for c in lower_candidates
    if not any(
        other[1] > c[1] and other[0] > c[0]
        for other in lower_candidates
    )
]
max_lower_area = max(
    get_area(coords[LOWER], c)
    for c in lower_candidates
)

# Take the larger of the two areas
part_two = max(max_upper_area, max_lower_area)

print(part_one)
print(part_two)
