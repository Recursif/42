

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename


def send_mail(send_from: str, subject: str, text: str, send_to: list, files= None):

    send_to = default_address if not send_to else send_to

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = ', '.join(send_to)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for file in files or []:
        with open(file, "rb") as fileToSend:
            # Get the extension of the file
            ext = file.split('.')[-1:]
            attachedFile = MIMEApplication(fileToSend.read(), _subtype = ext)
            attachedFile.add_header('content-disposition', 'attachment', filename=basename(file))
        msg.attach(attachedFile)

    smtp = smtplib.SMTP(host="smtp.gmail.com", port= "587")
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
    