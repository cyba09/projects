import requests
import time
from pymongo import MongoClient
import certifi
import operator
from datetime import datetime


def get_items():
    CONNECTION_STRING = 'mongodb+srv://asgardt48:69605odin@cluster0.fs9xwh1.mongodb.net/?retryWrites=true&w=majority'
    

    client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

    dbname = client['law_articles']
    collection_name = dbname["Salvation_Army"]
    myDict = collection_name.find()
    sorted_list = sorted(list(myDict), key=operator.itemgetter('Timestamp'))
    lst = sorted_list[0]

    timestamp = lst['Timestamp']   #Dont forget to add utc lag!!!!!
    timestamp = datetime.strptime('10/27/2023 09:26:00', "%m/%d/%Y %H:%M:%S").timestamp()
    return [int(timestamp), lst['ID'], lst['Ammount']]

 
print(get_items())