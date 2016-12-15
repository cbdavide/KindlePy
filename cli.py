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

from docopt import docopt

options = docopt(__doc__)

if 'send' in options:
  print('This guy knows what he\'s doing. I like that.')
