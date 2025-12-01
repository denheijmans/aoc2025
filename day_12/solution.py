from dataclasses import dataclass

import numpy as np


@dataclass
class Region:
    width: int
    height: int
    shape_counts: list[int]

    def enough_space(self, shapes: list[np.ndarray]):
        """Check if the region has enough space for all shapes"""
        total_area = self.width * self.height
        shapes_area = 0
        for i, n in enumerate(self.shape_counts):
            shapes_area += n * shapes[i].sum()
        return total_area >= shapes_area


with open("day_12/input.txt") as f:
    data = f.read().split("\n\n")

# Parse shapes and regions
shapes = [np.array([
    [1 if char == "#" else 0 for char in line]
    for line in shape.splitlines()[1:]
]) for shape in data[:-1]]
regions = [Region(
    *list(map(int, region.split(": ")[0].split("x"))),
    list(map(int, region.split(": ")[1].split())))
    for region in data[-1].splitlines()
]

# Part One
part_one = 0
for region in regions:
    part_one += region.enough_space(shapes)
print(part_one)
