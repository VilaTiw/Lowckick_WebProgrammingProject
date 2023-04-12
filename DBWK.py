from pandas import DataFrame
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for, session
import requests
from flask import request
from flask_oauthlib.client import OAuth
from json import dumps
from urllib.parse import urlencode


app = Flask(__name__)
app.secret_key = 'your secret key here'
oauth = OAuth(app)
steam_openid_url = 'https://steamcommunity.com/openid/login'



steam = oauth.remote_app(
    'steam',
    consumer_key='8386C327632B71BB13E0B9BD699E96BD',
    consumer_secret=app.secret_key,
    request_token_params={'scope': 'user:email'},
    base_url='https://api.steampowered.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://steamcommunity.com/openid/login',
    authorize_url='https://steamcommunity.com/openid/login'
)
    

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   #"mongodb+srv://UaroslavH:BV9caZNzBmBPiNYQ@csgoskinexplorer.patitvp.mongodb.net/test"
   CONNECTION_STRING = 'mongodb://azure-web-project:M73MVy790iHsITudPP4Q1xOeGjKLLeDueOKDM3h9hzZm0zmU8t1Ffc0uhTBFGQ74wz43RE8Shc6oACDbPizDQw==@azure-web-project.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azure-web-project@'
   client = MongoClient(CONNECTION_STRING)
   return client['CS_SE']

dbname=get_database()
collection_name = dbname["user_1_items"]



@app.route('/HTMLPage2_DB.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        sell_listings = request.form['sell_listings']
        sell_price_text = request.form['sell_price_text']
        sale_price_text = request.form['sale_price_text']
        type = request.form['type']
        icon_url = request.form['icon_url']

        new_item = {
            'name': name,
            'sell_listings': sell_listings,
            'sell_price_text': sell_price_text,
            'sale_price_text': sale_price_text,
            'type': type,
            'icon_url': icon_url,
        }
        

        collection_name.insert_one(new_item)

    data = collection_name.find({})
    return render_template('HTMLPage2_DB.html', data=data)


@app.route('/', methods=['GET'])
def index2():
    return render_template('HTMLPage1.html')


@app.route('/About.html', methods=['GET'])
def index3():
    return render_template('About.html')

@app.route('/login')
def login():
    return steam.authorize(callback=url_for('authorized', _external=True))

@app.route('/authorized')
def authorized():
    resp = steam.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['steam_token'] = resp['oauth_token']
    return 'You are now logged in as %s' % resp['screen_name']

@app.route("/auth")
def auth_with_steam():

  params = {
    'openid.ns': "http://specs.openid.net/auth/2.0",
    'openid.identity': "http://specs.openid.net/auth/2.0/identifier_select",
    'openid.claimed_id': "http://specs.openid.net/auth/2.0/identifier_select",
    'openid.mode': 'checkid_setup',
    'openid.return_to': 'http://127.0.0.1:5000/authorize',
    'openid.realm': 'http://127.0.0.1:5000'
  }

  query_string = urlencode(params)
  auth_url = steam_openid_url + "?" + query_string
  print(auth_url)
  return redirect(auth_url)

@app.route("/authorize")
def authorize():
  print(request.args)
  return dumps(request.args) + '<br><br><a href="http://localhost:5000/auth">Login with steam</a>'

if __name__ == "__main__":
    app.run()








if __name__ == '__main__':
    app.run(debug=True)
