import re

def is_strong_password(password):
    pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@\( !%?&])[A-Za-z\d@ \)!%?&]{8,}$'
    if re.match(pattern, password):
        return True
    else:
        return False

if is_strong_password("Password123@"):
    print("Strong pass")
else:
    print("Not strong pass")