# -*- coding: utf-8 -*-
import os
import sys
from mailroom_functions import (
    initialize_donor_dict,
    # list_of_donors,
    prompt_for_input,
)


def initialize_state_dict():
    state_0 = {'state': 0,
               'comment': 'this is the quite state.',
               'prompt_message':
               'Good By\n',
               'user_response': '',
               'valid_responses': state_0_valid_responses,
               'action': state_0_action,
               'next_state': 0
               }   # this is the quit state

    state_1 = {'state': 1,
               'comment': 'This is the initial entry state.',
               'prompt_message':
               'Welcome the the Donor Message Creation Center\n\n' +
               'Options:' +
               '\t[1] Print a Report of donors and donation history\n' +
               '\t\t[2] Send a Thank You email for a new donation\n' +
               '\t\t[0] Quit the Program\n\n' +
               'Ender Command: ',
               'user_response': '',
               'valid_responses': state_1_valid_responses,
               'action': state_1_action,
               'next_state': 0
               }
    state_2 = {'state': 2,
               'comment': 'This is the create a thank you letter state.',
               'prompt_message':
               'Options: \n' +
               '\t\t[l or list] Type "l" or list to get a list of current donors\n' +
               '\t\t[name]      Enter a donor name to write a thank you letter\n' +
               '\t\t[0]         Quit the Program\n\n' +
               'Ender Command: ',
               'user_response': '',
               'valid_responses': state_2_valid_responses,
               'action': state_2_action,
               'next_state': 0
               }
    state_3 = {'state': 3,
               'comment': 'This is Print a Report of donor information.',
               'prompt_message': '',
            #    '\nOptions: \n' +
            #    '\t\t[1] Return to main menu\n' +
            #    '\t\t[0] Quit the Program\n\n',
               'user_response': '',
               'valid_responses': state_3_valid_responses,
               'action': state_2_action,
               'next_state': 4
               }
    state_4 = {'state': 4,
               'comment': 'This is Print a Report of donor information.',
               'prompt_message': '',
            #    '\nOptions: \n' +
            #    '\t\t[1] Return to main menu\n' +
            #    '\t\t[0] Quit the Program\n\n',
               'user_response': '',
               'valid_responses': state_3_valid_responses,
               'action': state_2_action,
               }

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


def state_1_valid_responses(a):
    global CURRENT_STATE
    global STATE_DICT
    if a == '0':
        os.system('clear')
        print('Good By')
        sys.exit()
    elif a == '1':
        create_report()
        CURRENT_STATE = STATE_DICT['state_3']
        return True
    elif a == '2':
        CURRENT_STATE = STATE_DICT['state_2']
        os.system('clear')
        # print('you entered 2, next state should be 2')
        return True
    else:
        print('That was not a valid input')
        return False


def state_1_action():
    pass


def state_2_valid_responses(a):
    global CURRENT_STATE
    global DONORS
    if a == 'l' or a == 'list':
        CURRENT_STATE = STATE_DICT['state_2']
        list_of_donors(DONORS)
    elif DONORS[a]:
        update_donor(a)
        print('We Found A Donor that matches your inpput')
        CURRENT_STATE = STATE_DICT['state_4']
        os.system('clear')
    elif a == '0':
        # CURRENT_STATE = STATE_DICT['state_0']
        os.system('clear')
        print('Good By')
        # print('current state: {}'.format(CURRENT_STATE['state']))
        sys.exit()
    else:
            print('That was not a valid input')
            return False


def state_3_valid_responses(a):
    global CURRENT_STATE
    if a == '1':
        CURRENT_STATE = STATE_DICT['state_1']
        os.system('clear')
    elif a == '0':
        os.system('clear')
        print('Good By')
        sys.exit()
    else:
            print('That was not a valid input')
            return False


def state_2_action():
    pass

    # state_dict = {
    #     'state_0': state_0,
    #     'state_1': state_1,
    #     'state_2': state_2,
    #     }


def create_report():
    global DONORS
    os.system('clear')
    print('{:<20}  {:<20}  {:<20}  {:<20}  {:<20}'
          .format('Name', 'Total Donation', '# of Donations',
                  'Average Donation', 'Last Donation'))
    for donor in DONORS.values():
        # print(donor)
        print('{:<20}  {:<20}  {:<20}  {:<20}  {:<20}'
              .format(donor['name'], donor['total_donation'],
                      donor['num_donations'], donor['avg_donation'],
                      donor['last_donation']))

    print('\nOptions: \n\t\t[1] Return to main menu\n' +
          '\t\t[0] Quit the Program\n\n')


def list_of_donors(donor_dict):
        ''' print the list of donor names '''
        os.system('clear')
        print('\nCurrent Donors:')
        for donor in donor_dict.values():
            # print(donor)
            print('\t{}'.format(donor['name']))
        print()


def update_donor(name):
    global DONORS
    name_ = name.replace(' ', '_')
    print(name_)
    # for donor['name'][name] in DONORS;
    #     print(DONORS.)
    # DONORS[name]


DONORS = initialize_donor_dict()
STATE_DICT = initialize_state_dict()
CURRENT_STATE = STATE_DICT['state_1']

if __name__ == '__main__':
    os.system('clear')

    while True:
        # os.system('clear')
        # print(CURRENT_STATE)
        # print('current state: {}'.format(CURRENT_STATE['state']))
        response = prompt_for_input(CURRENT_STATE['prompt_message'])

        # print('response: {}\n'.format(response))
        CURRENT_STATE['valid_responses'](response)
        # current_state['action']()
