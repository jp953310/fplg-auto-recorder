from time import sleep
import spidev
spi=spidev.SpiDev()
spi.open(0,0)
def readChannel(channel):
    adc=spi.xfer2([1,(8+channel)<<4,0])
    data=((adc[1]&3)<<8)+adc[2]
    return data
retI=1
def getDistance(reading):
	if reading is not 0:
		if retI:
			return int(43300*reading**(-1.236))
		else:	
			return 43300*reading**(-1.236)
	return 80
try:
    while 1:
        val = readChannel(0)
        print "----------------------------"
        print val
        print getDistance(val)
        sleep(1)
finally:
    spi.close()