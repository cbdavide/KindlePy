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
from smtplib import SMTP
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from message import createMessage

options = docopt(__doc__)

if 'send' in options:

  print('This guy knows what he\'s doing. I like that.')

  msg = {}
  msg['From'] = 'david.castelblanco@hotmail.com'
  msg['To'] = 'cbdavides@gmail.com'
  msg['Subject'] = 'Buena buena'
  msg['Attachments'] = [os.path.join('.', filename) for filename in options['<file>']]

  text = createMessage(msg)

  server = SMTP('smtp-mail.outlook.com', 587)
  server.starttls()
  server.login(msg['From'], 'pass')

  server.sendmail(msg['From'], msg['To'], text)

  server.quit()
