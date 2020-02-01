from ds18b20 import DS18B20
from elasticsearch import Elasticsearch
from datetime import datetime
import time
connection = Elasticsearch(["http://192.168.1.11:9200"])
# test temperature sensors
x = DS18B20()
count=x.device_count()
while (True):
    for i in range(0, count):
        name = 'temperature ' + str(i)
        d = {'sensor_id': x._device_file[i][-21:][:12], 'sensor_name': name, 'sensor_type': 'temperature', 'value': x.tempC(i), 'timestamp': datetime.now()}
        res = connection.index(index="sensors", body=d)
        if res:
            print res
            print('Temperature inserted successfully')
    time.sleep(5)