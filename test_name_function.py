
from name_function import get_formatted_name

def test_first_last_name():
    """test for average name"""
    formatted_name = get_formatted_name('bob brown')
    assert formatted_name == 'Bob Brown'

