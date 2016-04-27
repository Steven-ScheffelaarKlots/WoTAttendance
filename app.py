
from flask import Flask, send_file
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return send_file("frontEnd/templates/index.html")


@app.route("/mockrequest")
def send_request():
    payload = {'application_id': 'insert_id', 'account_id': '1005669672'}
    return requests.get('https://api.worldoftanks.com/wot/account/info/', params=payload).content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)


