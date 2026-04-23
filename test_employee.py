
from employee import Employee

def test_give_default_raise():
    """test for default 5_000 raise"""
    emp = Employee('john','doe', 30_000)
    emp.give_raise()
    assert emp.salary == 3500

def test_give_custom_raise():
    """test for custom 6_000 raise"""
    emp = Employee('jane', 'doe', 35000)
    emp.give_raise(6000)
    assert emp.salary ==41000

