###################################################################################### imports

import re
import numpy as np

#################################################################################### functions

def get_next_free_space(line) :
    return np.where(line == '.')[0][0]

def check_is_ordered(line, first_empty) :
    for index in range(len(line[first_empty:])) :
        if line[first_empty + index] != '.' and index != 0 :
            return False
    return True

def get_last_non_empty_value(line) :
    last_value = re.findall(r'[0-9]', ''.join(line))[-1]
    return np.where(line == last_value)[0][-1]

######################################################################################## main

lines = open('input').read().strip().split('\n')
# lines = open('example_input').read().strip().split('\n')
list_line = list(map(int, lines[0]))

new_line = []
aux = 0
for index in range(len(list_line)) :
    if not index % 2 :
        for rep in range(list_line[index]) :
            new_line.append(str(aux))
        aux += 1
    else :
        for rep in range(list_line[index]) :
            new_line.append('.')

np_new_line = np.array(new_line)
next_empty_poss = get_next_free_space(np_new_line)
while not check_is_ordered(np_new_line, next_empty_poss) :
    np_new_line[next_empty_poss] = np_new_line[get_last_non_empty_value(np_new_line)]
    np_new_line[get_last_non_empty_value(np_new_line)] = '.'
    next_empty_poss = get_next_free_space(np_new_line)
    # print(''.join(np_new_line))

checksum = 0
for id in range(len(np_new_line)) :
    if np_new_line[id] == '.' :
        break
    mul = id * int(np_new_line[id])
    checksum += mul
print(checksum)