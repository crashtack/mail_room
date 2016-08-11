# -*- coding: utf-8 -*-

from mailroom_functions import initialize_donor_dict, \
    initialize_state_dict, list_of_donors, prompt_for_input

initialize_donor_dict()
initialize_state_dict()

current_state = state_1

while True:
    response = prompt_for_input(current_state['prompt_message'])
    current_state['valid_responses'](response)
    pass
