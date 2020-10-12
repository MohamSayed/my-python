# -*- coding: utf-8 -*-
import smtplib

def prompt(prompt):
    return input(prompt).strip()

fromaddr = "elsayedmohamed829@yahoo.com"
toaddrs  = "apitest160@gmail.com"
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message length is", len(msg))

server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
server.connect("smtp.mail.yahoo.com", 465)
server.ehlo()
server.starttls()
server.ehlo()
server.login("elsayedmohamed829@yahoo.com", "lC7JadIUo1NX")
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()