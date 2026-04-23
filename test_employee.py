
from employee.py import Employee

def test_give_default_raise():
    """test for default 5_000 raise"""
    employee = Employee('john','doe', 30_000)
    employee.give_raise()
    assert employee.salary == 3500

def test_give_custom_raise():
    """test for custom 6_000 raise"""
    employee = Employee('jane', 'doe', 35000)
    employee.give_raise(6000)
    assert employee.salary ==41000

