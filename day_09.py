import re
import numpy as np

# open the txt file (practise data)
path = 'input_data/day_09_input.txt'
# path = 'input_data/practise.txt'
with open(path) as file:
    arr = [line.strip() for line in file.readlines()]

def create_rows(input_arr):
    multi_lvl = [input_arr]
    current_arr = input_arr

    while not all(element == 0 for element in current_arr):
        new_lvl = []
        for i in range(len(current_arr))[1:]:
            diff = current_arr[i] - current_arr[i-1]
            new_lvl.append(diff)
        
        multi_lvl.append(new_lvl)
        current_arr = new_lvl

    return multi_lvl

def find_next(final_eles):
    acc = 0
    for ele in final_eles:
        acc += ele
    return acc

def find_previous(first_eles):
    acc = 0
    for ele in first_eles:
        acc = ele - acc
    return acc

# Part 1
total = 0
for sub_arr in arr:
    inp = [int(x) for x in sub_arr.split()]
    row_ends = [x[-1] for x in create_rows(inp)][::-1]
    solution = find_next(row_ends)
    total += solution
print(f'PART 1 SOLUTION = {total}')

# Part 2
total2 = 0
for sub_arr in arr:
    inp = [int(x) for x in sub_arr.split()]
    row_starts = [x[0] for x in create_rows(inp)][::-1]
    solution = find_previous(row_starts)
    total2 += solution
print(f'PART 2 SOLUTION = {total2}')