def prompt_for_input(menu, prompt):
    '''"Request user input based on current runmode'''
    print(menu)
    return input(prompt)




    if runmode == 1:
        # main input
        prompt_for_input(menu, prompt)
        menu = ''What would you like to do:
                            \t[1] Print a Report of donors and donation history.
                            \t[2] Send a Thank You email for a new donation.
                            \t[3] Quit the Program"
        prompt = 'Enter a numerical selection: '
       
        if reply == 1:
            return 'You have chosen to print a report.'
        elif reply == 2:
            return 'You have chosen to send a thank you email.'
        elif reply == 3:
            return 'You have chosen to end the program'
        else:
            prompt_for_input(runmode)

    if runmode == 2:
        prompt for different input

    if runmode == 3:
        prompt for different input

    if runmode == 4:
        prompt for differetn input