'''
A function for generating a saturated vapor pressure from a temp in K.
Author: Ben Sershen
'''
import math
def clausClap(temp): #temp in C
    SatVapPressure = 611*math.exp(5423*((1/273.15)-(1/temp)))
    print(SatVapPressure)
