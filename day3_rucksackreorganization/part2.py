# PROMPT:   https://adventofcode.com/2022/day/3#part2

import numpy as np

INPUT_FILE = 'input.txt'

elf_badges = []

def convert_letter_to_priority(letter):
    '''Uses ord() to get priority number of each letter.'''
    priority = 0
    
    # a to z have priority 1-26; ord('a') is 97
    if letter.islower():
        priority = ord(letter) - 96
    # A to Z have priority 27-52; ord('A') is 65
    elif letter.isupper():
        priority = ord(letter) - 64 + 26
        
    return priority


# Read input file and parse based on newlines
with open(INPUT_FILE) as file:
    line_counter = 0
    lines = []
    
    for line in file:
        line_counter += 1
        lines.append(line.rstrip())
        
        if line_counter%3 ==0:
            
            for item in lines[0]:
                if item in lines[1] and item in lines[2]:
                    elf_badges.append(item)
                    break
            
            lines = []
            
# Convert badges to priorities
elf_priorities = []
for badge in elf_badges:
    elf_priorities.append(convert_letter_to_priority(badge))

# # Sum each rucksack's priority
total_priority = np.sum(elf_priorities)

print(f'The total priority is {total_priority}.')
print('Program completed.')