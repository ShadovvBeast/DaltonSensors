import RPi.GPIO as GPIO
import time, sys
import database
import util

pin_number = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_number, GPIO.IN)

rate_cnt = 0 #Rate of counts (L/min
#tot_cnt = 0 #Total counts (total litres)
minutes = 0 #Total minutes
constant = 0.10#Convert pulses to litres
time_new = 0.0#Keep next time
#input_value = GPIO.input(pin_number)

print('Water Flow - Approximate')
#while True:
time_new = time.time()  + 60
rate_cnt = 0
while time.time() <= time_new:
    input_value = GPIO.input(pin_number) # Look for pulses
    if input_value != 0:
        rate_cnt += 1   # Pulses per time
 #       tot_cnt += 1 # Total pulses
        try:
            input_value = GPIO.input(pin_number)
            #sys.stdout.write(str(input_value)),
        except  KeyboardInterrupt: #Look for exit command
            print('\nCTRL C - Exiting nicely')
            GPIO.cleanup()
            sys.exit()

minutes += 1
value = rate_cnt * constant
print ('\nLitres / min', round(value, 4))
#print('\nTotal Litres', round(tot_cnt * constant, 4))
print('\nTime (min & clock)', minutes)
 #   raw_input("Press the <ENTER> key to continue...")

GPIO.cleanup()

if (database.insert_data({'sensor_id': 'WATERFLOW_' + util.getserial(), 'sensor_name': 'water flow 0', 'sensor_type': 'YFS201', 'value': value})):
    print('Water flow inserted successfully')



#print(input_value)
# output to pin 12
#GPIO.output(12, GPIO.HIGH)
