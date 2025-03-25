# utils/helpers.py
def validate_email(email):
    return "@" in email and "." in email
