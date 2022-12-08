#!/usr/bin/env python3

import sys

data = [line.strip().split() for line in sys.stdin.readlines()]

part1_score = 0
part2_score = 0

for o, m in data:
    if o == 'A':
        if m == 'X':  
            part1_score += 4 # 3+1
            part2_score += 3 # 0+3
        elif m == 'Y': 
            part1_score += 8 # 6+2
            part2_score += 4 # 3+1 
        else:           
            part1_score += 3 # 0+3
            part2_score += 8 # 2+6
    elif o == 'B':
        if m == 'Y': 
            part1_score += 5 # 3+2
            part2_score += 5 # 2+3
        elif m == 'Z': 
            part1_score += 9 # 6+3
            part2_score += 9 # 6+3
        else:           
            part1_score += 1 # 0+1
            part2_score += 1 # 0+1
    elif o == 'C':
        if m == 'Z': 
            part1_score += 6 # 3+3
            part2_score += 7 # 6+1
        elif m == 'X': 
            part1_score += 7 # 6+1
            part2_score += 2 # 2+0
        else:           
            part1_score += 2 # 0+2
            part2_score += 6 # 3+3

print('Part 1:', part1_score)
print('Part 2:', part2_score)

