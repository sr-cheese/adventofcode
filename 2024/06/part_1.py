###################################################################################### imports

import os
import time
import numpy as np

#################################################################################### functions

def check_next(actual_map, next_pos) :
    if next_pos[0] > 0 and next_pos[0] < len(actual_map) and next_pos[1] > 0 and next_pos[1] < len(actual_map[0]) :
        if actual_map[next_pos[0]][next_pos[1]] == '#' :
            actual_map[next_pos[0]][next_pos[1]] = '>'
            return actual_map

def move_up(actual_map, possition) :
    return 0

def move_right(actual_map, possition) :
    return 0

def move_down(actual_map, possition) :
    return 0

def move_left(actual_map, possition) :
    return 0

def move(actual_map) :
    array_row, array_column = np.where(actual_map == '^')
    row = array_row[0]
    column = array_column[0]

    os.system('cls||clear')
    print(actual_map)
    time.sleep(1)

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
        # return move(new_map)
    return actual_map

######################################################################################## main

with open('example_input', 'r') as file :
    content = file.read()
    lines   = content.strip().split('\n')

move(np.array([ list(line) for line in lines ]))
