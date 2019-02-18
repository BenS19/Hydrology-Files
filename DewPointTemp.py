'''
A function for generating the dew point temp in K based on vapor pressure in 
Pa.
Author: Ben Sershen
'''
import math
def dewTemp(VaporPressure):
    print(((1/273.15)-((math.log(VaporPressure/611))/5423))**-1)

