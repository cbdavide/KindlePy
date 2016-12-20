import re
from validate_email import validate_email

def readConfig():
    conf = {}
    with open('data', 'r') as input:
        data = input.readlines()
        data = [x.strip('\n') for x in data]

        for field in data:
            kind, value = re.search(r'([a-z]+)=([\w.@]+)', field).groups()
            conf[kind] = value

        return conf

def writeConfig(conf):
    with open('data', 'w') as output:
        for key, value in conf.items():
            output.write('{}={}{}'.format(key, value, '\n'))

def set(kind, email):
    if validate_email(email):
        conf = readConfig()
        conf[kind] = email
        writeConfig(conf)
    else:
        raise Exception('It seems that the email does not have a valid syntax.')

if __name__ == '__main__':
    print(readConfig())
    # set('sender', 'new55sender@gmail.com')
    # print(readConfig())
    set('receiver', 'newrec33eiver')
    print(readConfig())
