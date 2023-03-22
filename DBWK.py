from pymongo import MongoClient
from pandas import DataFrame
from pymongo_get_database import get_database
from flask import Flask, render_template, request
from pymongo_get_database import CONNECTION_STRING
from flask import request
app = Flask(__name__)
dbname = get_database()
collection_name = dbname["user_1_items"]
client = MongoClient(CONNECTION_STRING)

item_1 = {
  "Paint_seed" : "1000",
  "item_name" : "AK-47 | Redline",
  "Float" : 0.14075119793415  ,
  "Condition" : "Minimal Wear",
  "Market_price" : 2952.13 ,
  "Float_cap" : "0.1-0.7"
}

item_2 = {
  "Paint_seed" : "212",
  "item_name" : "AWP | Asiimov",
  "Float" : 0.21168099343777 ,
  "Condition" : "Field-Tested",
  "Market_price" : 5288.08 ,
  "Float_cap" : "0.018-1"
}
item_3 = {
  "Paint_seed" : "232",
  "item_name" : "USP-S | Orion",
  "Float" : 0.01807834580541 ,
  "Condition" : "Factory New",
  "Market_price" : 2125.12 ,
  "Float_cap" : "0-0.5"
}
item_4 = {
  "Paint_seed" : "120",
  "item_name" : "Shadow Daggers | Ultraviolet",
  "Float" : 0.27696374058723 ,
  "Condition" : "Field-Tested",
  "Market_price" : 3542.83 ,
  "Float_cap" : "0.06-0.8"
}
item_5 = {
  "Paint_seed" : "267",
  "item_name" : "Glock-18 | Nuclear Garden",
  "Float" : 0.08533399552107 ,
  "Condition" : "Minimal Wear",
  "Market_price" : 308.78 ,
  "Float_cap" : "0-0.7"
}
collection_name.insert_many([item_1,item_2, item_3, item_4, item_5])
#item_details = collection_name.find()
#items_df = DataFrame(item_details)
#print(items_df)
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
