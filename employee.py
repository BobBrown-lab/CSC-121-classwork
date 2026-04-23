
class Employee:

    """model an employee and salary"""
    def __init__(self, first_name, last_name, salary):

        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
       
    """raise function"""
    def give_raise(self, amount=5000):
        self.salary += amount

"""instance employee_one"""
employee_one = Employee('john', 'doe', 30_000)
employee_one.give_raise()

"""instance employee_two"""
employee_two = Employee('jane', 'doe', 35_000)
employee_two.give_raise(6000)

print(employee_one.first_name, employee_one.last_name, employee_one.salary)
print(employee_two.first_name, employee_two.last_name,employee_two.salary)
