from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests
import os
import time
import schedule

DOMAINS = ['http://capistrano.net.br',
    'http://zetecauto.com.br',
    'http://blogueirinhastore.com',
    'http://beabaweb.com.br',
    'http://rrsegurancaltr.com.br']

app = Flask(__name__)

@app.route('/sites_status')
def sites_status():
    
    return jsonify(os.environ['VERSION'])

def check_site_availability():
    
    for domain in DOMAINS:
        response = requests.get(domain)
        if response.status_code == 200: 
            print(domain + " - OK")
        else:
            print(domain + " - " + str(response.status_code))
            telegram_bot_sendtext("o site " + domain + " está fora do ar.")

def telegram_bot_sendtext(bot_message):
    
    bot_token = os.environ['TOKEN_TELEGRAM']
    bot_chatID = os.environ['CHAT_ID_TELEGRAM']
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

schedule.every(1).minutes.do(check_site_availability)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')