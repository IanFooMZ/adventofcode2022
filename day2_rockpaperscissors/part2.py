# PROMPT:   https://adventofcode.com/2022/day/2#part2

import pathlib
import numpy as np
INPUT_FILE = 'input.txt'

rounds = []

def calc_score(round):
    '''Takes as input an array of two letters e.g. ['A','Z'] and converts them into a score based on the algorithm presented in the URL above.'''
    
    shape_table = {'A': 1, 'B': 2, 'C': 3}
    outcome_table = {'X': 1, 'Y': 2, 'Z': 3}
    
    # Outcome logic table can be seen here: https://i.imgur.com/0NtcgfD.png
    outcome_score_arr = np.array(([3,1,2], [1,2,3], [2,3,1]))
    
    outcome_score = (outcome_table[round[1]] - 1) * 3
    shape_score = outcome_score_arr[outcome_table[round[1]] - 1, shape_table[round[0]] - 1]
    
    print(f'Round {line_counter}: You chose {round[1]}. Shape score is {shape_score}; Outcome_score is {outcome_score}.')
    
    return shape_score, outcome_score

# Read input file and parse based on newlines
with open(INPUT_FILE) as file:
    line_counter = 0
    
    for line in file:
        line_counter += 1
        
        round = line.rstrip().split(' ')
        rounds.append(calc_score(round))
            # except Exception as Ex:
            #     print(f'At line {line_counter} of the input file:')
            #     print(type(Ex))     # the exception instance
            #     print(Ex.args)      # arguments stored in .args]

# # Sum each round's score
total_scores = []
for round in rounds:
    total_scores.append(sum(round))

# # Find the total score over all rounds.
final_total = np.sum(total_scores)

print(f'The total score would be {final_total}.')
print('Program completed.')