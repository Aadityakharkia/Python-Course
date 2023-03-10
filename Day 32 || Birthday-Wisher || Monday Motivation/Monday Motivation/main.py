# Sending Motivation mails on monday

import smtplib
import datetime as dt
import random

my_email = "aadityakharkia10@gmail.com"
password = "pxduwpgyfmtvtzmj"

now = dt.datetime.now()
weekday = now.weekday()

#-------------------------------------------- Importng quotes -----------------------------------------------------------------
if weekday ==2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
#--------------------------------------------- Sending Mail ID ----------------------------------------------------------
    print(quote)
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="prafbaccc@gmail.com",msg=f"Monday Motivation\n\n{quote}")

#------------------------------------------------Future Work -------------------------------------------------------------

# Uploading it on PythonAnywhere to automate