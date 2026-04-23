from employee import Employee

def test_give_default_raise():
    """test for default 5_000 raise"""
    emp = Employee('john','doe', 30_000)
    emp.give_raise()
    assert emp.salary == 35000
