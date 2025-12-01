import numpy as np


def aggregate(numbers, operators):
    """Aggregate numbers based on the provided operators."""
    count = 0
    for i in range(len(operators)):
        if operators[i] == '+':
            count += np.sum(numbers[i])
        elif operators[i] == '*':
            count += np.prod(numbers[i])
    return count


with open("day_06/input.txt") as f:
    data = f.readlines()

operators = data[-1].split()

# Part One
n1 = np.array([
    list(map(int, row.split()))
    for row in data[:-1]
]).T
part_one = aggregate(n1, operators)

# Part Two
n2 = np.array([list(i) for i in data[:-1]]).T
n2 = [''.join(x).strip() for x in n2]
n2 = ','.join(n2)[:-1].split(',,')
n2 = [list(map(int, n.split(','))) for n in n2]
part_two = aggregate(n2, operators)

print(part_one)
print(part_two)
