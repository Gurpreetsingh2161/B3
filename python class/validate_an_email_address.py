import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    if re.match(pattern, email):
        return True
    else:
        return False

emails=["thrjr@gmail.com", "thrj222r@gmail.com", "thrj r@gmail.com", "thrjr@gmail.com", "thr\njr@gmail.com", "thrjr@gmail.com"]

for email in emails:
    if is_valid_email(email):
            print(f"{email} is valid.")
    else:
            print(f"{email} is invalid.")