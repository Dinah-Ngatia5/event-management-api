import re

def validate_register_form(username, email, password):
    if len(username) < 3 or len(email) < 5 or len(password) < 6:
        return False

    email_regex = r'^\S+@\S+\.\S+$'
    if not re.match(email_regex, email):
        return False

    return True

def validate_login_form(email, password):
    if len(email) < 5 or len(password) < 6:
        return False

    email_regex = r'^\S+@\S+\.\S+$'
    if not re.match(email_regex, email):
        return False

    return True
