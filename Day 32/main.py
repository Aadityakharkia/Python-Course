'''
import smtplib

my_email = "aadityakharkiatest@gmail.com"
password = "pxduwpgyfmtvtzmj"

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="aadityakharkia10@gmail.com",msg="Hello\n\n This is the body of my mail")


import datetime as dt

now = dt.datetime.now()
print(now)
'''

#