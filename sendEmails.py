# Assignment: Setup an SMTP server and send emails
#------------------------
# Key learning: In order for this to work, go to gmail account -> 
#               ALLOW ACCESS TO LESS SECURE APPS IN THE SETTINGS sections
#               Library SMTPLIB for smtp server
#               For email structuring: email.mime.text
#--------------------------
import smtplib as slib
from email.mime.text import MIMEText

msg = MIMEText("This is a test mail from Python Script")

msg['Subject'] = "Test email from Amarjeet"
msg['To'] = "amarjeet.dua@optym.com"
msg['From'] = "nippydua@gmail.com"

s=slib.SMTP_SSL("smtp.gmail.com",465)
#s.starttls()
s.login("nippydua@gmail.com", "<<mypasswordhere>>")
s.send_message(msg)
s.quit()