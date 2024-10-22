import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['weather_db']
collection = db['weather_data']

def store_weather_data(data):
    collection.insert_one(data)

def get_stored_data():
    return list(collection.find())
