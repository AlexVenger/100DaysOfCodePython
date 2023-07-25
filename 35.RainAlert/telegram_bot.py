#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import json
import logging
import requests
from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

with open("api_key.json") as key_file:
    data = json.load(key_file)
    bot_token = data["bot_key"]
    user_id = data["user_id"]
    api_key = data["api_key"]

users = {}
last_command = ""


def rain_warning(city_country):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city_country,
        "appid": api_key
    }
    response = requests.get(url, params)
    response.raise_for_status()
    f_data = response.json()
    f_country = f_data["city"]["country"]
    f_city = f_data["city"]["name"]
    data_list = f_data["list"]
    for f_data in data_list:
        for weather_data in f_data["weather"]:
            if weather_data["id"] < 700:
                return f"Umbrella situation in {f_city}, {f_country}"


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    users[user] = {"id": user.id}
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Welcome to the rain (or precipitation in general) warning bot! Type /city command"
        rf" to begin."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


async def city(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await context.bot.send_message(chat_id=users[user]["id"], text="Please type the city name")
    global last_command
    last_command = "city"


async def save_city(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    city_name = update.message.text
    users[user]["city"] = city_name
    await context.bot.send_message(chat_id=users[user]["id"], text=f"City {city_name} was set to your account. "
                                                                   f"You'll be receiving a warning message if it's "
                                                                   f"going to rain in {city_name} today. Please, "
                                                                   f"add a country name by typing /country because "
                                                                   f"there may be several cities with the same name in "
                                                                   f"different countries")


async def country(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await context.bot.send_message(chat_id=users[user]["id"], text="Please type the country name")
    global last_command
    last_command = "country"


async def save_country(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    country_name = update.message.text
    users[user]["country"] = country_name
    await context.bot.send_message(chat_id=users[user]["id"], text=f"Country {country_name} was set to your account.")
    if "country" in users[user].keys():
        rain = rain_warning(f"{users[user]['city']},{users[user]['country']}")
    else:
        rain = rain_warning(f"{users[user]['city']}")
    if rain is not None:
        await context.bot.send_message(chat_id=users[user]["id"], text=rain)


async def save_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global last_command
    if last_command == "city":
        await save_city(update, context)
    elif last_command == "country":
        await save_country(update, context)
    else:
        await echo(update, context)
    last_command = ""


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(bot_token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(CommandHandler("city", city))
    application.add_handler(CommandHandler("country", country))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_input))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
