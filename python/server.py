#!flask/bin/python
from flask import Flask
from flask import request
import Adafruit_I2C
from Adafruit_MCP230xx import *
import time

OUTPUT=0

app = Flask(__name__)

mcp=Adafruit_MCP230XX(busnum=1, address = 0x20, num_gpios=8)
mcp.config(4, OUTPUT)
mcp.config(1, OUTPUT)
mcp.config(2, OUTPUT)
mcp.config(3, OUTPUT)
mcp.config(5, OUTPUT)
mcp.config(6, OUTPUT)
mcp.config(7, OUTPUT)

@app.route('/')
def index():
    return "REST Server! usage: localhost:5000/api/4?value=1 for turning on pin 4"

# localhost:5000/api/set?pin=4&value=1
@app.route('/api/<int:pin>', methods=['GET', 'POST'])
def set_outputs(pin):
    if(pin<7):
        value=int(request.args.get('value') )
        mcp.output(pin,value)
        return "Configuring"
    else:
        return "Error! I dont have so many pins"

if __name__ == '__main__':
    app.run(debug=True)
