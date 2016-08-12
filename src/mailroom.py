# -*- coding: utf-8 -*-
import os
from mailroom_functions import initialize_donor_dict, \
    initialize_state_dict, list_of_donors, prompt_for_input


donar_dict = initialize_donor_dict()
state_dict = initialize_state_dict()

current_state = state_dict['state_1']

if __name__ == '__main__':
    while True:
        os.system('clear')
        response = prompt_for_input(current_state['prompt_message'])

        print('response: {}\n'.format(response))
        if current_state['valid_responses'](response):
            current_state['action']()
