#!/usr/bin/python

import smbus, time, sys, getopt

def usage():
	print "whatTemp.py [-a <temp in F>]"
	print
	print "Displays temperature in the house."
	print "use '-a' and a value to alert on extremely low or high values."
	

try: 
	opts, args = getopt.getopt(sys.argv[1:], "ha:", ["help", "alertTemp="])
except getopt.GetoptError as err:
	print (err)
	usage()
	sys.exeit(2)

for o, a in opts:
	if o in ("-a", "--alertTemp"):
		degrees = int(a)
	elif o in ("-h", "--help"):
		usage()
		sys.exit()
	else:
		assert False, "unhandled option"

# Fetch the temp
bus = smbus.SMBus(1)
data = bus.read_i2c_block_data(0x48,0)
msb = data[0]
lsb = data[1]
Celsius =  (((msb<<8)|lsb)>>4) * 0.0625   
Farenheit = Celsius * 1.8 + 32

localtime = time.asctime( time.localtime(time.time()) )


try:
	if ( degrees ):
		if (Farenheit < degrees):
			print "%s, %d, %d" % (localtime, Farenheit, Celsius)
except:
	print "%s, %d, %d" % (localtime, Farenheit, Celsius)
	
