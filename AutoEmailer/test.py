

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Sender account
gmail_user = 'terry@radicalagreement.com'
gmail_password = 'M1ch1oKaku'

#List of recipients
recipients = [
    {'name': 'Terry', 'email': 'terry@radicalagreement.com'},
    {'name': 'Terry', 'email': 'terrywithers@gmail.com'},
    {'name': 'Paul', 'email': 'board@macramemore.org'},    
    # Add more recipients as needed
]

#Email subject
subject = 'Testing The Awesome Power Of AutoEing!!!!'

#Connect to Sender Email Account (Gmail Only)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gmail_user, gmail_password)

#Loop through each recipient and send the email
for recipient in recipients:
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = recipient['email']
    msg['Subject'] = subject

    #Email body
    body = 'Dear {},\n\nCan you feel it?  Yeah!  What a feeling! To be be AutoEiiiinnngggg!'.format(recipient['name'])
    msg.attach(MIMEText(body, 'plain'))

    #Send the email
    server.send_message(msg)

    # Wait for 100 seconds
    time.sleep(100)

# Close the connection to the email server
server.quit()


