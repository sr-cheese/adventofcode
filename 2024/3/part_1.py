# For example, consider the following section of corrupted memory:
#   xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

# Only the four highlighted sections are real mul instructions. 
# Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5)

import re

mul_list = []
result   = 0

with open('input', 'r') as file :
    content = file.read()
    lines   = content.strip().split('\n')

for line in lines :
    for mul_element in re.findall(r"mul\(\d*,\d*\)", line) :
        mul_list.append(mul_element)

numbers = list(map( lambda mul : re.findall(r"\d+", mul), mul_list ))

for mul in numbers :
    product = int(mul[0]) * int(mul[1])
    result += product

print(result)