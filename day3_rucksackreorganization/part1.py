# PROMPT:   https://adventofcode.com/2022/day/3

import numpy as np

INPUT_FILE = 'input.txt'

rucksacks = []

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
    for line in file:
        line_counter += 1
        
        items = line.rstrip()
        split_idx = int(len(items)/2)
        assert len(items)/2 > 0, f'Item array length should be even, not odd!'
        
        left_compartment = items[:split_idx]
        right_compartment = items[split_idx:]
        
        for item in left_compartment:
            right_idx_match = right_compartment.find(item)
            if right_idx_match == -1:
                # print(f'Rucksack {line_counter}: No matching item found.')
                continue
            else:
                priority = convert_letter_to_priority(right_compartment[right_idx_match])
                rucksacks.append(priority)
                print(f'Rucksack {line_counter}: Matching item {right_compartment[right_idx_match]}, with priority {priority}.')
                break

# # Sum each rucksack's priority
total_priority = np.sum(rucksacks)

print(f'The total priority is {total_priority}.')
print('Program completed.')