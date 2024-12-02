# the lists are not sorted
# the lists must be compared once they have been sorted 1 by 1
# the sum of the absolute value of the previous comparisons is the objective result

import re

# read input file
inputs = open('input', 'r')
lines  = inputs.readlines()
inputs.close()

# define result var
result = 0

# define map methos (i'm sure it can be optimized)
def get_left_ids(line) :
    splited_line      = re.split(r'   ', line)
    return int(splited_line[0])

def get_right_ids(line) :
    splited_line      = re.split(r'   ', line)
    return int(splited_line[1])

# get left and right id lists
left_ids  = map(get_left_ids, lines)
right_ids = map(get_right_ids, lines)

# sort left and right id lists
sorted_left_ids  = sorted(left_ids)
sorted_right_ids = sorted(right_ids)

# get distances between ids
compared_ids = map(lambda x, y: abs(x - y), sorted_left_ids, sorted_right_ids)

# get result
for id in compared_ids :
    result = result + id

print(result)