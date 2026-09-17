import smtplib
from email.message import EmailMessage

sender = "yasirmle16@gmail.com"
app_pass = "amxkxtayrffkzous"
receiver = "yasir.bcpsc@gmail.com"

msg = EmailMessage()
msg["Subject"] = "Test Email by SMTP Python"
msg["From"] = sender
msg["To"] = receiver
msg.set_content("Hello! This is a sample mail.\nAutomatic email by Python")

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender, app_pass)
server.send_message(msg)
server.quit()

print("Mail has sent successfully!")


