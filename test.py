import pymongo
client = pymongo.MongoClient('mongodb://dalton:!df420DF!@ds261088.mlab.com:61088/dalton')
db = client.dalton
collection = db.dt_sensor_data
id = collection.insert_one({'test':'testval'}).inserted_id
print(id)