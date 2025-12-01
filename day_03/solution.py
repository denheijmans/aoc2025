def get_joltage(b, size):
    digits = [int(d) for d in str(b)]
    n = len(digits)
    joltage = [0] * size
    start = 0
    for d in range(size):
        for i in range(start, n - size + d + 1):
            if digits[i] > joltage[d]:
                joltage[d] = digits[i]
                start = i + 1
                if joltage[d] == 9:
                    break
    return int(''.join([str(d) for d in joltage]))


with open('day_03/input.txt') as f:
    data = f.readlines()

banks = [int(bank) for bank in data]

part_one = 0
part_two = 0

for bank in banks:
    part_one += get_joltage(bank, 2)
    part_two += get_joltage(bank, 12)

print(part_one)
print(part_two)
