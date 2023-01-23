# This programme sends birthday wishes to your friend automatically

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "Your mail Id"
MY_PASSWORD = "your password"

today = datetime.now()
today_tuple = (today.month, today.day)

#---------------------------------------------------Reading Files through Pandas -------------------------------------
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#--------------------------------------------------- Selecting tempelate and sending mail --------------------------
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

# Sending Mail

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
