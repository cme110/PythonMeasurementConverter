'''The module for processing specific types of measurement conversions.

All functions contain a list of unit classes, a list of possible input
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
    options = ['1', '2', '3']
    title = 'Temperature'
    print_units(units, title)
    new_unit = valid_unit(options)
    while new_unit not in 'Qq':
        process_conversion(units, options, title, new_unit)
        
        units = [Celsius(), Fahrenheit(), Kelvin()]
        print_units(units, title)
        new_unit = valid_unit(options)
    print()

def length():
    units = [Metres(), Kilometres(), Centimetres(), Millimetres(), Micrometres(),
             Nanometres(), Miles(), Yards(), Feet(), Inches(), NauticalMiles()]
    options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    title = 'Length'
    print_units(units, title)
    new_unit = valid_unit(options)
    while new_unit not in 'Qq':
        process_conversion(units, options, title, new_unit)

        units = [Metres(), Kilometres(), Centimetres(), Millimetres(), Micrometres(),
                 Nanometres(), Miles(), Yards(), Feet(), Inches(), NauticalMiles()]
        print_units(units, title)
        new_unit = valid_unit(options)
    print()

def mass():
    units = [Grams(), Kilograms(), Tonnes(), Milligrams(), Micrograms(),
             Ounces(), Pounds(), Stone(), ImperialTons(), USTons()]
    options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    title = 'Mass'
    print_units(units, title)
    new_unit = valid_unit(options)
    while new_unit not in 'Qq':
        process_conversion(units, options, title, new_unit)

        units = [Grams(), Kilograms(), Tonnes(), Milligrams(), Micrograms(),
                Ounces(), Pounds(), Stone(), ImperialTons(), USTons()]
        print_units(units, title)
        new_unit = valid_unit(options)
    print()

def time():
    units = [Nanoseconds(), Microseconds(), Milliseconds(), Seconds(), Minutes(),
             Hours(), Days(), Weeks(), Months(), Years(), Decades(), Centuries()]
    options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    title = 'Time'
    print_units(units, title)
    new_unit = valid_unit(options)
    while new_unit not in 'Qq':
        process_conversion(units, options, title, new_unit)

        units = [Nanoseconds(), Microseconds(), Milliseconds(), Seconds(), Minutes(),
                Hours(), Days(), Weeks(), Months(), Years(), Decades(), Centuries()]
        print_units(units, title)
        new_unit = valid_unit(options)
    print()

def speed():
    units = [MetresPerSecond(), KilometresPerHour(), FeetPerSecond(),
             MilesPerHour(), Knots()]
    options = ['1', '2', '3', '4', '5']
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
    options = ['1', '2', '3', '4', '5', '6']
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

def area():
    units = [SquareMetres(), SquareKilometres(), SquareMiles(), SquareYards(),
             SquareFeet(), SquareInches(), Hectares(), Acres()]
    options = ['1', '2', '3', '4', '5', '6', '7', '8']
    title = 'Area'
    print_units(units, title)
    new_unit = valid_unit(options)
    while new_unit not in 'Qq':
        process_conversion(units, options, title, new_unit)

        units = [SquareMetres(), SquareKilometres(), SquareMiles(), SquareYards(),
                 SquareFeet(), SquareInches(), Hectares(), Acres()]
        print_units(units, title)
        new_unit = valid_unit(options)
    print()

def pressure():
    units = [Pascals(), PoundsPerSquareInch(), Bars(), StandardAtmospheres(), Torrs()]
    options = ['1', '2', '3', '4', '5']
    title = 'Pressure'
    print_units(units, title)
    new_unit = valid_unit(options)
    while new_unit not in 'Qq':
        process_conversion(units, options, title, new_unit)

        units = [Pascals(), PoundsPerSquareInch(), Bars(), StandardAtmospheres(), Torrs()]
        print_units(units, title)
        new_unit = valid_unit(options)
    print()

def frequency():
    units = [Hertz(), Kilohertz(), Megahertz(), Gigahertz()]
    options = ['1', '2', '3', '4']
    title = 'Frequency'
    print_units(units, title)
    new_unit = valid_unit(options)
    while new_unit not in 'Qq':
        process_conversion(units, options, title, new_unit)

        units = [Hertz(), Kilohertz(), Megahertz(), Gigahertz()]
        print_units(units, title)
        new_unit = valid_unit(options)
    print()