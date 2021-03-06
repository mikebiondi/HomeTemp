#!/usr/bin/python

import smbus
import time

bus = smbus.SMBus(1)
data = bus.read_i2c_block_data(0x48,0)
msb = data[0]
lsb = data[1]
Celsius =  (((msb<<8)|lsb)>>4) * 0.0625   
Farenheit = Celsius * 1.8 + 32

print "%d,%d" % (Celsius,Farenheit)

