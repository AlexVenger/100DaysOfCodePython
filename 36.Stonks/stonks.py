import requests
import json
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

with open("keys.json") as keys_file:
	keys = json.load(keys_file)
	alpha_vantage_key = keys["alpha_vantage_key"]

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

alpha_vantage_url = \
	'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
alpha_vantage_params = {
	"function": "TIME_SERIES_DAILY",
	"symbol": STOCK,
	"apikey": alpha_vantage_key
}
r = requests.get(url=alpha_vantage_url, params=alpha_vantage_params)
data = r.json()
time_series = data["Time Series (Daily)"]
yesterday = datetime.date.today() - datetime.timedelta(days=1)
day_before_yesterday = yesterday - datetime.timedelta(days=1)

prev_stonk = time_series[str(day_before_yesterday)]
stonk = time_series[str(yesterday)]
delta = float(stonk["1. open"]) * 100 / float(prev_stonk["1. open"])
if delta > 105 or delta < 95:
	print("Get News")


with open("stonks.json", "w") as stonk_file:
	json.dump(data, stonk_file, indent=2)
