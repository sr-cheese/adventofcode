#############
# IMPORTS   #
#############

import re
import math

#############
# FUNCTIONS #
#############

def clean_orders(order) :
    if len(order) > 0 :
        return order.split('|')
    
def clean_updates(update) :
    if len(update) > 0 :
        return update.split(',')
    
def get_rules(page, orders) :
    return [ order for order in orders if str(page) in order ]

def check_rules(this_page, other_page, pages, rules) :
    index_diff = pages.index(str(other_page)) - pages.index(str(this_page))
    return [ rule.index(str(this_page)) == 0 and index_diff > 0 for rule in rules if str(this_page) in rule and str(other_page) in rule ][0]

def array_search(search_list, orders) :
    rules = get_rules(search_list[0], orders) 

    if len(search_list) == 1 :
        return True

    check_results = [ check_rules(search_list[0], other_page, search_list, rules) for other_page in search_list[1:] ]

    if False in check_results :
        return False

    return array_search(search_list[1:], orders)
    
#############
# EXECUTION #
#############

with open('example_input', 'r') as file :
    content = file.read()
    lines   = content.strip().split('\n')

raw_orders  = list(map( lambda line: ''.join(re.findall(r'\d*\|\d*', line)), lines ))
raw_updates = list(map( lambda line: ''.join(re.findall(r'\d*,\d*', line)), lines ))

orders = [ order for order in list(map(clean_orders, raw_orders)) if order is not None ]
updates = [ update for update in list(map(clean_updates, raw_updates)) if update is not None ]

incorrectly_ordered = [ update for update in updates if not array_search(update, orders) ]

# Falta reordenar las incorrectas
print(incorrectly_ordered)