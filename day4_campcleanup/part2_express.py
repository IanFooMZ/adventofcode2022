import re, numpy
num_ov_pairs = 0
with open('input.txt') as file:
    for line in file:
        res = numpy.array(re.split(',|-', line.rstrip()),dtype='int')
        if set(range(res[0], res[1]+1)).intersection(set(range(res[2], res[3]+1))):
            num_ov_pairs += 1
print(f'There are {num_ov_pairs} pairs where overlap occurs.')