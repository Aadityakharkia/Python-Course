import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

News_API_Key = "9c17299b1b4f46609aba430f1c471d91"
Stock_API_Key = "G4FGUZ9J3DDHXGBT"

Account_SID = "AC3cc0660bec8ec35159d570a1e4237a04"
Auth_Token = "c28c83d570ec564e8b9bfaec6788d928"
Number = "+13607806746"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
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

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round(difference/float(yesterday_closing_price))*100
Up_Down = None
if difference > 0:
    Up_Down = "🔺"
else:
    Up_Down = "🔻"

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 2:
    print("Get News")

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent) > 2:
    news_params = {
        "apiKey":News_API_Key,
        "qInTitle":COMPANY_NAME,

    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[0:3]
print(three_articles)

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"{STOCK_NAME}:{Up_Down}{diff_percent}% \nHeadline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio.
client = Client(Account_SID, Auth_Token)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_=Number,
        to='+918092338438'
    )

    print(message.sid)