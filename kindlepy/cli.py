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
import util
from docopt import docopt
from mail import sendMail, createMessage
from getpass import getpass

options = docopt(__doc__)

if 'send' in options:

  print('This guy knows what he\'s doing. I like that.')

  msg = {}
  msg['from'] = util.inputmail('Input your email address: ')
  msg['pass'] = getpass('Input your password: ')
  msg['to'] = util.inputmail('Input your kindle address: ')
  msg['subject'] = 'Book'

  attachments = [os.path.join('.', filename) for filename in options['<file>']]

  envelope = createMessage(msg, attachments)

  print(sendMail(msg, envelope))
