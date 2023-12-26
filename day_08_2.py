from math import gcd

path = 'input_data/day_08_input.txt'
# path = 'input_data/practise.txt'
with open(path) as file:
    arr = [line.strip() for line in file.readlines()]

# Creating an array comprised of the directions
path = arr[0]
directions = [1 if x == 'R' else 0 for x in path]

# Turning locations into a key, value pair
locations = arr[2:]
network = {}
for location in locations:
    loc_set = (location[7:10], location[12:15])
    network[location[0:3]] = loc_set


# each of the ghosts has only one possible position that ends with a "Z" on its path.
# need to find where it loops i.e a -> c -> z -> c -> z
def find_z(start, insert_initial=True):
    current_position = start

    # whether or not the start input is put into the returned list
    if insert_initial:
        steps_taken = [current_position]
    else:
         steps_taken = []

    # Looping through the steps to find the path
    while not current_position.endswith('Z'):
        for dir in directions:
            current_position = network[current_position][dir]
            steps_taken.append(current_position)

    return steps_taken

def find_loop(start):
    current_position = start
    steps_taken = []
    current_position = network[current_position][directions[0]]
    steps_taken.append(current_position)

    for dir in directions[1:]:
            current_position = network[current_position][dir]
            steps_taken.append(current_position)
  
    if steps_taken[-1].endswith('Z'):
        return steps_taken
    else:
        return steps_taken + find_z(steps_taken[-1], False)

positions = [key for key in network if key.endswith('A')]
steps = []
loops = []

for start_pos in positions:
    initial_steps = find_z(start_pos)
    steps.append(len(initial_steps) - 1)

    z_step = initial_steps[-1]
    loop_steps = find_loop(z_step)
    loops.append(len(loop_steps))

print(steps)
print(loops)

# found that all loops are equal to the steps so following code is used to find LCM

def find_lcm_of_list(numbers):
    def lcm(x, y):
        return x * y // gcd(x, y)

    if len(numbers) == 0:
        return None

    result_lcm = numbers[0]

    for num in numbers[1:]:
        result_lcm = lcm(result_lcm, num)

    return result_lcm

# Example usage:
numbers_list = loops
result = find_lcm_of_list(numbers_list)

print(f"The LCM of {numbers_list} is: {result}")

print('done')