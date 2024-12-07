###################################################################################### imports

import itertools

#################################################################################### functions

def binary_operators(num_operators) :
    return list(itertools.product([0, 1], repeat=num_operators))

def check_operations(line) :
    test_value = int(line.split(':')[0])
    numbers = list(map( int, line.split(':')[1].strip().split(' ') ))
    operations = binary_operators(len(numbers) - 1)
    operations_results = []

    for operation in operations :
        test_result = 0
        for index in range(len(numbers)) :
            if index == 0 :
                test_result = numbers[index]
            else :
                if operation[index - 1] == 0 :
                    test_result += numbers[index]
                else :
                    test_result *= numbers[index]  

        operations_results.append(test_value == test_result)

    return [ test_value, operations_results ]

######################################################################################## main

with open('example_input', 'r') as file :
    content = file.read()
    lines   = content.strip().split('\n')

print( sum( [ line[0] for line in list(map( check_operations, lines )) if True in line[1] ] ) )
