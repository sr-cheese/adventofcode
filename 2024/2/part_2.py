# example_imput:
#   7 6 4 2 1
#   1 2 7 8 9
#   9 7 6 2 1
#   1 3 2 4 5
#   8 6 4 4 1
#   1 3 6 7 9

# Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
# More of the above example's reports are now safe:
#   7 6 4 2 1: Safe without removing any level.
#   1 2 7 8 9: Unsafe regardless of which level is removed.
#   9 7 6 2 1: Unsafe regardless of which level is removed.
#   1 3 2 4 5: Safe by removing the second level, 3.
#   8 6 4 4 1: Safe by removing the third level, 4.
#   1 3 6 7 9: Safe without removing any level.

import copy

# read input file
with open('input', 'r') as file :
    content = file.read()
    lines   = content.strip().split('\n')
    result  = [ list( map( int, line.split() ) ) for line in lines ]

safe_reports = 0

def is_safe(actual_status, last_status, actual_level, last_level) :
    if actual_status == 0 :
        return False
    if actual_status < 0 and last_status > 0 :
        return False
    if actual_status > 0 and last_status < 0 :
        return False
    if abs(actual_level - last_level) > 3 :
        return False
    return True

def check_line(line, removed_level) :
    count         = 1
    last_status   = 0
    last_level    = line[0]
    actual_status = last_level - line[1]

    while count < len(line) :
        last_level    = line[count - 1]
        actual_level  = line[count]
        last_status   = actual_status
        actual_status = last_level - actual_level

        if not(is_safe(actual_status, last_status, actual_level, last_level)) :
            if removed_level == 0 :
                dampener_line = copy.deepcopy(line)
                dampener_line.pop(count)
                return check_line(dampener_line, 1)
            else :
                break
        count += 1

    if count == len(line) :
        return 1
    print(f'linea {line} invalida')
    return 0

for line in result :
    safe_reports += check_line(line, 0)

print(safe_reports)