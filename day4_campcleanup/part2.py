# PROMPT:   https://adventofcode.com/2022/day/4#part2

import numpy as np

INPUT_FILE = 'input.txt'

pairs = []

# Read input file and parse based on newlines
with open(INPUT_FILE) as file:
    line_counter = 0
    
    for line in file:
        line_counter += 1
        pair = []
        
        group = line.rstrip().split(',')
        for assignment in group:
            sections = assignment.split('-')
            pair.append(int(sections[0]))
            pair.append(int(sections[1]))
        
        pairs.append(pair)


overlaps_boolean = []
pair_counter = 0

for pair in pairs:
    pair_counter += 1
    
    s1s = set(range(pair[0], pair[1]+1))
    s2s = set(range(pair[2], pair[3]+1))
    
    ov = False
    if s1s.intersection(s2s):
        ov = True
    
    overlaps_boolean.append(ov)
    print(f'Pair {pair_counter}: First range, {pair[0]}-{pair[1]}, Second range,{pair[2]}-{pair[3]}. Overlaps: {ov}')
    
# How many pairs overlap each other?
num_ov_pairs = np.sum(overlaps_boolean)

print(f'There are {num_ov_pairs} pairs where overlap occurs.')
print('Program completed.')