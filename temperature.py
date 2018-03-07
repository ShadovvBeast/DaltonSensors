from ds18b20 import DS18B20
import requests
import pymongo
client = pymongo.MongoClient('mongodb://dalton:!df420DF!@ds261088.mlab.com:61088/dalton')
db = client.dalton
collection = db.dt_sensor_data
# test temperature sensors
x = DS18B20()
count=x.device_count()
for i in range(0, count):
    d = {'sensor_id': x._device_file[i][-21:][:12], 'sensor_name': 'temperature ' + str(i), 'sensor_type': 'temperature', 'value': x.tempC(i)}
    r = requests.post("http://www.dalton.farm/sensors/insert_data.php", data=d)
    id = collection.insert_one(d).inserted_id
    print('Mongo id:', id)
    print(r.status_code, r.reason)
    print(r.text[:300] + '...')
