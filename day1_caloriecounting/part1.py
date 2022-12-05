# PROMPT:   https://adventofcode.com/2022/day/1

import pathlib
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

# Find the max, which elf has it, and print.
max_calories = max(sum_calories)
max_elf = sum_calories.index(max_calories)

print(f'Elf no. {max_elf} has the most calories, with a total of {max_calories}.')
print('Program completed.')