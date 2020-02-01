from ds18b20 import DS18B20
from elasticsearch import Elasticsearch
connection = Elasticsearch(["http://192.168.1.11:9200"])
# test temperature sensors
x = DS18B20()
count=x.device_count()
for i in range(0, count):
    name = 'temperature ' + str(i)
    d = {'sensor_id': x._device_file[i][-21:][:12], 'sensor_name': name, 'sensor_type': 'temperature', 'value': x.tempC(i)}
    res = connection.indices.create(index="sensors", body=d)
    if res:
        print('Temperature inserted successfully')
        print res
