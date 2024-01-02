import logging

logger = logging.getLogger() 
logging.debug("This is a debug message.")

# open the txt file
path = 'input_data/day_09_input.txt'
path = 'input_data/practise.txt'
with open(path) as file:
    arr = [line.strip() for line in file.readlines()]

# creating galaxy
galaxy = []
for row in arr:
    galaxy.append([x for x in row])

def find_empty_rows(galaxy):
    '''
    Find empty rows in each galaxy.
    '''
    rows = []
    for idx, row in enumerate(galaxy):
        if all(element == '.' for element in row):
            rows.append(idx)

    return rows

def find_empty_cols(galaxy):
    '''
    Find empty cols in each galaxy.
    '''

    # Get the number of rows and columns
    num_rows = len(galaxy)
    num_cols = len(galaxy[0]) if num_rows > 0 else 0

    # Create a new transposed galaxy
    transposed = [[galaxy[row][col] for row in range(num_rows)] for col in range(num_cols)]

    cols = find_empty_rows(transposed)

    return cols




    cols = []
    
    return cols

def expand_galaxy(galaxy, rows=[], cols=[]):
    pass

def get_coordinates():
    pass

def find_distances():
    pass


print()
