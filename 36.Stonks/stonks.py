import requests
import json
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

with open("keys.json") as keys_file:
	keys = json.load(keys_file)
	alpha_vantage_key = keys["alpha_vantage_key"]
	news_api_key = keys["news_api_key"]
	bot_token = keys["bot_key"]
	user_id = keys["user_id"]

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
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
"""


def build_message(delta: int, articles: list) -> str:
	triangle = "🔺" if delta > 0 else "🔻"
	message = f"{COMPANY_NAME}: {triangle}{abs(delta)}%\n"
	for article in articles:
		p_article = f"Headline: {article['title']}\nBrief: {article['description']}\nURL: {article['url']}\n"
		message += p_article
	return message


def send_to_telegram(message):
	api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
	try:
		requests.post(api_url, json={'chat_id': user_id, 'text': message})
	except Exception as e:
		print(e)


def get_stock_info():
	alpha_vantage_url = "https://www.alphavantage.co/query"
	alpha_vantage_params = {
		"function": "TIME_SERIES_DAILY",
		"symbol": STOCK,
		"apikey": alpha_vantage_key
	}
	r = requests.get(url=alpha_vantage_url, params=alpha_vantage_params)
	r.raise_for_status()
	data = r.json()
	time_series = data["Time Series (Daily)"]
	yesterday = datetime.date.today() - datetime.timedelta(days=1)
	day_before_yesterday = yesterday - datetime.timedelta(days=1)

	prev_stonk = time_series[str(day_before_yesterday)]
	stonk = time_series[str(yesterday)]
	delta = float(stonk["1. open"]) * 100 / float(prev_stonk["1. open"])
	if delta > 105 or delta < 95:
		get_and_send_news(delta - 100)


def get_and_send_news(delta):
	news_api_url = "https://newsapi.org/v2/everything"
	news_api_params = {
		"q": COMPANY_NAME,
		"from": str(datetime.date.today() - datetime.timedelta(days=30)),
		"sortBy": "publishedAt",
		"apiKey": news_api_key
	}
	r = requests.get(url=news_api_url, params=news_api_params)
	r.raise_for_status()
	data = r.json()
	articles = data["articles"][0:3]
	message = build_message(round(delta), articles)
	send_to_telegram(message)


get_stock_info()
