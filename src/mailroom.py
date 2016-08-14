# -*- coding: utf-8 -*-
"""
    TODO: sort user report before printing
    TODO: create function to create a new user

"""
import os
import sys
from mailroom_functions import (
    initialize_donor_dict,
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
               'Enter Command: ',
               'valid_responses': state_1_valid_responses,
               }
    state_2 = {'state': 2,
               'comment': 'This is the create a thank you letter state.',
               'prompt_message':
               'Options: \n' +
               '\t\t[l or list] Type "l" or list to get a list of current donors\n' +
               '\t\t[name]      Enter a donor name to write a thank you letter\n' +
               '\t\t[0]         Return to Main Menu\n\n' +
               'Enter Command or donor name: ',
               'user_response': '',
               'valid_responses': state_2_valid_responses,
               }
    state_3 = {'state': 3,
               'comment': 'This is Print a Report of donor information.',
               'prompt_message': '',
               'user_response': '',
               'valid_responses': state_3_valid_responses,
               }
    state_4 = {'state': 4,
               'comment': 'Enter New Donation Amount',
               'prompt_message': 'Enter New Donation Amount or' +
               ' 0 to return to previous menu: ',
               'user_response': '',
               'valid_responses': state_4_valid_responses,
               }
    state_5 = {'state': 5,
               'comment': 'Ask to print a Thank You Letter',
               'prompt_message': 'Print a thank you letter? (y or n): ',
               'valid_responses': state_5_valid_responses,
               }
    state_6 = {'state': 6,
               'comment': 'Ask to validate creating a user',
               'prompt_message': ' (y or n): ',
               'valid_responses': state_6_valid_responses,
               'new_donor_name': ''
               }
    state_7 = {'state': 7,
               'comment': 'Ask to validate creating a user',
               'prompt_message': ' (y or n): ',
               'valid_responses': state_6_valid_responses,
               'new_donor_name': ''
               }

    state_dict = {
        'state_0': state_0,
        'state_1': state_1,
        'state_2': state_2,
        'state_3': state_3,
        'state_4': state_4,
        'state_5': state_5,
        'state_6': state_6,
        'state_7': state_7,
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


def state_2_valid_responses(a):
    global CURRENT_STATE
    global CURRENT_DONOR
    if a == 'l' or a == 'list':
        CURRENT_STATE = STATE_DICT['state_2']
        list_of_donors(DONORS)
    elif a == '0':
        CURRENT_STATE = STATE_DICT['state_1']
        os.system('clear')
    else:
        try:
            CURRENT_DONOR = DONORS[a]
            user_report()
            CURRENT_STATE = STATE_DICT['state_4']
        except KeyError:
            print('{} is not a current donor.'.format(a))
            print('Create a new donor {}'.format(a), end='')
            STATE_DICT['state_6']['new_donor_name'] = a
            CURRENT_STATE = STATE_DICT['state_6']
            return


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


def state_4_valid_responses(a):
    ''' need to test for properly formated $ amout iiiiii.ii '''
    global CURRENT_STATE
    global CURRENT_DONOR
    if a == '0':
        CURRENT_STATE = STATE_DICT['state_2']
        os.system('clear')
        return
    try:
        amount = float(a)
        update_donor(amount)
        user_report()
        CURRENT_STATE = STATE_DICT['state_5']
        # print('amount = {:.2f}'.format(amount))
        return amount
    except ValueError:
        print('{} is not a valid amount'.format(a))
        return False


def state_5_valid_responses(a):
    global CURRENT_STATE
    if a == 'y':
        print_letter()
        CURRENT_STATE = STATE_DICT['state_2']
    elif a == 'n':
        os.system('clear')
        CURRENT_STATE = STATE_DICT['state_2']
    else:
            print('That was not a valid input')
            return False
    return


def state_6_valid_responses(a):
    global CURRENT_STATE
    if a == 'y':
        create_donor()
        # update_donor()
        CURRENT_STATE = STATE_DICT['state_4']
    elif a == 'n':
        os.system('clear')
        CURRENT_STATE = STATE_DICT['state_2']
    else:
        print('That was not a valid input')
        CURRENT_STATE = STATE_DICT['state_6']
        return False
    return


# def state_2_action():
#     pass


def create_report():
    global DONORS
    os.system('clear')
    print('{:<20}  {:<20}  {:<20}  {:<20}  {:<20}\n'
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


def user_report():
    donor = CURRENT_DONOR
    os.system('clear')
    print('Donor info:')
    print('{:>25}{}'.format('Name:  ', donor['name']))
    print('{:>25}${:,.2f}'.format('Total Donation:  ', donor['total_donation']))
    print('{:>25}{}'.format('Number of Donations:  ', donor['num_donations']))
    print('{:>25}${:,.2f}'.format('Average Donation:  ', donor['avg_donation']))
    print('{:>25}${:,.2f}'.format('Last Donation:  ', donor['last_donation']))
    print()


def list_of_donors(donor_dict):
        ''' print the list of donor names '''
        os.system('clear')
        print('\nCurrent Donors:')
        for donor in donor_dict.values():
            # print(donor)
            print('\t\t{}'.format(donor['name']))
        print()


def create_donor():
    global DONORS
    global CURRENT_DONOR
    new_donor = {'name': CURRENT_STATE['new_donor_name'],
                 'total_donation': 0,
                 'num_donations': 0,
                 'avg_donation': 0,
                 'last_donation': 0}
    DONORS[CURRENT_STATE['new_donor_name']] = new_donor
    CURRENT_DONOR = DONORS[CURRENT_STATE['new_donor_name']]
    print('Created New Donor:')
    user_report()


def update_donor(amount):
    # os.systme('clear')
    global CURRENT_DONOR
    print('updating: {}'.format(CURRENT_DONOR))
    CURRENT_DONOR['last_donation'] = amount
    CURRENT_DONOR['total_donation'] += amount
    CURRENT_DONOR['num_donations'] += 1
    CURRENT_DONOR['avg_donation'] = CURRENT_DONOR['total_donation']\
        / CURRENT_DONOR['num_donations']


def print_letter():
    os.system('clear')
    print("""
    ----------------------------------------------------------------------------

    Dear {},
    Thank you for your recent donation of ${:,.2f}. Without donors like you
    the Save the Womp Rats Foundation would not exist.

    Sincerly Yours,
    Jane Doe
    Save the Womp Rats Foundation

    ----------------------------------------------------------------------------
    """
          .format(CURRENT_DONOR['name'],
                  CURRENT_DONOR['last_donation']))


DONORS = initialize_donor_dict()
CURRENT_DONOR = {}
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
