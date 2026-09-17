import schedule
import time
import requests
import smtplib
from email.message import EmailMessage

sender = "yasirmle16@gmail.com"
app_pass = "amxkxtayrffkzous"
receiver = "yasir.bcpsc@gmail.com"

def job():
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=24.670875&longitude=89.409741&current_weather=true"

    response = requests.get(url)

    jn = response.json()

    tt= f"Temperature: {jn["current_weather"]["temperature"]}"

    msg = EmailMessage()
    msg["Subject"] = "Temp Data by SMTP Python"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content(f"Hello! Temperature Now: {tt}\nAutomatic email by Python")

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, app_pass)
    server.send_message(msg)
    server.quit()

    print("Mail has sent successfully!")


print("Checking....")
schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

