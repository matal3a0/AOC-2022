#!/usr/bin/env python3

import sys

data = [line for line in sys.stdin.readlines()]

biggest = 0
calories = 0
sums = []

for d in data:
    if d != '\n':
        calories = calories + int(d)
    else:
        sums.append(calories)
        calories = 0

print('Part 1:', max(sums))
print('Part 2:', sum(sorted(sums)[-3:]))
