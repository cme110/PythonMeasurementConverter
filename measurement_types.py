'''The module for processing specific types of measurement conversions.

All functions contain a list of unit classes, a string of possible input
options and a string of the type of conversion. Units are printed, and user is
asked to input a number for the corresponding unit (which is removed from units
list), or input 'Q' for quit. While input is not 'Q', conversion to new unit is
processed, units list is assigned with original units, units are printed and
user is asked to input again. Otherwise, a new line is printed.
'''

from extra_functions import valid_unit, print_units, process_conversion
from measurement_units import *

def temperature():
    units = [Celsius(), Fahrenheit(), Kelvin()]
    options = '123'
    title = 'Temperature'
    print_units(units, title)
    new_unit = valid_unit(options)
    while new_unit not in 'Qq':
        process_conversion(units, options, title, new_unit)
        
        units = [Celsius(), Fahrenheit(), Kelvin()]
        print_units(units, title)
        new_unit = valid_unit(options)
    print()

def speed():
    units = [MetresPerSecond(), KilometresPerHour(), FeetPerSecond(),
             MilesPerHour(), Knots()]
    options = '12345'
    title = 'Speed'
    print_units(units, title)
    new_unit = valid_unit(options)
    while new_unit not in 'Qq':
        process_conversion(units, options, title, new_unit)
        
        units = [MetresPerSecond(), KilometresPerHour(), FeetPerSecond(),
                 MilesPerHour(), Knots()]
        print_units(units, title)
        new_unit = valid_unit(options)
    print()

def angle():
    units = [Degrees(), Radians(), Milliradians(), Gradians(), Arcseconds(),
             Arcminutes()]
    options = '123456'
    title = 'Angle'
    print_units(units, title)
    new_unit = valid_unit(options)
    while new_unit not in 'Qq':
        process_conversion(units, options, title, new_unit)

        units = [Degrees(), Radians(), Milliradians(), Gradians(), Arcseconds(),
                 Arcminutes()]
        print_units(units, title)
        new_unit = valid_unit(options)
    print()
    
