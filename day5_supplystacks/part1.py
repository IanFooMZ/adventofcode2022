# PROMPT:   https://adventofcode.com/2022/day/4

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


fully_contains_boolean = []
pair_counter = 0

for pair in pairs:
    pair_counter += 1
    
    fc = False
    if pair[0] <= pair[2] and pair[1] >= pair[3] or pair[2] <= pair[0] and pair[3] >= pair[1]:  
        fc = True
    
    fully_contains_boolean.append(fc)
    print(f'Pair {pair_counter}: First range, {pair[0]}-{pair[1]}, Second range,{pair[2]}-{pair[3]}. Fully Contains: {fc}')
    
# How many pairs fully contain each other?
num_fc_pairs = np.sum(fully_contains_boolean)

print(f'There are {num_fc_pairs} pairs where full containment occurs.')
print('Program completed.')