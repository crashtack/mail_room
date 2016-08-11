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
                  'Ralf the Dog': Ralf_the_Dog,
                  }

    return donor_dict


def list_of_donors(donor_dict):
        ''' print the list of donor names '''
        for donor in donor_dict.values():
            # print(donor)
            print(donor['name'])

        # print the entire donar list
        # for donar in donars:
        #     print(donar(keyname))

# John_Doe = {'name': 'John Doe','total_donation': 0,'num_donations': 0,'avg_donation': 0,'last_donation': 0}
# print(John_Doe)
# print(John_Doe['name'])
print(list_of_donors(initialize_donor_dict()))
