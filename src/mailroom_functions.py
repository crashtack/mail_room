# -*- coding: utf-8 -*-
''' main mailroom script file '''


def initialize_donor_dict():
    '''function to create the dictionary of dictionary to hold donor information'''
    John_Doe = {'name': 'John Doe','total_donation': 0,'num_donations': 0,'avg_donation': 0,'last_donation': 0}
    Neil_Armstrong = {'name': 'Neil Armstrong','total_donation': 23000000,'num_donations': 4,'avg_donation': 5750000,'last_donation': 10000000}
    Sara_Smith = {'name': 'Sara Smith','total_donation': 100,'num_donations': 2,'avg_donation': 50,'last_donation': 35}
    Ralf_the_Dog = {'name': 'Ralf the Dog','total_donation': 1000,'num_donations': 1,'avg_donation': 1000,'last_donation': 1000}

    donor_dict = {'John Doe': John_Doe,
                  'Neil Armstrong': Neil_Armstrong,
                  'Sara Smith': Sara_Smith,
                  'Ralf the Dog': Ralf_the_Dog
                  }

    return donor_dict


def list_of_donars(donor_dict):
        ''' print the list of donor names '''
        for donor in donor_dict:
            print(donor['name'])

        print the entire donar list
        for donar in donars:
            print(donar(keyname))

def mailroom():
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


        if runmode == 2:
          # this if the create a thank you letter mode
          prompt_for_input(runmode)
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
