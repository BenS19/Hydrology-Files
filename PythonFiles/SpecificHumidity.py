'''
A function for generating a specific humidity in g/kg from a vapor pressure in
Pa and air pressure in Pa.
Author: Ben Sershen
'''
def specHum(VaporPressure,AirPressure):
    print(0.622*(VaporPressure/(AirPressure-(0.378*VaporPressure))))
