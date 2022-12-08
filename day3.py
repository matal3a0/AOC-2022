#!/usr/bin/env python3

import sys

data = [line.strip() for line in sys.stdin.readlines()]

part1_sum = 0
part2_sum = 0

for d in data:
    l = int(len(d)/2)
    a = d[l:]
    b = d[:l]
    s = list(set(a).intersection(b))[0]
    
    if s.isupper():
        v = ord(s) - 38
    else:
        v = ord(s) - 96
    
    part1_sum += v

for k,_ in enumerate(data):
    if (k+1) % 3 != 0:
        continue
    
    s1 = data[k-2]
    s2 = data[k-1]
    s3 = data[k]

    s = list(set(s1).intersection(s2,s3))[0]
    print('s',s)

    if s.isupper():
        v = ord(s) - 38
    else:
        v = ord(s) - 96
    
    part2_sum += v

print('Part 1:', part1_sum)
print('Part 2:', part2_sum)
