# -*- coding: utf-8 -*-
import os
import sys
from mailroom_functions import (
    initialize_donor_dict,
    # initialize_state_dict,
    list_of_donors,
    prompt_for_input
)


def initialize_state_dict():
    state_0 = {'state': 0,
               'comment': 'this is the quite state.',
               'prompt_message':
               'Good By\n',
               'user_response': '',
               'valid_responses': state_0_valid_responses,
               'action': state_0_action,
               'next_state': 2
               }   # this is the quit state

    state_1 = {'state': 1,
               'comment': 'This is the initial entry state.',
               'prompt_message':
               'Welcome the the Donor Message Creation Center\n' +
               'Options: \n'
               '\t\t[1] Print a Report of donors and donation history\n' +
               '\t\t[2] Send a Thank You email for a new donation\n' +
               '\t\t[0] Quit the Program\n\n',
               'user_response': '',
               'valid_responses': state_1_valid_responses,
               'action': state_1_action,
               'next_state': 2
               }
    state_2 = {'state': 2,
               'comment': 'This is the create a thank you letter state.',
               'prompt_message':
               '\t\t[l or list] Type "l" or list to get a list of current donors\n' +
               '\t\t[name]      Enter a donor name to write a thank you letter\n' +
               '\t\t[0]         Quit the Program\n\n',
               'user_response': '',
               'valid_responses': state_2_valid_responses,
               'action': state_2_action,
               'next_state': 2
               }
    state_3 = {}

    state_dict = {
        'state_0': state_0,
        'state_1': state_1,
        'state_2': state_2,
        'state_3': state_3,
    }

    return state_dict


def state_0_valid_responses():
    pass


def state_0_action():
    pass


def state_1_valid_responses(a, state_dict):

    if a == '0':
        CURRENT_STATE = STATE_DICT['state_0']
        print('you entered 0')
        sys.exit()
        return True
    elif a == '1':
        CURRENT_STATE = STATE_DICT['state_3']
        return True
    elif a == '2':
        CURRENT_STATE = STATE_DICT['state_2']
        return True
    else:
        print('That was not a valid input')
        return False


def state_1_action():
    pass


def state_2_valid_responses(a):
    if a == 'l' or a == 'list':
        CURRENT_STATE = STATE_DICT['state_4']
    if a in DONORS.values():
        pass


def state_2_action():
    pass


DONORS = initialize_donor_dict()
STATE_DICT = initialize_state_dict()
CURRENT_STATE = STATE_DICT['state_1']

if __name__ == '__main__':
    while True:
        # os.system('clear')
        print('current state: {}'.format(CURRENT_STATE['state']))
        response = prompt_for_input(CURRENT_STATE['prompt_message'])

        print('response: {}\n'.format(response))
        CURRENT_STATE['valid_responses'](response, STATE_DICT)
        # current_state['action']()
