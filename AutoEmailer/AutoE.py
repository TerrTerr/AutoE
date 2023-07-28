import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Your Gmail account details
gmail_user = 'your-email@gmail.com'
gmail_password = 'your-password'

# List of recipients
recipients = [
    {'name': 'Rob', 'email': 'rob@example.com'},
    {'name': 'Diane', 'email': 'diane@example.com'},
    {'name': 'Teddy', 'email': 'teddy@example.com'},
    # Add more recipients as needed
]

# Email subject
subject = 'Your Subject Here'

# Connect to Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gmail_user, gmail_password)

# Loop through each recipient and send the email
for recipient in recipients:
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = recipient['email']
    msg['Subject'] = subject

    # Email body
    body = 'Dear {},\n\nYour email body here.'.format(recipient['name'])
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server.send_message(msg)

    # Wait for 100 seconds
    time.sleep(100)

# Close the connection to the email server
server.quit()