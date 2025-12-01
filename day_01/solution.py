with open('day_01/input.txt') as f:
    data = f.readlines()

steps = [int(i[1:]) * (2 * (i[0] == "R") - 1) for i in data]

part_one = 0
part_two = 0

pos = 50

for step in steps:
    div, pos, prev = *divmod(pos + step, 100), pos
    part_one += (pos == 0)
    part_two += abs(div) - (prev == 0 and div < 0) + (pos == 0 and step < 0)

print(part_one)
print(part_two)
