import re
import numpy as np

# open the txt file (practise data)
# path = 'input_data/day_08_input.txt'
path = 'input_data/practise.txt'
with open(path) as file:
    arr = [line.strip() for line in file.readlines()]

# Creating an array comprised of the directions
path = arr[0]
directions = [1 if x == 'R' else 0 for x in path]

# Turning locations into a key, value pair
locations = arr[2:]
locus = {}
for location in locations:
    loc_set = (location[7:10], location[12:15])
    locus[location[0:3]] = loc_set


# Looping through the directions array to get to 'ZZZ'
current_position = 'AAA'
steps = 0

while current_position != 'ZZZ':
    for dir in directions:
        current_position = locus[current_position][dir]
        steps += 1

print('--------------PART 1--------------')
print(f'steps taken = {steps}')
print(f'destination = {current_position}')

