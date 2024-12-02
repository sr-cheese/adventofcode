# example_imput:
#   7 6 4 2 1
#   1 2 7 8 9
#   9 7 6 2 1
#   1 3 2 4 5
#   8 6 4 4 1
#   1 3 6 7 9

# a report only counts as safe if both of the following are true:
#   - The levels are either all increasing or all decreasing.
#   - Any two adjacent levels differ by at least one and at most three.
# In the example above, the reports can be found safe or unsafe by checking those rules:
#     7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
#     1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
#     9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
#     1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
#     8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
#     1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

import re

# read input file
inputs = open('input', 'r')
lines  = inputs.readlines()
inputs.close()

safe_reports = 0

for line in lines :
    list_line = re.split(r' ', line)
    numeric_line = list(map(int, list_line))

    count = 1
    last_status = 0
    last_value = numeric_line[0]
    actual_status = last_value - numeric_line[1]

    while count < len(numeric_line) :
        last_value = numeric_line[count - 1]
        actual_value = numeric_line[count]
        last_status = actual_status
        actual_status = last_value - actual_value

        if actual_status == 0 :
            break

        if actual_status < 0 and last_status > 0 :
            break

        if actual_status > 0 and last_status < 0 :
            break

        if abs(actual_value - last_value) > 3 :
            break

        count += 1

    if count == len(numeric_line) :
        safe_reports += 1

print(safe_reports)