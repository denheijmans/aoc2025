from itertools import combinations

import numpy as np
from pulp import (
    PULP_CBC_CMD,
    LpInteger,
    LpMinimize,
    LpProblem,
    LpVariable,
    lpSum,
    value,
)
from tqdm import tqdm


def configure_lights(lights, buttons):
    """Solve using brute force: minimize button presses with exact light constraints"""
    for i in range(len(buttons) + 1):
        for bs in combinations(buttons, i):
            ls = np.zeros_like(lights, dtype=bool)
            for b in bs:
                ls[b] ^= True
            if np.array_equal(ls, lights):
                return i


def configure_counters(counters, buttons):
    """Solve using MILP: minimize button presses with exact counter constraints"""
    n_buttons = len(buttons)
    n_counters = len(counters)

    # Create the MILP problem
    prob = LpProblem("Counters", LpMinimize)

    # Decision variables: non-negative integer for each button (can press multiple times)
    x = [
        LpVariable(f"button_{i}", lowBound=0, cat=LpInteger)
        for i in range(n_buttons)
    ]

    # Objective: minimize total button presses
    prob += lpSum(x)

    # Constraints: for each counter, sum of button presses affecting it must equal target
    for counter_idx in range(n_counters):
        # Count which buttons affect this counter
        affecting_buttons = [
            i for i in range(n_buttons)
            if counter_idx in buttons[i]
        ]
        prob += lpSum(
            [x[i] for i in affecting_buttons]
        ) == counters[counter_idx]

    # Solve
    prob.solve(PULP_CBC_CMD(msg=False))

    return int(value(prob.objective))


with open("day_10/input.txt") as f:
    data = f.read().splitlines()

buttons = [[
    list(map(int, button[1:-1].split(',')))
    for button in line.split()[1:-1]
] for line in data]
lights = [np.array([
    light == '#'
    for light in line.split()[0][1:-1]
]) for line in data]
counters = [np.array(list(
    map(int, line.split()[-1][1:-1].split(','))
)) for line in data]

part_one = 0
part_two = 0

for i in tqdm(range(len(data)), leave=False):
    part_one += configure_lights(lights[i], buttons[i])

print(part_one)

for i in tqdm(range(len(data)), leave=False):
    part_two += configure_counters(counters[i], buttons[i])

print(part_two)
