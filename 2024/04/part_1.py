# find one word: XMAS
# This word search allows words to be:
#   - horizontal
#   - vertical
#   - diagonal
#   - written backwards
#   - overlapping other words.
#
# For example:
#   MMMSXXMASM
#   MSAMXMSMSA
#   AMXSXMAAMM
#   MSAMASMSMX
#   XMASAMXAMM
#   XXAMMXXAMA
#   SMSMSASXSS
#   SAXAMASAAA
#   MAMMMXMMMM
#   MXMXAXMASX
#
# In this word search, XMAS occurs a total of 18 times

import re
import numpy as np

t_matrix = []

XMAS_COUNT  = 0

with open('example_input_2', 'r') as file :
    content = file.read()
    lines   = content.strip().split('\n')

word_matrix = np.array([list(line) for line in lines])
t_matrix = word_matrix.transpose()

# Horizontal XMAS
for line in lines :
    XMAS_COUNT += len(re.findall(r'XMAS', line))
    XMAS_COUNT += len(re.findall(r'SAMX', line))

# Vertical XMAS
for t_line in t_matrix :
    t_str = ''.join(t_line)
    XMAS_COUNT += len(re.findall(r'XMAS', t_str))
    XMAS_COUNT += len(re.findall(r'SAMX', t_str))

# Diagonal top_left to botom_right
print(word_matrix)
print('')
for y in range(len(word_matrix)) :
    d1_line = []
    d2_line = []
    for x in range(len(word_matrix[y])) :
        if x+y < len(word_matrix) :
            d1_line.append(word_matrix[x][x+y])
            d2_line.append(word_matrix[x+y][x])

    XMAS_COUNT += len(re.findall(r'XMAS', ''.join(d1_line)))
    XMAS_COUNT += len(re.findall(r'SAMX', ''.join(d1_line)))
    print(d1_line)
    if y > 0 :
        XMAS_COUNT += len(re.findall(r'XMAS', ''.join(d2_line)))
        XMAS_COUNT += len(re.findall(r'SAMX', ''.join(d2_line)))
        print(d2_line)

# Diagonal botom_left to top_right
print('')
print(word_matrix)
print('')
for y in range(len(word_matrix)) :
    d1_line = []
    d2_line = []
    for x in range(len(word_matrix[y])) :
        if y-x > -1 :
            d1_line.append(word_matrix[y-x][x])
            d2_line.append(word_matrix[y][y-x])

    XMAS_COUNT += len(re.findall(r'XMAS', ''.join(d1_line)))
    XMAS_COUNT += len(re.findall(r'SAMX', ''.join(d1_line)))
    print(d1_line)
    if y+x > len(word_matrix[0]) :
        XMAS_COUNT += len(re.findall(r'XMAS', ''.join(d2_line)))
        XMAS_COUNT += len(re.findall(r'SAMX', ''.join(d2_line)))
        print(d2_line)

# print(word_matrix)
# print('')
# print(t_matrix)
print(XMAS_COUNT)