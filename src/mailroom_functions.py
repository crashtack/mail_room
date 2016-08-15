# -*- coding: utf-8 -*-
''' main mailroom script file '''


# def initialize_state_dict():
#     state_0 = {}   # this is the quit state
#
#     state_1 = {'state': 1,
#                'comment': 'This is the initial entry state.',
#                'prompt_message':
#                'Welcome the the Donor Message Creation Center\n' +
#                'Options: \n'
#                '\t\t[1] Print a Report of donors and donation history\n' +
#                '\t\t[2] Send a Thank You email for a new donation\n' +
#                '\t\t[0] Quit the Program\n\n',
#                'user_response': '',
#                'valid_responses': state_1_valid_responses,
#                'action': state_1_action,
#                'next_state': 2
#                }
#     state_2 = {'state': 2,
#                'comment': 'This is the create a thank you letter state.',
#                'prompt_message':
#                '\t\t[l or list] Type "l" or list to get a list of current donors\n' +
#                '\t\t[name]      Enter a donor name to write a thank you letter\n' +
#                '\t\t[0]         Quit the Program\n\n',
#                'user_response': '',
#                'valid_responses': state_2_valid_responses,
#                'action': state_2_action,
#                'next_state': 2
#                }
#
#     state_dict = {
#         'state_0': state_0,
#         'state_1': state_1,
#         'state_2': state_2,
#     }
#
#     return state_dict

# John_Doe = {'name': 'John Doe','total_donation': 0,'num_donations': 0,'avg_donation': 0,'last_donation': 0}
# print(John_Doe)
# print(John_Doe['name'])
# print(initialize_state_dict()['state_1'])
# print(list_of_donors(initialize_donor_dict()))


# def state_1_valid_responses(a):
#
#     if a == '0':
#         current_state = state_dict['state_0']
#         print('you entered 0')
#         return True
#     elif a == '1':
#         current_state = state_dict['state_3']
#         return True
#     elif a == '2':
#         current_state = state_dict['state_2']
#         return True
#     else:
#         print('That was not a valid input')
#         return False


def state_1_action():
    pass


def state_2_valid_responses(a):
    if a == 'l' or a == 'list':
        current_state = state_dict['state_4']
    if a in donor_dict.values():
        pass


def state_2_action():
    pass


def initialize_donor_dict():
    '''function to create the dictionary of dictionary to
       hold donor information
    '''
    John_Doe = {'name': 'John Doe',
                'total_donation': 0,
                'num_donations': 0,
                'avg_donation': 0,
                'last_donation': 0}

    Neil_Armstrong = {'name': 'Neil Armstrong',
                      'total_donation': 23000000,
                      'num_donations': 4,
                      'avg_donation': 5750000,
                      'last_donation': 10000000}

    Sara_Smith = {'name': 'Sara Smith',
                  'total_donation': 100,
                  'num_donations': 2,
                  'avg_donation': 50,
                  'last_donation': 35}
                  
    Ralf_the_Dog = {'name': 'Ralf the Dog',
                    'total_donation': 1000,
                    'num_donations': 1,
                    'avg_donation': 1000,
                    'last_donation': 1000}

    donor_dict = {'John Doe': John_Doe,
                  'Neil Armstrong': Neil_Armstrong,
                  'Sara Smith': Sara_Smith,
                  'Ralf the Dog': Ralf_the_Dog,
                  }

    return donor_dict


def prompt_for_input(message):
    '''"Request user input based on current runmode'''
    return input(message)


# def list_of_donors(donor_dict):
#         ''' print the list of donor names '''
#         for donor in donor_dict.values():
#             # print(donor)
#             print(donor['name'])

# print(list_of_donors(initialize_donor_dict()))


def create_new_donor():
    # TODO: refactor to pull out prompt_for_input() call
    new_donor = {}
    message = ''
    prompt = 'Enter Name of New Donor: '
    name = prompt_for_input(message, prompt)
    if type(name) == str and len(name) < 100:
        new_donor['name'] = name
    else:
        print("That doesn't apear to be a valid name")
        create_new_donor()

    message = ''
    prompt = 'Enter donation amount for {0}: '.format(name)
    name = prompt_for_input(message, prompt)


# print(initialize_state_dict()['state_1']['prompt_message'])
