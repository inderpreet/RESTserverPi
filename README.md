Basic REST Server Implementation using Python and Flask
=======================================================
This is a simple REST server implementation using python that can access an MCP23008 using I2C on a Raspberry PI. I wrote this as a service to access GPIO on an expansion port using HTTP calls. 

## Dependencies
I wrote this for the Rapberry Pi and you need to install
* Python 2.7.x
* Flask( sudo pip install flask)

Then run python server.py and you should be good

To test things, use
curl -i localhost:5000/ and you should get a hello world reply
curl -i localhost:5000/api/output1/ON to turn on output 1 and so and so forth. Use OFF to turn it off (duh!)

I have use Adafruit's MCP230xx libraries to get things up and running so all credit on the lib to them.

-----> http://embeddedcode.wordpress.com

Designed by Inderpreet Singh Of Guru Nanak Dev Univeristy, Amritsar

This software may be distributed and modified under the terms of the GNU
General Public License version 2 (GPL2) as published by the Free Software
Foundation and appearing in the file LICENSE.TXT included in the packaging of
this file. Please note that GPL2 Section 2[b] requires that all works based
on this software must also be made publicly available under the terms of
the GPL2 ("Copyleft").

We put a lot of time and effort into our project and hence this copyright 
notice ensures that people contribute as well as each contribution is 
acknowledged. Please retain this original notice and if you make changes
please document them below along with your details.

The latest copy of this project/library can be found at: 
https://github.com/inderpreet/
