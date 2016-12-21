import os
import re
from smtplib import SMTP
from smtplib import SMTP_SSL
from smtplib import SMTPServerDisconnected
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

services = {
    'google': {
        'smtp': 'smtp.gmail.com',
        'domains': ['gmail', 'googlemail'],
        'port': 465,
        'secure': True
    },
    'microsoft': {
        'smtp': 'smtp-mail.outlook.com',
        'domains': ['outlook', 'hotmail'],
        'port': 587,
        'secure': False
    },
    "yahoo": {
        'smtp': "smtp.mail.yahoo.com",
        'domains': ['yahoo'],
        'port': 465,
        'secure': True
    },
    'aol': {
        'smtp': "smtp.aol.com",
        'domains': ['aol.com'],
        'port': 587,
        'secure': False
    }
}

def createMessage(conf, attachments):

    message = MIMEMultipart()

    message['From'] = conf['from']
    message['To'] = conf['to']
    message['Subject'] = conf['subject']

    for attachment in attachments:
        message.attach(buildAttachment(attachment))

    return message.as_string()

def buildAttachment(path):
    name = os.path.basename(path)
    with open(path, 'rb') as inFile:

        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(inFile.read())

    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename = name)

    return attachment

def findSMTPServer(emailDomain):
    '''
        Look through all the services to get a domain that matches with emailDomain
        an return a tuple with its smtp hots, and smtp port
    '''
    for key, service in services.items():
        if emailDomain in service['domains']:
            return service['smtp'], service['port'], service['secure']

    return None, None, None

def getDomain(emailAddress):
    return re.search(r'@(\w+)', emailAddress).groups()[0]

def sendMail(conf, message):
    host, port, secure = findSMTPServer(getDomain(conf['from']))
    result = {}

    if not host:
        raise Exception('Not supported SMTP service.')

    if secure:
        smtp = SMTP_SSL(host, port)
    else:
        smtp = SMTP(host, port)
        print(smtp.starttls())

    try:
        smtp.login(conf['from'], conf['pass'])
        result = smtp.sendmail(conf['from'], conf['to'], message)
    except SMTPServerDisconnected:
        raise Exception('Sorry we could\'t connect to the server, you should check your credendials...')
    finally:
        smtp.close()

    return result == {}
