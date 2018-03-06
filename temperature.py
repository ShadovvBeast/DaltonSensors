from ds18b20 import DS18B20
import requests
# test temperature sensors
x = DS18B20()
count=x.device_count()
for i in range(0, count):
    r = requests.post("http://www.dalton.farm/sensors/insert_data.php", data={'sensor_id': x._device_file[i][-21:][:12], 'sensor_name': 'temperature ' + str(i), 'sensor_type': 'temperature', 'value': x.tempC(i)})
    print(r.status_code, r.reason)
    print(r.text[:300] + '...')
