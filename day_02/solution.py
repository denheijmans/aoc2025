from tqdm import tqdm


def is_valid_part_one(id):
    digits = [int(d) for d in str(id)]
    n = len(digits)
    if n % 2 == 0:
        half = n // 2
        if digits[:half] == digits[half:]:
            return False
    return True


def is_valid_part_two(id):
    digits = [int(d) for d in str(id)]
    n = len(digits)
    divisors = [d for d in range(1, n) if n % d == 0]
    for d in divisors:
        groups = [digits[i:i + d] for i in range(0, n, d)]
        if all(g == groups[0] for g in groups[1:]):
            return False
    return True


def sum_invalid_ids(r, f):
    count = 0
    for i in range(r[0], r[1] + 1):
        if not f(i):
            count += i
    return count


with open('day_02/input.txt') as f:
    data = f.readline()

ranges = [tuple(map(int, r.split('-'))) for r in data.split(',')]

part_one = 0
part_two = 0

for r in tqdm(ranges, leave=False):
    part_one += sum_invalid_ids(r, is_valid_part_one)

print(part_one)

for r in tqdm(ranges, leave=False):
    part_two += sum_invalid_ids(r, is_valid_part_two)

print(part_two)
