"""KindlePy

  CLI to send emails to your kindle device.

  Usage:
    kindlepy send <file>...
    kindlepy config (-l | --list)
    kindlepy config --sender <sender_email>
    kindlepy config --receiver <receiver_email>
    kindlepy config --sender <sender_email> --receiver <receiver_email>
    kindlepy -h | --help
    kindlepy -v | --version

  Options:
    --sender      Set the sender's email
    --receiver    Set the receiver's email
    --l --list    List the sender and receiver email
    -h --help     Show this screen.
    -v --version  Show version.

"""
import os
import sys
from docopt import docopt
from getpass import getpass
from . import __version__ as VERSION
from kindlepy.src import mail, config, util

def main():
    options = docopt(__doc__)

    if options['send']:
        msg = {}
        conf = config.readConfig()

        if 'sender' in conf:
            msg['from'] = conf['sender']
        else:
            msg['from'] = util.inputmail('Input the sender email address: ')

        msg['pass'] = getpass('Input the sender email password: ')

        if 'receiver' in conf:
            msg['to'] = conf['receiver']
        else:
            msg['to'] = util.inputmail('Input the receiver email address: ')

        msg['subject'] = 'Book'

        attachments = [os.path.join('.', filename) for filename in options['<file>']]

        envelope = mail.createMessage(msg, attachments)

        try:
            if mail.sendMail(msg, envelope):
                print('The documents were successfully sent.')
        except Exception as err:
            print(err)

        sys.exit(0)

    if options['config']:
        if options['<sender_email>']:
            setField('sender', options['<sender_email>'])
        if options['<receiver_email>']:
            setField('receiver', options['<receiver_email>'])

        if options['-l'] or options['--list']:
            conf = config.readConfig()
            for key, value in conf.items():
                print('{}: {}'.format(key, value))

        sys.exit(0)

    if options['--version']:
        print(VERSION)
        sys.exit(0)


def setField(kind, email):
    '''
        Auxiliary function to deal with exceptions in a cleaner way.
    '''
    try:
        config.set(kind, email)
    except Exception as err:
        print(err)
        sys.exit(1)

if __name__ == '__main__':
    main()
