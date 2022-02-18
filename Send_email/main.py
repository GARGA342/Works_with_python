from email import message
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#BODY OF EMAIL
msg = MIMEMultipart()
text = "New email!"

#DATA OF EMAIL
password = "password_of_sender"
msg['From'] = "sender_email@gmail.com"
msg['To'] = "destination_email@gmail.com"
msg['Subject'] = "SUBJECT EMAIL"

#BUILD CONNECTION
msg.attach(MIMEText(text, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()

#LOGIN
server.login(msg['From'], password)

#SEND EMAIL
server.sendmail(msg['From'], msg['To'], msg.as_string)

#CLOSE SERVER
server.quit()