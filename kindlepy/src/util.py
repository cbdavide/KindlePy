import sys
from validate_email import validate_email

def inputmail(prompt):
    mail = input(prompt)

    if not validate_email(mail):
        print('mmm... {} does not look like a valid email address.'.format(mail))
        sys.exit(1)

    return mail
