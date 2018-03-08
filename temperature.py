from ds18b20 import DS18B20
import database

# test temperature sensors
x = DS18B20()
count=x.device_count()
for i in range(0, count):
    d = {'sensor_id': x._device_file[i][-21:][:12], 'sensor_name': 'temperature ' + str(i), 'sensor_type': 'temperature', 'value': x.tempC(i)}
    if(database.insert_data(d)):
        print('Temperature inserted successfully')
