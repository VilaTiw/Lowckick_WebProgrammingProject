from pymongo import MongoClient
from pandas import DataFrame
from flask import Flask, render_template, request
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
        paint_seed = request.form['paint_seed']
        item_name = request.form['item_name']
        float_val = request.form['float']
        condition = request.form['condition']
        market_price = request.form['market_price']
        float_cap = request.form['float_cap']

        new_item = {
            'Paint_seed': paint_seed,
            'item_name': item_name,
            'Float': float_val,
            'Condition': condition,
            'Market_price': market_price,
            'Float_cap': float_cap
        }

        collection_name.insert_one(new_item)

    data = collection_name.find({})
    return render_template('HTMLPage2_DB.html', data=data)
if __name__ == '__main__':
    app.run()

