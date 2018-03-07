from ds18b20 import DS18B20
import requests
import pymongo
client = pymongo.MongoClient('mongodb://dalton:!df420DF!@ds261088.mlab.com:61088/dalton')
# test temperature sensors
x = DS18B20()
count=x.device_count()
for i in range(0, count):
    d = {'sensor_id': x._device_file[i][-21:][:12], 'sensor_name': 'temperature ' + str(i), 'sensor_type': 'temperature', 'value': x.tempC(i)}
    r = requests.post("http://www.dalton.farm/sensors/insert_data.php", data=d)
    print(r.status_code, r.reason)
    print(r.text[:300] + '...')
