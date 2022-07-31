import telebot
import requests
import traceback

bot = telebot.TeleBot("1874273085:AAGSGG9QZjaqmIRCSpGLUYWFLAGpftCsGP8")
CODES = (403, 429, 418)
URL = "https://api1.binance.com"

@bot.message_handler(commands = ['start'])
def start(message):
	first_name = message.from_user.first_name
	bot.reply_to(message, f"👋👋👋 Welcome {first_name}! 👋👋👋"
		"\n\nI am PriceCryptosBot🤖, I can show you the prices of cryptocurrencies."
		"\n\nBinance address for donations:❤️❤️❤️"
		"\n\n✅TRX TRC20 (TN5V6q9LxMs8R9Yf4zEBwgYDE2iKjGA9Nk)"
		"\n✅USDT TRC20 (TN5V6q9LxMs8R9Yf4zEBwgYDE2iKjGA9Nk)")



@bot.message_handler(commands = ['price'])
def price(message):
	try:
		if message.text[6] != " ":
			bot.reply_to(message, "ERROR‼️‼️"
				"\n\nCommand format: /price token"
				"\n\nExample: /price btc or /price BTC")

		else:
			token = message.text[7:].upper()
			respont = requests.get(URL + f"/api/v3/trades?symbol={token}USDT&limit=1")

			if respont.status_code == 200:
				price = respont.json()[0]["price"]
				bot.reply_to(message, f"💰 Price[USD] ${token}: ${price}")


			elif respont.status_code in CODES or respont.status_code >= 500:
				bot.reply_to(message, "ERROR DE API, no usar mas la API")

			else:
				bot.reply_to(message, "ERROR: THE CRYPTOCURRENCY DOES NOT EXIST")

	except:
		traceback.print_exc()
		bot.reply_to(message, "ERROR‼️‼️"
			"\n\nCommand format: /price token"
			"\n\nExample: /price btc or /price BTC")
	


@bot.message_handler(commands = ['trade'])
def trade(message):
	try:
		if message.text[6] != " ":
			bot.reply_to(message, "ERROR‼️‼️"
				"\n\nCommand format: /trade pair"
				"\n\nExample: /trade btc usdt or /trade ETH USDT")

		else:
			token = message.text[7:].upper()
			token = token.split()
			token_1 = token[0]
			token_2 = token[1]
			respont = requests.get(URL + f"/api/v3/trades?symbol={token_1}{token_2}&limit=1")

			if respont.status_code == 200:
				price = respont.json()[0]["price"]
				bot.reply_to(message, f"💰 Price[USD] {token_1}/{token_2}: ${price}")


			elif respont.status_code in CODES or respont.status_code >= 500:
				bot.reply_to(message, "ERROR DE API, no usar mas la API")

			else:
				bot.reply_to(message, "ERROR: THE CRYPTOCURRENCY DOES NOT EXIST")

	except:
		traceback.print_exc()
		bot.reply_to(message, "ERROR‼️‼️"
			"\n\nCommand format: /trade pair"
			"\n\nExample: /trade btc usdt or /trade ETH USDT")



@bot.message_handler(commands = ['help'])
def help(message):
	first_name = message.from_user.first_name
	bot.reply_to(message, f"Hi 👋👋👋, {first_name}!"
		"\n\nTo make your queries please use the following commands:"
		"\n\n/price - To check the price of any cryptocurrency"
		"\n/trade - To check the price of a pair"
		"\n/exchange - "
		"\n/calc - ")



@bot.message_handler(commands = ['exchange'])
def exchange(message):
	bot.reply_to(message, "Exchange💸💸💸"
		"\n\n✅Binance: https://accounts.binance.me/es-la/register?ref=WHK9HW8Y"
		"\n✅OKEX: https://www.okex.com/join/3212839"
		"\n✅LATOKEN: https://latoken.com/invite?r=5twvq9gk")


@bot.message_handler(commands = ['calc'])
def  calc(message):
	try:
		token = message.text[6:].upper()
		token = token.split()
		token_1 = token[0]
		token_2 = token[1]
		token_3 = token[2]

		respont = requests.get(URL + f"/api/v3/trades?symbol={token_2}{token_3}&limit=1")

		if respont.status_code == 200:
			price = respont.json()[0]["price"]
			total = float(price) * float(token_1)
			bot.reply_to(message, f"💰 Price[USD] {token_2}/{token_3}: ${total}")

		else:
			bot.reply_to(message, "ERROR: THE CRYPTOCURRENCY DOES NOT EXIST")

		
	except:
		traceback.print_exc()
		bot.reply_to(message, "ERROR‼️‼️"
			"\n\nCommand format: /calc amount token1 token2"
			"\n\nExample: /calc 2 btc usdt or /calc 5 ETH BTC")


	
bot.polling()