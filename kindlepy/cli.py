"""KindlePy

  CLI to send emails to your kindle device.

  Usage:
    kindlepy send <file>...
    kindlepy -h | --help
    kindlepy -v |   --version

  Options:
    -h --help     Show this screen.
    --version     Show version.

"""
import os
from . import util
from docopt import docopt
from . import mail
from getpass import getpass

def main():
    options = docopt(__doc__)

    if 'send' in options:

        print('This guy knows what he\'s doing. I like that.')

        msg = {}
        msg['from'] = util.inputmail('Input your email address: ')
        msg['pass'] = getpass('Input your password: ')
        msg['to'] = util.inputmail('Input your kindle address: ')
        msg['subject'] = 'Book'

        attachments = [os.path.join('.', filename) for filename in options['<file>']]

        envelope = mail.createMessage(msg, attachments)

        print(mail.sendMail(msg, envelope))
