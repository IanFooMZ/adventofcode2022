# PROMPT:   https://adventofcode.com/2022/day/1#part2

import pathlib
import numpy as np
INPUT_FILE = 'input.txt'

calories = []

# Read input file and parse based on newlines
with open(INPUT_FILE) as file:
    line_counter = 0
    elf = []
    
    for line in file:
        line_counter += 1
        if line.rstrip() in ['']:
            calories.append(elf)
            elf = []
        else:
            try:
                elf.append(int(line.rstrip()))
            except Exception as Ex:
                print(f'At line {line_counter} of the input file:')
                print(type(Ex))     # the exception instance
                print(Ex.args)      # arguments stored in .args]

# Sum each elf's calories
sum_calories = []
for elf in calories:
    sum_calories.append(sum(elf))

# Find the top three, and which elves have them.
sum_calories = np.array(sum_calories)
idxs = np.argpartition(sum_calories, -3)[-3:]
maxs = sum_calories[idxs]
max_calories = np.sum(maxs)

print(f'Elves nos. {idxs} have the most calories, with {maxs} calories respectively. Their total is {max_calories}.')
print('Program completed.')