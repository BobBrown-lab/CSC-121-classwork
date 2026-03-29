class User:
    """describe user"""

    def __init__(self, first_name, last_name, sex, login_attempts=0):
        """user attributes"""
       
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.login_attempts = login_attempts

    def increment_login_attempts(login_attempts):
        me.login_attempts += 1
        print(me.login_attempts)


        me.increment_login_attempts
        me.increment_login_attempts
        me.increment_login_attempts
     
     
me = User('bob', 'brown', 'm', 0)

print (
    f"\n{me.first_name.title()}"
    f" {me.last_name.title()}"
    f" {me.sex}"
    f" {me.login_attempts}"
    "\n"
    )
    

 