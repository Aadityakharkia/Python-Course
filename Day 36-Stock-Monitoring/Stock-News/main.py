import requests

# ---------------------------------- Set Values ----------------------------------------------------------------------------------------
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

News_API_Key = "Your Key"
Stock_API_Key = "Your Key"

Account_SID = "Your ID"
Auth_Token = "Your Key"
Number = "Your Number"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# ---------------------------Getting data from the website and extracting the closing price for last 2 days ------------------------------

perimeters_stock = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK_NAME,
    "apikey":Stock_API_Key
}

response_stock= requests.get(STOCK_ENDPOINT,params=perimeters_stock)
data = response_stock.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# ----------------------------- Finding Difference between the closing prices --------------------------------------------------------------
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

diff_percent = difference/float(yesterday_closing_price)*100


if float(yesterday_closing_price) - float(day_before_yesterday_closing_price) > 0:
    sign = "Increased by approximately "
else:
    sign = "Decreased by approximately "
# ----------------------------- Getting News related to Company ----------------------------------------------------------------------------
if abs(diff_percent) > 2:
    news_params = {
        "apiKey":News_API_Key,
        "qInTitle":COMPANY_NAME,

    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

three_articles = articles[0:3]

formatted_articles = [f"{STOCK_NAME}:{sign }{round(diff_percent)}% \nHeadline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]

for i in formatted_articles:
    print(i,end="\n\n\n")

# ----------------------------- Future Works ------------------------------------------------------------------------------------------

# Adding SMS ALERT
# Automating it with Different Stocks
# Getting News From better sources and making it user friendly