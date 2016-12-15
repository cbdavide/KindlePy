"""
    Message

    Responsabilities:
        - Create the message
        - Add all the attachments
        - Return the whole message as a string

"""
import os
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

def createMessage(msg):

    message = MIMEMultipart()

    message['From'] = msg['From']
    message['To'] = msg['To']
    message['Subject'] = msg['Subject']

    for attachment in msg['Attachments']:
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
