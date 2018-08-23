from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os


def sendemail(email, bodyInformation):
    try:
        cc = [os.environ['EMAIL']]

        emailServer = smtplib.SMTP('smtp.gmail.com', 587)
        emailServer.starttls()
        emailServer.login(os.environ['EMAIL'], os.environ['EMAIL_PASSWORD'])

        message = MIMEMultipart()

        message['From'] = os.environ['EMAIL']
        message['To'] = email
        message['CC'] = ",".join(cc)
        cc.append(email)
        message['Subject'] = "I'll be in touch soon"

        body = bodyInformation
        message.attach(MIMEText(body, 'plain'))

        emailServer.sendmail(os.environ['EMAIL'], cc, message.as_string())
        emailServer.quit()

    except KeyError as e:

        print(e + 'Missing Email or Password, no email was sent')
        return e + 'Missing Email or Password, no email was sent'

    return "Email successful"