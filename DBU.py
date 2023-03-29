from pandas import DataFrame
from pymongo import MongoClient
from flask import Flask, render_template, request
import requests
from flask import request
from DBWK import get_database
import json

url = "https://steamcommunity.com/market/search/render/?query=&start=0&count=100&search_descriptions=0&appid=730&norender=1"
response = requests.get(url)
data = json.loads(response.text)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)


dbname = get_database()
collection_name = dbname["user_1_items"]
with open('data.json') as f:
    data = json.load(f)
collection_name.insert_many(data['results'])

# Додавання отриманих даних до таблиці MongoDB
"""if response.status_code == 200:
    items = response.json()['response']
    for item in items:
        collection_name.insert_one(item)
        print("Додано: ", item['name'])
else:
    print("Помилка: ", response.status_code)"""