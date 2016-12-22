import re
import os
from validate_email import validate_email

CONFIG_FILE_PATH = os.path.expanduser('~/.config/kindlepy')
CONFIG_FILE_NAME = 'config'

def readConfig():
    config_file = prepareConfigFile()
    conf = {}

    with open(config_file, 'r') as input:
        data = input.readlines()
        data = [x.strip('\n') for x in data]

        for field in data:
            kind, value = re.search(r'([a-z]+)=([\w.@]+)', field).groups()
            conf[kind] = value

        return conf

def writeConfig(conf):
    config_file = prepareConfigFile()
    with open(config_file, 'w') as output:
        for key, value in conf.items():
            output.write('{}={}{}'.format(key, value, '\n'))

def set(kind, email):
    if validate_email(email):
        conf = readConfig()
        conf[kind] = email
        writeConfig(conf)
    else:
        raise Exception('It seems that the email does not have a valid syntax.')

def prepareConfigFile():
    '''
        Checks whether or not the config file is exist
        and returns the absolute path of the file
        (The config file is created in case that it does not exist)
    '''
    file_path = os.path.join(CONFIG_FILE_PATH, CONFIG_FILE_NAME)
    if not os.path.exists(CONFIG_FILE_PATH):
        os.makedirs(CONFIG_FILE_PATH)
        with open(file_path, 'w') as fp:
            pass
    return file_path
