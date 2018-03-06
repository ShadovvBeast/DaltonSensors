from ds18b20 import DS18B20
# test temperature sensors
x = DS18B20()
count=x.device_count()
for i in range(0, count):
    print(x._read_temp(i))#print(x.tempC(i))
