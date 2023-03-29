from pandas import DataFrame
from pymongo import MongoClient
from flask import Flask, render_template, request
import requests
from flask import request

app = Flask(__name__)
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   #"mongodb://azure-web-project:M73MVy790iHsITudPP4Q1xOeGjKLLeDueOKDM3h9hzZm0zmU8t1Ffc0uhTBFGQ74wz43RE8Shc6oACDbPizDQw%3D%3D@azure-web-project.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@azure-web-project@"
   CONNECTION_STRING = 'mongodb+srv://UaroslavH:BV9caZNzBmBPiNYQ@csgoskinexplorer.patitvp.mongodb.net/test'
   client = MongoClient(CONNECTION_STRING)
   return client['CS_SE']

dbname=get_database()
collection_name = dbname["user_1_items"]



@app.route('/', methods=['GET', 'POST'])
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
if __name__ == '__main__':
    app.run()
