from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import *
import time
OUTPUT=0

mcp=Adafruit_MCP230XX(busnum=1, address = 0x20, num_gpios=8)
mcp.config(4, OUTPUT)
mcp.config(1, OUTPUT)
mcp.config(2, OUTPUT)
mcp.config(3, OUTPUT)
mcp.output(4, 0)
time.sleep(1)
mcp.output(1, 0)
time.sleep(1)
mcp.output(2, 0)
time.sleep(1)
mcp.output(3, 0)

