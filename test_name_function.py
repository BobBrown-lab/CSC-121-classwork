
from name_function import get_formatted_name

def test_first_last_name():
    """test for name"""
    formatted_name = get_formatted_name('robert', 'brown')
    assert formatted_name == 'Robert Brown'
