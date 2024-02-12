import smtplib,ssl
import os

def email_send(message):
    host = "smtp.gmail.com"
    port = 465

    user = ""

    password = ""
    print(password)
    receiver = "vya4eslav.tka4enko@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user,password)
        server.sendmail(user,receiver,message)