import os
import json
import requests
import pandas as pd
from flask    import Flask, request, Response

# constants
TOKEN = '2045023714:AAH3Api8QrgyEd7kOnW2G1gBz3ER6a_rcyI'

# # Info about the Bot
# https://api.telegram.org/bot2045023714:AAH3Api8QrgyEd7kOnW2G1gBz3ER6a_rcyI/getMe

# # Get updates
# https://api.telegram.org/bot2045023714:AAH3Api8QrgyEd7kOnW2G1gBz3ER6a_rcyI/getUpdates

# # Webhook
# https://api.telegram.org/bot2045023714:AAH3Api8QrgyEd7kOnW2G1gBz3ER6a_rcyI/setWebhook?url=https://54f4089072000d.lhr.domains

# # Webhook Heroku
# https://api.telegram.org/bot2045023714:AAH3Api8QrgyEd7kOnW2G1gBz3ER6a_rcyI/setWebhook?url=https://rossmann-project-telegram-bot.herokuapp.com

# # Send message
# https://api.telegram.org/bot2045023714:AAH3Api8QrgyEd7kOnW2G1gBz3ER6a_rcyI/sendMessage?chat_id=1306549820&text=Hi Victor, i am doing good, tks!

def parse_message(message):
	chat_id = message['message']['chat']['id']
	store_id = message['message']['text']

	store_id = store_id.replace('/', '')

	try:
		store_id = int(store_id)

	except ValueError:
		
		store_id = 'error'

	return chat_id, store_id

def load_dataset(store_id):
	# load test dataset
	df10 = pd.read_csv('test.csv')
	df_store_raw = pd.read_csv('store.csv')

	# merge test dataset + store dataset
	df_test = pd.merge( df10, df_store_raw, how='left', on='Store' )

	# choose store for prediction
	df_test = df_test[df_test['Store'] == store_id]

	if not df_test.empty:
		# remove closed days
		df_test = df_test[df_test['Open'] != 0]
		df_test = df_test[~df_test['Open'].isnull()]
		df_test = df_test.drop( 'Id', axis=1 )

		# convert Dataframe to json
		data = json.dumps( df_test.to_dict( orient='records' ) )

	else:
		data = 'error'

	return data

def predict(data):
	# Call API
	url = 'https://rossmann-sales-project.herokuapp.com/rossmann/predict'
	header = {'Content-type': 'application/json' }
	data = data

	# Make the request
	r = requests.post( url, data=data, headers=header )
	print('Status Code {}'.format(r.status_code))

	# convert the fetched json back to a data frame
	d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )

	return d1

def send_message(chat_id, text):
	url = f'https://api.telegram.org/bot{TOKEN}/'
	url = url + f'sendMessage?chat_id={chat_id}' 

	r = requests.post(url, json={'text': text})
	print(f'Status Code {r.status_code}')

	return None

# API initialize
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
	if request.method == 'POST':
		message = request.get_json()

		chat_id, store_id = parse_message(message)

		if store_id != 'error':
			# loading data
			data = load_dataset(store_id)

			if data != 'error':
				# prediction
				d1 = predict(data)

				# calculation
				d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()

				# send message
				msg = f"Store Number {d2['store'].values[0]} will sell R$ {d2['prediction'].values[0]:,.2f} in the next 6 weeks"

				send_message(chat_id, msg) 
				return Response('Ok', status=200)

			else:
				send_message(chat_id, 'Store Not Available')
				return Response('Ok', status=200)

		else:
			send_message(chat_id, 'Store ID is Wrong')
			return Response('Ok', status=200)

	else:
		return '<h1> Rossmann Telegram BOT </h1>'

if __name__ == '__main__':
	port = os.environ.get('PORT', 5000)
	app.run(host='0.0.0.0', port=port)