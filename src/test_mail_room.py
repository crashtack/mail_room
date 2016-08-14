# -*- coding: utf-8 -*-
import pytest


STATE4_TABLE = [
    (10, 10),
    (11, 11),
    # ('0', SystemExit),
]
# def test_mailroom():
    # from mailroom_functions import mailroom_functions


def test_mailroom_initialize_donor_dict():
    from mailroom_functions import initialize_donor_dict
    assert type(initialize_donor_dict()) == dict


def test_list_of_donors():
    from mailroom import list_of_donors


def test_state2():
    from mailroom_functions import state_2_valid_responses


def test_state4_1():
    from mailroom import state_4_valid_responses
    assert state_4_valid_responses('10') == 10


def test_update_donor():
    from mailroom import update_donor
    from mailroom import DONORS
    assert update_donor('John Doe') == DONORS['John Doe']


@pytest.mark.parametrize('a, result', STATE4_TABLE)
def test_state4_2(a, result):
    from mailroom import state_4_valid_responses
    assert state_4_valid_responses(a) == result





# @pytest.mark.parametrize('m, n, result', ACK_TABLE)
# def test_akermann(m, n, result):
#     from ackermann import ackermann
#     assert ackermann(m, n) == result
