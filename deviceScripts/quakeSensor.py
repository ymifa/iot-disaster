#!/usr/bin/python
# Only run on the raspberry pi
import smbus
import math
from dbus._dbus import Bus
 
# Power management registers
power_mgmt_1 = 0x6b
# or bus = smbus.SMBus(0) for pre-Revision 2 boards
bus = smbus.SMBus(1)
# This is the address value read via the i2cdetect command, can be changed via setup()
i2cAddress = 0x00
  
def setup(address):
    global i2cAddress
    global bus
    i2cAddress = address
    # Now wake the 6050 up as it starts in sleep mode
    bus.write_byte_data(i2cAddress, power_mgmt_1, 0)
         
def read_byte(adr):
    global i2cAddress
    global bus
    return bus.read_byte_data(i2cAddress, adr)
 
def read_word(adr):
    global i2cAddress
    global bus
    high = bus.read_byte_data(i2cAddress, adr)
    low = bus.read_byte_data(i2cAddress, adr+1)
    val = (high << 8) + low
    return val
 
def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
 
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)
 
# Main exposed routine
def sample():
    data = {}
    data['key'] = 'value'

    data['gyroX'] = read_word_2c(0x43)
    data['gyroY'] = read_word_2c(0x45)
    data['gyroZ'] = read_word_2c(0x47)

    data['gyroScaledX'] = data['gyroX'] / 131
    data['gyroScaledY'] = data['gyroY'] / 131
    data['gyroScaledZ'] = data['gyroZ'] / 131

    data['accelX'] = read_word_2c(0x3b)
    data['accelY'] = read_word_2c(0x3d)
    data['accelZ'] = read_word_2c(0x3f)
 
    data['accelScaledX'] = data['accelX'] / 16384.0
    data['accelScaledY'] = data['accelY'] / 16384.0
    data['accelScaledZ'] = data['accelZ'] / 16384.0
 
    data['rotationX'] = get_x_rotation(data['accelScaledX'], data['accelScaledY'], data['accelScaledZ'])
    data['rotationY'] = get_y_rotation(data['accelScaledX'], data['accelScaledY'], data['accelScaledZ'])
    return data

# Routine to test if input sensor data is indicative of an earthquake
def isPossibleQuake(data):
    xMotion = abs(data['gyroScaledX'])
    yMotion = abs(data['gyroScaledY'])
    zMotion = abs(data['gyroScaledZ'])
    return ((xMotion > 3) or (yMotion > 3) or (zMotion > 3))
