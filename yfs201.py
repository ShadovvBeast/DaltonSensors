import RPi.GPIO as GPIO

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up the GPIO channels - one input and one output
GPIO.setup(11, GPIO.IN)

# input from pin 11
input_value = GPIO.input(11)

print(input_value)
# output to pin 12
#GPIO.output(12, GPIO.HIGH)
