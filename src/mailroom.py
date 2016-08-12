# -*- coding: utf-8 -*-
import os
from mailroom_functions import initialize_donor_dict, \
    initialize_state_dict, list_of_donors, prompt_for_input


donar_dict = initialize_donor_dict()
state_dict = initialize_state_dict()

current_state = state_dict['state_1']

while True:
    response = prompt_for_input(current_state['prompt_message'])
    os.system('clear')
    print('response: {}\n'.format(response))
    # current_state['valid_responses'](response)
    pass
