# Learning about SMTP Protocol and sending email

import smtplib

my_email = "Your authorized mail"
password = "Your Password"

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="The mail id you want to send email to",msg="Hello\n\n This is the body of my mail")

#-------------------------------------------------------------------------------------------------------------------------
# Learning about datetime module

import datetime as dt

now = dt.datetime.now()
print(now)
