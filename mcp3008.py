import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

mcp_test = mcp.read_adc(0)
ambiance = mcp.read_adc(1)
ph = mcp.read_adc(2)
humidity = mcp.read_adc(3)

print(mcp_test, ambiance, ph, humidity)