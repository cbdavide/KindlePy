import os
from smtplib import SMTP
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

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

def sendMail(conf, message):

    with SMTP('smtp-mail.outlook.com', 587) as smtp:
        print(smtp.starttls())
        print(smtp.login(conf['from'], conf['pass']))

        return smtp.sendmail(conf['from'], conf['to'], message)
