import pymongo
import requests
client = pymongo.MongoClient('mongodb://dalton:!df420DF!@ds261088.mlab.com:61088/dalton')
db = client.dalton
collection = db.dt_sensor_data

def insert_data(data):
    r = requests.post("http://www.dalton.farm/sensors/insert_data.php", data=data)
    id = collection.insert_one(data).inserted_id
    return (id & r.status_code == 200)