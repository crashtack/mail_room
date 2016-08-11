""" this file is pseudocode for the Mail Room Madness projet """

""" Create our dictionary of donars """
#  Donor Name, total donated, number of donations and average donation amount
donars = ()


def prompt_for_input(runmode):
    '''request user input based on current runmode'''
    if runmode == 1:
        print('Selections:')
        print('\t[1] Create Report')
        print('\t[2] Write Thank You Letter')
        print('\t[3] Quit')
        reply = input('Enter selection: ')
        if reply == 1:
            return 'create report'
        elif reply == 2:
            return 'thank you'
        elif reply == 3:
            return 'quit'
        else:
            prompt_for_input(runmode)

    if runmode == 2:
        prompt for different input

    if runmode == 3:
        prompt for different input

    if runmode == 4:
        prompt for differetn input


def create_new_donar(name, amount):
    ''' create a new donar based on input '''
    donars[name] = amount


def add_amount_to_donar(name, amount):
    ''' you guessed it, increase the total donation amount of a donar '''
    donars[name] += amount


def list_donars():
    ''' print the list of donars '''
    print the entire donar list
    for donar in donars:
        print(donar(keyname))


def cleanup():
    ''' do whatever needs to be done for cleanup '''
    save the donar dict to disk
    print some stats
    print some good by message



runmode = 1
while runmode:

    # This is the starting mode
    if runmode == 1:
        # prompt user to create a thank you letter or print a report
        if prompt_for_input(runmode) == 'thank you':
            runmode = 2
        elif prompt_for_input(runmode) == 'create report':
            runmode = 4
        elif prompt_for_input(runmode) == 'quit':
            runmode = 0


    if runmode = 2:
      # this if the create a thank you letter mode
      prompt_for_input(menu, prompt)
      if blank:
        list_of_donars()
        runmode = 2
      elif name is valid:
        runmode = 3
      else name_is_new:
         create_new_donar()
         runmode = 3


    if runmode = 3
         prompt_for_input()
           if amount is valid:
             add_amount_to_donar()
             compose_email()
             runmode = 1
           else:
              display an error message
              runmode = 3


    if runmode == 4:
        # this is the Create a Report state
        if user_input() == yes:
            list_donars()
            runmode = 1
        else:
            runmode = 1

cleanup()   # save dict to drive, etc.
return # This quits back to command line
