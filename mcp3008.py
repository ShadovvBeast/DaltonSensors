import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import database
import util

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

mcp_test = mcp.read_adc(0)
ambience = mcp.read_adc(1)
ph = mcp.read_adc(2)
humidity = mcp.read_adc(3)

if (database.insert_data({'sensor_id': 'AMBIENCE_' + util.getserial(), 'sensor_name': 'ambience 0', 'sensor_type': 'TEMT6000', 'value': ambience})):
    print('Ambiance inserted successfully')
if(database.insert_data({'sensor_id': 'PH_' + util.getserial(), 'sensor_name': 'ph 0', 'sensor_type': 'ph', 'value': ph})):
    print('pH inserted successfully')
if (database.insert_data({'sensor_id': 'HUMIDITY_' + util.getserial(), 'sensor_name': 'humidity 0', 'sensor_type': 'HR202L', 'value': humidity})):
    print('Humidity inserted successfully')


