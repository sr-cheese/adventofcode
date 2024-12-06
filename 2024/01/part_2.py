# the lists are not sorted
# each id in the list on the left must be multiplied by the number of times it is repeated in the list on the right
# the sum of these values is the similarity score of the lists

import re

# read input file
inputs = open('input', 'r')
lines  = inputs.readlines()
inputs.close()

# define result var
result = 0

# define aux vars
similarity_results = []

# define map methos (i'm sure it can be optimized)
def get_left_ids(line) :
    splited_line = re.split(r'   ', line)
    return int(splited_line[0])

def get_right_ids(line) :
    splited_line = re.split(r'   ', line)
    return int(splited_line[1])

# get left and right id lists
left_ids  = list(map(get_left_ids, lines))
right_ids = list(map(get_right_ids, lines))

# get partial similarity
for id in left_ids :
    partial_result = id * right_ids.count(id)
    similarity_results.append(partial_result)

# get result
for partial_result in similarity_results :
    result = result + partial_result

print(result)