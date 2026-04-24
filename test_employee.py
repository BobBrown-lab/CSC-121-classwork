
import pytest
from employee import Employee

@pytest.fixture
def default_employee():
    return Employee('john','doe', 30_000)

@pytest.fixture
def custom_employee():
    return Employee('jane', 'doe', 35_000)  

def test_give_default_raise(default_employee):
    """test for default 5_000 raise"""
    default_employee.give_raise()
    assert default_employee.salary == 35000

def test_give_custom_raise(custom_employee):
    """test for custom 6_000 raise"""
    custom_employee.give_raise(6000)
    assert emp.salary == 41000
