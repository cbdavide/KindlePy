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
from docopt import docopt
from mail import sendMail, createMessage

options = docopt(__doc__)

if 'send' in options:

  print('This guy knows what he\'s doing. I like that.')

  msg = {}
  msg['from'] = ''
  msg['pass'] = ''
  msg['to'] = ''
  msg['subject'] = 'Book'

  attachments = [os.path.join('.', filename) for filename in options['<file>']]

  envelope = createMessage(msg, attachments)

  sendMail(msg, envelope)
