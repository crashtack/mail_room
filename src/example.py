# -*- coding: utf-8 -*-
"""a simplistic command line program, demonstrates isolation of user I/O"""
from random import shuffle
import sys
try:
    input = raw_input
except NameError:
    pass


def user_interaction(menu, error=None):
    if error is not None:
        print("Error: ", error, end="\n\n")
    print(menu)
    print("\t(type 'q' at any time to quit)")
    return input("Enter Your Choice: ")

names = ['bob', 'tom', 'fred', 'sally']

top_menu = """
1. print list
2. add name
"""

print_menu = """
1. print full list
2. print random two names
"""

def validate_integer_in_range(input, range):
    try:
        input = int(input)
    except ValueError:
        return False, "select a choice by number"
    if input not in range:
        return False, "that is not a valid choice, pick again"
    return input, None


def validate_top_menu(input):
    return validate_integer_in_range(input, [1, 2])


def validate_print_menu(input):
    return validate_integer_in_range(input, [1, 2])


def validate_add_menu(input):
    if not isinstance(input, str):
        return False, 'Please input a valid name'
    return input, None


def handle_top_menu(input):
    print("nothing special to do here")
    next_states = {
        1: 'print',
        2: 'add',
    }
    return next_states[input]


def handle_print_menu(input):
    if input == 1:
        print(names)
    elif input == 2:
        random_names = names[:]
        shuffle(random_names)
        print(random_names[:2])
    return 'top'


def handle_add_menu(input):
    global names
    names.append(input)
    return 'top'


STATES = {
    'top': {
        'menu': top_menu,
        'validate': validate_top_menu,
        'handler': handle_top_menu,
    },
    'print': {
        'menu': print_menu,
        'validate': validate_print_menu,
        'handler': handle_print_menu,
    },
    'add': {
        'menu': 'Type a name to add',
        'validate': validate_add_menu,
        'handler': handle_add_menu
    }
}


def get_state(state):
    new_state = STATES[state]
    menu = new_state['menu']
    validator = new_state['validate']
    handler = new_state['handler']
    return menu, validator, handler


if __name__ == '__main__':
    state = 'top'
    error = None
    while True:
        menu, validator, handler = get_state(state)
        user_input = user_interaction(menu, error=error)
        if user_input == 'q':
            sys.exit(0)
        print(user_input)
        user_input, error = validator(user_input)
        if error is not None:
            continue
        state = handler(user_input)
