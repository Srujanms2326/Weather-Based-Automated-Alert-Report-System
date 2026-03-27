import smtplib
from email.mime.text import MIMEText

def send_email(alerts):
    sender = "your_email@gmail.com"
    password = "your_app_password"
    receiver = "receiver@gmail.com"

    message = MIMEText("\n".join(alerts))
    message["Subject"] = "Weather Alert 🚨"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())
    server.quit()