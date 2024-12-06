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

# read input file
with open('example_input', 'r') as file :
    content = file.read()
    lines   = content.strip().split('\n')
    result  = [ list( map( int, line.split() ) ) for line in lines ]

safe_reports      = 0

for line in result :
    count         = 1
    last_status   = 0
    last_level    = line[0]
    actual_status = last_level - line[1]

    while count < len(line) :
        last_level    = line[count - 1]
        actual_level  = line[count]
        last_status   = actual_status
        actual_status = last_level - actual_level

        if actual_status == 0 :
            break

        if actual_status < 0 and last_status > 0 :
            break

        if actual_status > 0 and last_status < 0 :
            break

        if abs(actual_level - last_level) > 3 :
            break

        count += 1

    if count == len(line) :
        safe_reports += 1

print(safe_reports)