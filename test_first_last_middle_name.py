
from name_function import get_formatted_name

def test_first_last_middle_name():
    """test name"""
    formatted_name = get_formatted_name('robert', 'brown', 'hunter')
    assert formatted_name == 'Robert Hunter Brown'
