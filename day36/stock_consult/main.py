import requests
from twilio.rest import Client

COMPANY_NAME = "Tesla Inc"
API_KEY_NEWS = "80d5b68c7c504c0185fae40abd10a6c3"

TWILIO_SD = "AC4f41fd005d033ae5cb83f17268995d9a"
TWILIO_AT = "3dc92f6f6e79c9e7dd499cefebc42127"
STOCK = "TSLA"
API_KEY_ALPHAVANTAGE = "8ZM33IKAQ9IOZJAR"
INTERVAL = "60min"
FUNCTION = "TIME_SERIES_DAILY"

parameters_alphavantage = {
    "function":FUNCTION,
    "symbol":STOCK,
    "apikey":API_KEY_ALPHAVANTAGE,
}
parameters_news = {
    "q":COMPANY_NAME,
    "from":"2025-04-16",
    "sortBy":"publishedAt",
    "apiKey":API_KEY_NEWS,
}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response_alpha = requests.get("https://www.alphavantage.co/query?",params=parameters_alphavantage)
response_alpha.raise_for_status()
data_alpha = response_alpha.json()
yesterday = data_alpha['Time Series (Daily)']["2025-05-14"]["4. close"]
today = data_alpha['Time Series (Daily)']["2025-05-15"]["4. close"]

percentage = (float(yesterday) - float(today)) /float(yesterday) * 100

up_down = None
if percentage > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
response_news = requests.get("https://newsapi.org/v2/everything?",params=parameters_news)
response_news.raise_for_status()
data_news = response_news.json()

title = data_news["articles"][0]["title"]
description = data_news["articles"][0]["description"]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
client = Client(TWILIO_SD,TWILIO_AT)
message = client.messages.create(body=f"{STOCK}: {up_down}{percentage}%\n{title}\n{description}",from_="+18312082592",to="+5527998996531")
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

