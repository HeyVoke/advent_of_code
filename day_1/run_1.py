import re

# open the txt file

file = open('day_1/day_1_input.txt') 
arr = file.readlines()
file.close()

codes = []
# first digit and last digit

for str in arr:
    match = re.findall(r'\d', str)
    num = int(match[0] + match[-1])
    codes.append(num)

print(sum(codes))