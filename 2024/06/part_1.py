###################################################################################### imports

import os
import re
import time
import numpy as np

#################################################################################### functions

def move_up(actual_map, possition) :
    if possition[0] - 1 >= 0 :
        if actual_map[possition[0] - 1][possition[1]] == '#' :
            actual_map[possition[0]][possition[1]] = '>'
            return actual_map
        else :
            actual_map[possition[0] - 1][possition[1]] = '^'
            actual_map[possition[0]][possition[1]] = 'X'
            return actual_map
    else :
        actual_map[possition[0]][possition[1]] = 'X'
        return actual_map

def move_right(actual_map, possition) :
    if possition[1] + 1 < len(actual_map[0]) :
        if actual_map[possition[0]][possition[1] + 1] == '#' :
            actual_map[possition[0]][possition[1]] = 'v'
            return actual_map
        else :
            actual_map[possition[0]][possition[1] + 1] = '>'
            actual_map[possition[0]][possition[1]] = 'X'
            return actual_map
    else :
        actual_map[possition[0]][possition[1]] = 'X'
        return actual_map

def move_down(actual_map, possition) :
    if possition[0] + 1 < len(actual_map) :
        if actual_map[possition[0] + 1][possition[1]] == '#' :
            actual_map[possition[0]][possition[1]] = '<'
            return actual_map
        else :
            actual_map[possition[0] + 1][possition[1]] = 'v'
            actual_map[possition[0]][possition[1]] = 'X'
            return actual_map
    else :
        actual_map[possition[0]][possition[1]] = 'X'
        return actual_map

def move_left(actual_map, possition) :
    if possition[1] - 1 >= 0 :
        if actual_map[possition[0]][possition[1] - 1] == '#' :
            actual_map[possition[0]][possition[1]] = '^'
            return actual_map
        else :
            actual_map[possition[0]][possition[1] - 1] = '<'
            actual_map[possition[0]][possition[1]] = 'X'
            return actual_map
    else :
        actual_map[possition[0]][possition[1]] = 'X'
        return actual_map

def move(actual_map) :

    if '^' in actual_map :
        array_row, array_column = np.where(actual_map == '^')
    elif '>' in actual_map :
        array_row, array_column = np.where(actual_map == '>')
    elif 'v' in actual_map :
        array_row, array_column = np.where(actual_map == 'v')
    elif '<' in actual_map :
        array_row, array_column = np.where(actual_map == '<')
    else :
        return actual_map

    row = array_row[0]
    column = array_column[0]

    # os.system('cls||clear')
    # print(actual_map)
    # time.sleep(0.2)

    if row > 0 and row < len(actual_map) and column > 0 and column < len(actual_map[0]) :
        match actual_map[row][column] :
            case '^' :
                new_map = move_up(actual_map, [row, column])
            case '>' :
                new_map = move_right(actual_map, [row, column])
            case 'v' :
                new_map = move_down(actual_map, [row, column])
            case '<' :
                new_map = move_left(actual_map, [row, column])
        
    return new_map

######################################################################################## main

with open('input', 'r') as file :
    content = file.read()
    lines   = content.strip().split('\n')

actual_map = np.array([ list(line) for line in lines ])

while '^' in actual_map or '>' in actual_map or 'v' in actual_map or '<' in actual_map :
    actual_map = move(actual_map)

# os.system('cls||clear')
# print(actual_map)

print(sum([ len(re.findall('X', ''.join(line))) for line in actual_map ]))