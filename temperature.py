from ds18b20 import DS18B20
import requests
# test temperature sensors
x = DS18B20()
count=x.device_count()
for i in range(0, count):
    print(x._device_file[i][-21:][:12] + ' - ' + str(x.tempC(i)));
