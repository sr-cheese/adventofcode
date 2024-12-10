###################################################################################### imports

import os
import re
import time
import numpy as np

#################################################################################### functions

def find_nodes_types(map_row) :
    res = []
    numbers = re.findall(r'[0-9]', map_row)
    chars = re.findall(r'[a-z]|[A-Z]', map_row)

    for number in numbers :
        res.append(number)    
        
    for char in chars :
        res.append(char) 

    return res

def marc_antinode(nodes_map, first_node, second_node, distance, antinodes_map) :
    first_antinode_position = [ first_node[0] + distance[0], first_node[1] + distance[1] ]
    second_antinode_position = [ second_node[0] - distance[0], second_node[1] - distance[1] ]

    if first_antinode_position[0] >= 0 and first_antinode_position[0] < len(nodes_map) :
        if first_antinode_position[1] >= 0 and first_antinode_position[1] < len(nodes_map[0]) :
            if antinodes_map[first_antinode_position[0]][first_antinode_position[1]] == '.' :
                antinodes_map[first_antinode_position[0]][first_antinode_position[1]] = '#'

    if second_antinode_position[0] >= 0 and second_antinode_position[0] < len(nodes_map) :
        if second_antinode_position[1] >= 0 and second_antinode_position[1] < len(nodes_map[0]) :
            if antinodes_map[second_antinode_position[0]][second_antinode_position[1]] == '.':
                antinodes_map[second_antinode_position[0]][second_antinode_position[1]] = '#'

    # os.system('cls||clear')
    # print(f'Comparing {first_node} with {second_node}')
    # print(antinodes)
    # print(nodes_map)
    # time.sleep(1)

    return antinodes_map

def nodes_vector(nodes_map, first_node, second_node, antinodes_map) :
    return marc_antinode(nodes_map, first_node, second_node, [ first_node[0] - second_node[0], first_node[1] - second_node[1] ], antinodes_map )

def compare_possitions(nodes_map, possitions, antinodes_map) :
    first = possitions[0]
    if len(possitions) > 1 :
        for index in range(len(possitions[1:])) :
            antinodes_map = nodes_vector(nodes_map, first, possitions[index + 1], antinodes_map)
        return compare_possitions(nodes_map, possitions[1:], antinodes_map)
    return antinodes_map

def get_nodes_position(rows, columns) :
    possitions = []
    for index in range(len(rows)) :
        possitions.append([ rows[index], columns[index]])
    return possitions

######################################################################################## main

lines = open('input', 'r').read().split('\n')
nodes_map = np.array([ list(line) for line in lines ])

different_nodes = []

raw_nodes = list(map( find_nodes_types, lines ))
nodes = []
antinodes = 0

antinodes_map_raw = []
for line in lines :
    new_line = []
    for point in line :
        new_line.append('.')
    antinodes_map_raw.append(new_line)
antinodes_map = np.array(antinodes_map_raw)

for node_line in raw_nodes :
    for node in node_line :
        if node not in nodes :
            nodes.append(node)

for node in nodes :
    rows, columns = np.where(nodes_map == node)
    possitions = get_nodes_position(rows, columns)
    antinodes_map = compare_possitions(nodes_map, possitions, antinodes_map)

print(nodes)
# print(antinodes) # 266 -> muy alta
# print(sum([ len(re.findall(r'#', ''.join(antinodes))) for antinodes in nodes_map ])) # 250 -> muy baja   
print(sum([ len(re.findall(r'#', ''.join(antinodes))) for antinodes in antinodes_map ]))

for line in nodes_map :
    print(''.join(line))