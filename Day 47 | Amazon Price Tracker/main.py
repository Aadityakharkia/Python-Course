import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

# ------------------------------------------------Url and Header to pass auth. ---------------------------------------------

Amazon_Product_Url = "https://www.amazon.in/AP-Calculus-Premium-2022-2023-Comprehensive/dp/1506263941/ref=sr_1_2?crid=1YQJQPY5CCBP0&keywords=ap+calculus+bc+barron&qid=1675129467&sprefix=ap+calculus+bc+barro%2Caps%2C217&sr=8-2"

header_for_amazon_requests ={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language":"en"
}

# --------------------------------------------- Extracting the price from Amazon ----------------------------------------

response = requests.get(Amazon_Product_Url,headers=header_for_amazon_requests)

soup = BeautifulSoup(response.text,"lxml")
price = soup.find("span", class_="a-size-base a-color-price a-color-price").get_text()

# ---------------------------------------- Extracting the vale and converting into float ------------------------------

price_without_currency = price.split("₹")[1]
price_without_comma = price_without_currency.replace(",","")
price_as_float = float(price_without_comma)
print(price_as_float)

# -------------------------------------------------- Emailing and monotiring ---------------------------------------------

BUY_PRICE = 2000

Host_Email_ID = "aadityakharkiatest@gmail.com"
Receivers_Email_Id = "aadityakharkia10@gmail.com"
Password = "pxduwpgyfmtvtzmj"

if price_as_float < BUY_PRICE:
    message = f"AP-Calculus-Premium-2022-2023 is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=Host_Email_ID, password=Password)
        connection.sendmail(
            from_addr=Host_Email_ID,
            to_addrs=Receivers_Email_Id,
            msg=f"Subject:Amazon Price Alert!\n\n The Price Has Dropped ! Go and buy it Now ! \n\n{message}"
        )