class User:
    """describe user"""

    def __init__(self, first_name, last_name, sex):
        """user attributes"""
       
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

        """login attributes"""
        self.login_attempts = 0

    """increment login attempts"""   
    def increment_login_attempts(self):
        self.login_attempts += 1

    """reset login attempts"""
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('bob', 'brown', 'm')

print (
    f"\n{user.first_name.title()}"
    f" {user.last_name.title()}"
    f" {user.sex}"
     "\n"
    )
    
"""call increment 3 times"""
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

"""print login attempts"""
print(f"Login attempts: {user.login_attempts}")

"""Reset and print login attempts"""
user.reset_login_attempts()
print(f"After reset: {user.login_attempts}")
print("\n")