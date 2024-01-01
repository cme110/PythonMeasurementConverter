'''The module containing all the classes for each measurement unit used for
converting measurements.

All classes have two attributes:
    name (str): Name of the unit
    symbol (str): Symbol of the unit

All classes have three methods:
    __init__():
        Initialises the class by assigning name and symbol attributes.

    __repr__():
        String representation of the class.
    
        Returns:
            String of capitalised name attribute
        
    conversion(old_unit, old_{measurement}):
        Chooses the conversion calculation based on the name attribute of
        the old measurement unit, then does the calculation. 
        
        Args:
            old_unit (class): Represents the old measurement unit
            old_{measurement} (int): Represents the amount of the old measurement unit

        Returns:
            new_{measurement} (float): The result of the conversion calculation
'''

import math

# Temperature Units =============================================================

class Celsius():
    def __init__(self):
        self.name = 'degrees Celsius'
        self.symbol = '°C'

    def __repr__(self):
        return self.name.title()

    def conversion(self, old_unit, old_temp):
        if old_unit.name == 'degrees Fahrenheit':
            new_temp = (old_temp - 32) * (5/9)
        else:
            new_temp = old_temp - 273.15
        return new_temp

class Fahrenheit():
    def __init__(self):
        self.name = 'degrees Fahrenheit'
        self.symbol = '°F'

    def __repr__(self):
        return self.name.title()

    def conversion(self, old_unit, old_temp):
        if old_unit.name == 'degrees Celsius':
            new_temp = (old_temp * (9/5)) + 32
        else:
            new_temp = (old_temp - 273.15) * (9/5) + 32
        return new_temp

class Kelvin():
    def __init__(self):
        self.name = 'Kelvin'
        self.symbol = 'K'

    def __repr__(self):
        return self.name

    def conversion(self, old_unit, old_temp):
        if old_unit.name == 'degrees Celsius':
            new_temp = old_temp + 273.15
        else:
            new_temp = (old_temp - 32) * (5/9) + 273.15
        return new_temp

# Length Units =================================================================

class Metres():
    def __init__(self):
        self.name = 'metres'
        self.symbol = 'm'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_length):
        if old_unit.name == 'kilometres':
            new_length = old_length * 1000
        elif old_unit.name == 'centimetres':
            new_length = old_length / 100
        elif old_unit.name == 'millimetres':
            new_length = old_length / 1000
        elif old_unit.name == 'micrometres':
            new_length = old_length / 1e6
        elif old_unit.name == 'nanometres':
            new_length = old_length / 1e9
        elif old_unit.name == 'miles':
            new_length = old_length * 1609
        elif old_unit.name == 'yards':
            new_length = old_length / 1.094
        elif old_unit.name == 'feet':
            new_length = old_length / 3.281
        elif old_unit.name == 'inches':
            new_length = old_length / 39.37
        else:
            new_length = old_length * 1852
        return new_length

class Kilometres():
    def __init__(self):
        self.name = 'kilometres'
        self.symbol = 'km'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_length):
        if old_unit.name == 'metres':
            new_length = old_length / 1000
        elif old_unit.name == 'centimetres':
            new_length = old_length / 100000
        elif old_unit.name == 'millimetres':
            new_length = old_length / 1e6
        elif old_unit.name == 'micrometres':
            new_length = old_length / 1e9
        elif old_unit.name == 'nanometres':
            new_length = old_length / 1e12
        elif old_unit.name == 'miles':
            new_length = old_length * 1.609
        elif old_unit.name == 'yards':
            new_length = old_length / 1094
        elif old_unit.name == 'feet':
            new_length = old_length / 3281
        elif old_unit.name == 'inches':
            new_length = old_length / 39370
        else:
            new_length = old_length * 1.852
        return new_length

class Centimetres():
    def __init__(self):
        self.name = 'centimetres'
        self.symbol = 'cm'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_length):
        if old_unit.name == 'metres':
            new_length = old_length * 100
        elif old_unit.name == 'kilometres':
            new_length = old_length * 100000
        elif old_unit.name == 'millimetres':
            new_length = old_length / 10
        elif old_unit.name == 'micrometres':
            new_length = old_length / 10000
        elif old_unit.name == 'nanometres':
            new_length = old_length / 1e7
        elif old_unit.name == 'miles':
            new_length = old_length * 160900
        elif old_unit.name == 'yards':
            new_length = old_length * 91.44
        elif old_unit.name == 'feet':
            new_length = old_length * 30.48
        elif old_unit.name == 'inches':
            new_length = old_length * 2.54
        else:
            new_length = old_length * 185200
        return new_length

class Millimetres():
    def __init__(self):
        self.name = 'millimetres'
        self.symbol = 'mm'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_length):
        if old_unit.name == 'metres':
            new_length = old_length * 1000
        elif old_unit.name == 'kilometres':
            new_length = old_length * 1e6
        elif old_unit.name == 'centimetres':
            new_length = old_length * 10
        elif old_unit.name == 'micrometres':
            new_length = old_length / 1000
        elif old_unit.name == 'nanometres':
            new_length = old_length / 1e6
        elif old_unit.name == 'miles':
            new_length = old_length * 1.609e6
        elif old_unit.name == 'yards':
            new_length = old_length * 914.4
        elif old_unit.name == 'feet':
            new_length = old_length * 304.8
        elif old_unit.name == 'inches':
            new_length = old_length * 25.4
        else:
            new_length = old_length * 1.852e6
        return new_length

class Micrometres():
    def __init__(self):
        self.name = 'micrometres'
        self.symbol = 'μm'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_length):
        if old_unit.name == 'metres':
            new_length = old_length * 1e6
        elif old_unit.name == 'kilometres':
            new_length = old_length * 1e9
        elif old_unit.name == 'centimetres':
            new_length = old_length * 10000
        elif old_unit.name == 'millimetres':
            new_length = old_length * 1000
        elif old_unit.name == 'nanometres':
            new_length = old_length / 1000
        elif old_unit.name == 'miles':
            new_length = old_length * 1.609e9
        elif old_unit.name == 'yards':
            new_length = old_length * 914400
        elif old_unit.name == 'feet':
            new_length = old_length * 304800
        elif old_unit.name == 'inches':
            new_length = old_length * 25400
        else:
            new_length = old_length * 1.852e9
        return new_length

class Nanometres():
    def __init__(self):
        self.name = 'nanometres'
        self.symbol = 'nm'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_length):
        if old_unit.name == 'metres':
            new_length = old_length * 1e9
        elif old_unit.name == 'kilometres':
            new_length = old_length * 1e12
        elif old_unit.name == 'centimetres':
            new_length = old_length * 1e7
        elif old_unit.name == 'millimetres':
            new_length = old_length * 1e6
        elif old_unit.name == 'micrometres':
            new_length = old_length * 1000
        elif old_unit.name == 'miles':
            new_length = old_length * 1.609e12
        elif old_unit.name == 'yards':
            new_length = old_length * 9.144e8
        elif old_unit.name == 'feet':
            new_length = old_length * 3.048e8
        elif old_unit.name == 'inches':
            new_length = old_length * 2.54e7
        else:
            new_length = old_length * 1.852e12
        return new_length

class Miles():
    def __init__(self):
        self.name = 'miles'
        self.symbol = 'mi'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_length):
        if old_unit.name == 'metres':
            new_length = old_length / 1609
        elif old_unit.name == 'kilometres':
            new_length = old_length / 1.609
        elif old_unit.name == 'centimetres':
            new_length = old_length / 160900
        elif old_unit.name == 'millimetres':
            new_length = old_length / 1.609e6
        elif old_unit.name == 'micrometres':
            new_length = old_length / 1.609e9
        elif old_unit.name == 'nanometres':
            new_length = old_length / 1.609e12
        elif old_unit.name == 'yards':
            new_length = old_length / 1760
        elif old_unit.name == 'feet':
            new_length = old_length / 5280
        elif old_unit.name == 'inches':
            new_length = old_length / 63360
        else:
            new_length = old_length * 1.151
        return new_length

class Yards():
    def __init__(self):
        self.name = 'yards'
        self.symbol = 'yd'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_length):
        if old_unit.name == 'metres':
            new_length = old_length * 1.094
        elif old_unit.name == 'kilometres':
            new_length = old_length * 1094
        elif old_unit.name == 'centimetres':
            new_length = old_length / 91.44
        elif old_unit.name == 'millimetres':
            new_length = old_length / 914.4
        elif old_unit.name == 'micrometres':
            new_length = old_length / 914400
        elif old_unit.name == 'nanometres':
            new_length = old_length / 9.144e8
        elif old_unit.name == 'miles':
            new_length = old_length * 1760
        elif old_unit.name == 'feet':
            new_length = old_length / 3
        elif old_unit.name == 'inches':
            new_length = old_length / 36
        else:
            new_length = old_length * 2025
        return new_length

class Feet():
    def __init__(self):
        self.name = 'feet'
        self.symbol = 'ft'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_length):
        if old_unit.name == 'metres':
            new_length = old_length * 3.281
        elif old_unit.name == 'kilometres':
            new_length = old_length * 3281
        elif old_unit.name == 'centimetres':
            new_length = old_length / 30.48
        elif old_unit.name == 'millimetres':
            new_length = old_length / 304.8
        elif old_unit.name == 'micrometres':
            new_length = old_length / 304800
        elif old_unit.name == 'nanometres':
            new_length = old_length / 3.048e8
        elif old_unit.name == 'miles':
            new_length = old_length * 5280
        elif old_unit.name == 'yards':
            new_length = old_length * 3
        elif old_unit.name == 'inches':
            new_length = old_length / 12
        else:
            new_length = old_length * 6076
        return new_length

class Inches():
    def __init__(self):
        self.name = 'inches'
        self.symbol = 'in'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_length):
        if old_unit.name == 'metres':
            new_length = old_length * 39.37
        elif old_unit.name == 'kilometres':
            new_length = old_length * 39370
        elif old_unit.name == 'centimetres':
            new_length = old_length / 2.54
        elif old_unit.name == 'millimetres':
            new_length = old_length / 25.4
        elif old_unit.name == 'micrometres':
            new_length = old_length / 25400
        elif old_unit.name == 'nanometres':
            new_length = old_length / 2.54e7
        elif old_unit.name == 'miles':
            new_length = old_length * 63360
        elif old_unit.name == 'yards':
            new_length = old_length * 36
        elif old_unit.name == 'feet':
            new_length = old_length * 12
        else:
            new_length = old_length * 72910
        return new_length

class NauticalMiles():
    def __init__(self):
        self.name = 'nautical miles'
        self.symbol = 'nmi'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_length):
        if old_unit.name == 'metres':
            new_length = old_length / 1852
        elif old_unit.name == 'kilometres':
            new_length = old_length / 1.852
        elif old_unit.name == 'centimetres':
            new_length = old_length / 185200
        elif old_unit.name == 'millimetres':
            new_length = old_length / 1.852e6
        elif old_unit.name == 'micrometres':
            new_length = old_length / 1.852e9
        elif old_unit.name == 'nanometres':
            new_length = old_length / 1.852e12
        elif old_unit.name == 'miles':
            new_length = old_length / 1.151
        elif old_unit.name == 'yards':
            new_length = old_length / 2025
        elif old_unit.name == 'feet':
            new_length = old_length / 6076
        else:
            new_length = old_length / 72910
        return new_length

# Mass Units ===================================================================

class Grams():
    def __init__(self):
        self.name = 'grams'
        self.symbol = 'g'
    
    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_mass):
        if old_unit.name == 'kilograms':
            new_mass = old_mass * 1000
        elif old_unit.name == 'tonnes':
            new_mass = old_mass * 1e6
        elif old_unit.name == 'milligrams':
            new_mass = old_mass / 1000
        elif old_unit.name == 'micrograms':
            new_mass = old_mass / 1e6
        elif old_unit.name == 'ounces':
            new_mass = old_mass * 28.35
        elif old_unit.name == 'pounds':
            new_mass = old_mass * 453.6
        elif old_unit.name == 'stone':
            new_mass = old_mass * 6350
        elif old_unit.name == 'imperial tons':
            new_mass = old_mass * 1.016e6
        else:
            new_mass = old_mass * 907200
        return new_mass

class Kilograms():
    def __init__(self):
        self.name = 'kilograms'
        self.symbol = 'kg'
    
    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_mass):
        if old_unit.name == 'grams':
            new_mass = old_mass / 1000
        elif old_unit.name == 'tonnes':
            new_mass = old_mass * 1000
        elif old_unit.name == 'milligrams':
            new_mass = old_mass / 1e6
        elif old_unit.name == 'micrograms':
            new_mass = old_mass / 1e9
        elif old_unit.name == 'ounces':
            new_mass = old_mass / 35.274
        elif old_unit.name == 'pounds':
            new_mass = old_mass / 2.205
        elif old_unit.name == 'stone':
            new_mass = old_mass * 6.35
        elif old_unit.name == 'imperial tons':
            new_mass = old_mass * 1016
        else:
            new_mass = old_mass * 907.2
        return new_mass

class Tonnes():
    def __init__(self):
        self.name = 'tonnes'
        self.symbol = 't'
    
    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_mass):
        if old_unit.name == 'grams':
            new_mass = old_mass / 1e6
        elif old_unit.name == 'kilograms':
            new_mass = old_mass / 1000
        elif old_unit.name == 'milligrams':
            new_mass = old_mass / 1e9
        elif old_unit.name == 'micrograms':
            new_mass = old_mass / 1e12
        elif old_unit.name == 'ounces':
            new_mass = old_mass / 35270
        elif old_unit.name == 'pounds':
            new_mass = old_mass / 2205
        elif old_unit.name == 'stone':
            new_mass = old_mass / 157.5
        elif old_unit.name == 'imperial tons':
            new_mass = old_mass * 1.016
        else:
            new_mass = old_mass / 1.102
        return new_mass

class Milligrams():
    def __init__(self):
        self.name = 'milligrams'
        self.symbol = 'mg'
    
    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_mass):
        if old_unit.name == 'grams':
            new_mass = old_mass * 1000
        elif old_unit.name == 'kilograms':
            new_mass = old_mass * 1e6
        elif old_unit.name == 'tonnes':
            new_mass = old_mass * 1e9
        elif old_unit.name == 'micrograms':
            new_mass = old_mass / 1000
        elif old_unit.name == 'ounces':
            new_mass = old_mass * 28350
        elif old_unit.name == 'pounds':
            new_mass = old_mass * 453600
        elif old_unit.name == 'stone':
            new_mass = old_mass * 6.35e6
        elif old_unit.name == 'imperial tons':
            new_mass = old_mass * 1.016e9
        else:
            new_mass = old_mass * 9.072e8
        return new_mass

class Micrograms():
    def __init__(self):
        self.name = 'micrograms'
        self.symbol = 'μg'
    
    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_mass):
        if old_unit.name == 'grams':
            new_mass = old_mass * 1e6
        elif old_unit.name == 'kilograms':
            new_mass = old_mass * 1e9
        elif old_unit.name == 'tonnes':
            new_mass = old_mass * 1e12
        elif old_unit.name == 'milligrams':
            new_mass = old_mass * 1000
        elif old_unit.name == 'ounces':
            new_mass = old_mass * 2.835e7
        elif old_unit.name == 'pounds':
            new_mass = old_mass * 4.536e8
        elif old_unit.name == 'stone':
            new_mass = old_mass * 6.35e9
        elif old_unit.name == 'imperial tons':
            new_mass = old_mass * 1.016e12
        else:
            new_mass = old_mass * 9.072e11
        return new_mass

class Ounces():
    def __init__(self):
        self.name = 'ounces'
        self.symbol = 'oz'
    
    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_mass):
        if old_unit.name == 'grams':
            new_mass = old_mass / 28.35
        elif old_unit.name == 'kilograms':
            new_mass = old_mass * 35.274
        elif old_unit.name == 'tonnes':
            new_mass = old_mass * 35270
        elif old_unit.name == 'milligrams':
            new_mass = old_mass / 28350
        elif old_unit.name == 'micrograms':
            new_mass = old_mass / 2.835e7
        elif old_unit.name == 'pounds':
            new_mass = old_mass * 16
        elif old_unit.name == 'stone':
            new_mass = old_mass * 224
        elif old_unit.name == 'imperial tons':
            new_mass = old_mass * 35840
        else:
            new_mass = old_mass * 32000
        return new_mass

class Pounds():
    def __init__(self):
        self.name = 'pounds'
        self.symbol = 'lb'
    
    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_mass):
        if old_unit.name == 'grams':
            new_mass = old_mass / 453.6
        elif old_unit.name == 'kilograms':
            new_mass = old_mass * 2.205
        elif old_unit.name == 'tonnes':
            new_mass = old_mass * 2205
        elif old_unit.name == 'milligrams':
            new_mass = old_mass / 453600
        elif old_unit.name == 'micrograms':
            new_mass = old_mass / 4.536e8
        elif old_unit.name == 'ounces':
            new_mass = old_mass / 16
        elif old_unit.name == 'stone':
            new_mass = old_mass * 14
        elif old_unit.name == 'imperial tons':
            new_mass = old_mass * 2240
        else:
            new_mass = old_mass * 2000
        return new_mass

class Stone():
    def __init__(self):
        self.name = 'stone'
        self.symbol = 'st'
    
    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_mass):
        if old_unit.name == 'grams':
            new_mass = old_mass / 6350
        elif old_unit.name == 'kilograms':
            new_mass = old_mass / 6.35
        elif old_unit.name == 'tonnes':
            new_mass = old_mass * 157.5
        elif old_unit.name == 'milligrams':
            new_mass = old_mass / 6.35e6
        elif old_unit.name == 'micrograms':
            new_mass = old_mass / 6.35e9
        elif old_unit.name == 'ounces':
            new_mass = old_mass / 224
        elif old_unit.name == 'pounds':
            new_mass = old_mass / 14
        elif old_unit.name == 'imperial tons':
            new_mass = old_mass * 160
        else:
            new_mass = old_mass * 142.9
        return new_mass

class ImperialTons():
    def __init__(self):
        self.name = 'imperial tons'
        self.symbol = 'LT'
    
    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_mass):
        if old_unit.name == 'grams':
            new_mass = old_mass / 1.016e6
        elif old_unit.name == 'kilograms':
            new_mass = old_mass / 1016
        elif old_unit.name == 'tonnes':
            new_mass = old_mass / 1.016
        elif old_unit.name == 'milligrams':
            new_mass = old_mass / 1.016e9
        elif old_unit.name == 'micrograms':
            new_mass = old_mass / 1.016e12
        elif old_unit.name == 'ounces':
            new_mass = old_mass / 35840
        elif old_unit.name == 'pounds':
            new_mass = old_mass / 2240
        elif old_unit.name == 'stone':
            new_mass = old_mass / 160
        else:
            new_mass = old_mass / 1.12
        return new_mass

class USTons():
    def __init__(self):
        self.name = 'US tons'
        self.symbol = 'tn'
    
    def __repr__(self):
        return self.name

    def conversion(self, old_unit, old_mass):
        if old_unit.name == 'grams':
            new_mass = old_mass / 907200
        elif old_unit.name == 'kilograms':
            new_mass = old_mass / 907.2
        elif old_unit.name == 'tonnes':
            new_mass = old_mass * 1.102
        elif old_unit.name == 'milligrams':
            new_mass = old_mass / 9.072e8
        elif old_unit.name == 'micrograms':
            new_mass = old_mass / 9.072e11
        elif old_unit.name == 'ounces':
            new_mass = old_mass / 32000
        elif old_unit.name == 'pounds':
            new_mass = old_mass / 2000
        elif old_unit.name == 'stone':
            new_mass = old_mass / 142.9
        else:
            new_mass = old_mass * 1.12
        return new_mass

# Time Units ===================================================================

class Nanoseconds():
    def __init__(self):
        self.name = 'nanoseconds'
        self.symbol = 'ns'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_time):
        if old_unit.name == 'microseconds':
            new_time = old_time * 1000
        elif old_unit.name == 'milliseconds':
            new_time = old_time * 1e6
        elif old_unit.name == 'seconds':
            new_time = old_time * 1e9
        elif old_unit.name == 'minutes':
            new_time = old_time * 6e10
        elif old_unit.name == 'hours':
            new_time = old_time * 3.6e12
        elif old_unit.name == 'days':
            new_time = old_time * 8.64e13
        elif old_unit.name == 'weeks':
            new_time = old_time * 6.048e14
        elif old_unit.name == 'months':
            new_time = old_time * 2.628e15
        elif old_unit.name == 'years':
            new_time = old_time * 3.154e16
        elif old_unit.name == 'decades':
            new_time = old_time * 3.154e17
        else:
            new_time = old_time * 3.154e18
        return new_time

class Microseconds():
    def __init__(self):
        self.name = 'microseconds'
        self.symbol = 'μs'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_time):
        if old_unit.name == 'nanoseconds':
            new_time = old_time / 1000
        elif old_unit.name == 'milliseconds':
            new_time = old_time * 1000
        elif old_unit.name == 'seconds':
            new_time = old_time * 1e6
        elif old_unit.name == 'minutes':
            new_time = old_time * 6e7
        elif old_unit.name == 'hours':
            new_time = old_time * 3.6e9
        elif old_unit.name == 'days':
            new_time = old_time * 8.64e10
        elif old_unit.name == 'weeks':
            new_time = old_time * 6.048e11
        elif old_unit.name == 'months':
            new_time = old_time * 2.628e12
        elif old_unit.name == 'years':
            new_time = old_time * 3.154e13
        elif old_unit.name == 'decades':
            new_time = old_time * 3.154e14
        else:
            new_time = old_time * 3.154e15
        return new_time

class Milliseconds():
    def __init__(self):
        self.name = 'milliseconds'
        self.symbol = 'ms'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_time):
        if old_unit.name == 'nanoseconds':
            new_time = old_time / 1e6
        elif old_unit.name == 'microseconds':
            new_time = old_time / 1000
        elif old_unit.name == 'seconds':
            new_time = old_time * 1000
        elif old_unit.name == 'minutes':
            new_time = old_time * 60000
        elif old_unit.name == 'hours':
            new_time = old_time * 3.6e6
        elif old_unit.name == 'days':
            new_time = old_time * 8.64e7
        elif old_unit.name == 'weeks':
            new_time = old_time * 6.048e8
        elif old_unit.name == 'months':
            new_time = old_time * 2.628e9
        elif old_unit.name == 'years':
            new_time = old_time * 3.154e10
        elif old_unit.name == 'decades':
            new_time = old_time * 3.154e11
        else:
            new_time = old_time * 3.154e12
        return new_time

class Seconds():
    def __init__(self):
        self.name = 'seconds'
        self.symbol = 's'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_time):
        if old_unit.name == 'nanoseconds':
            new_time = old_time / 1e9
        elif old_unit.name == 'microseconds':
            new_time = old_time / 1e6
        elif old_unit.name == 'milliseconds':
            new_time = old_time / 1000
        elif old_unit.name == 'minutes':
            new_time = old_time * 60
        elif old_unit.name == 'hours':
            new_time = old_time * 3600
        elif old_unit.name == 'days':
            new_time = old_time * 86400
        elif old_unit.name == 'weeks':
            new_time = old_time * 604800
        elif old_unit.name == 'months':
            new_time = old_time * 2.628e6
        elif old_unit.name == 'years':
            new_time = old_time * 3.154e7
        elif old_unit.name == 'decades':
            new_time = old_time * 3.154e8
        else:
            new_time = old_time * 3.154e9
        return new_time

class Minutes():
    def __init__(self):
        self.name = 'minutes'
        self.symbol = 'min'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_time):
        if old_unit.name == 'nanoseconds':
            new_time = old_time / 6e10
        elif old_unit.name == 'microseconds':
            new_time = old_time / 6e7
        elif old_unit.name == 'milliseconds':
            new_time = old_time / 60000
        elif old_unit.name == 'seconds':
            new_time = old_time / 60
        elif old_unit.name == 'hours':
            new_time = old_time * 60
        elif old_unit.name == 'days':
            new_time = old_time * 1440
        elif old_unit.name == 'weeks':
            new_time = old_time * 10080
        elif old_unit.name == 'months':
            new_time = old_time * 43800
        elif old_unit.name == 'years':
            new_time = old_time * 525600
        elif old_unit.name == 'decades':
            new_time = old_time * 5.256e6
        else:
            new_time = old_time * 5.256e7
        return new_time

class Hours():
    def __init__(self):
        self.name = 'hours'
        self.symbol = 'h'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_time):
        if old_unit.name == 'nanoseconds':
            new_time = old_time / 3.6e12
        elif old_unit.name == 'microseconds':
            new_time = old_time / 3.6e9
        elif old_unit.name == 'milliseconds':
            new_time = old_time / 3.6e6
        elif old_unit.name == 'seconds':
            new_time = old_time / 3600
        elif old_unit.name == 'minutes':
            new_time = old_time / 60
        elif old_unit.name == 'days':
            new_time = old_time * 24
        elif old_unit.name == 'weeks':
            new_time = old_time * 168
        elif old_unit.name == 'months':
            new_time = old_time * 730
        elif old_unit.name == 'years':
            new_time = old_time * 8760
        elif old_unit.name == 'decades':
            new_time = old_time * 87600
        else:
            new_time = old_time * 876000
        return new_time

class Days():
    def __init__(self):
        self.name = 'days'
        self.symbol = 'd'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_time):
        if old_unit.name == 'nanoseconds':
            new_time = old_time / 8.64e13
        elif old_unit.name == 'microseconds':
            new_time = old_time / 8.64e10
        elif old_unit.name == 'milliseconds':
            new_time = old_time / 8.64e7
        elif old_unit.name == 'seconds':
            new_time = old_time / 86400
        elif old_unit.name == 'minutes':
            new_time = old_time / 1440
        elif old_unit.name == 'hours':
            new_time = old_time / 24
        elif old_unit.name == 'weeks':
            new_time = old_time * 7
        elif old_unit.name == 'months':
            new_time = old_time * 30.417
        elif old_unit.name == 'years':
            new_time = old_time * 365
        elif old_unit.name == 'decades':
            new_time = old_time * 3650
        else:
            new_time = old_time * 36500
        return new_time

class Weeks():
    def __init__(self):
        self.name = 'weeks'
        self.symbol = 'wk'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_time):
        if old_unit.name == 'nanoseconds':
            new_time = old_time / 6.048e14
        elif old_unit.name == 'microseconds':
            new_time = old_time / 6.048e11
        elif old_unit.name == 'milliseconds':
            new_time = old_time / 6.048e8
        elif old_unit.name == 'seconds':
            new_time = old_time / 604800
        elif old_unit.name == 'minutes':
            new_time = old_time / 10080
        elif old_unit.name == 'hours':
            new_time = old_time / 168
        elif old_unit.name == 'days':
            new_time = old_time / 7
        elif old_unit.name == 'months':
            new_time = old_time * 4.345
        elif old_unit.name == 'years':
            new_time = old_time * 52.143
        elif old_unit.name == 'decades':
            new_time = old_time * 521.4
        else:
            new_time = old_time * 5214
        return new_time

class Months():
    def __init__(self):
        self.name = 'months'
        self.symbol = 'mo'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_time):
        if old_unit.name == 'nanoseconds':
            new_time = old_time / 2.628e15
        elif old_unit.name == 'microseconds':
            new_time = old_time / 2.628e12
        elif old_unit.name == 'milliseconds':
            new_time = old_time / 2.628e9
        elif old_unit.name == 'seconds':
            new_time = old_time / 2.628e6
        elif old_unit.name == 'minutes':
            new_time = old_time / 43800
        elif old_unit.name == 'hours':
            new_time = old_time / 730
        elif old_unit.name == 'days':
            new_time = old_time / 30.417
        elif old_unit.name == 'weeks':
            new_time = old_time / 4.345
        elif old_unit.name == 'years':
            new_time = old_time * 12
        elif old_unit.name == 'decades':
            new_time = old_time * 120
        else:
            new_time = old_time * 1200
        return new_time

class Years():
    def __init__(self):
        self.name = 'years'
        self.symbol = 'yr'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_time):
        if old_unit.name == 'nanoseconds':
            new_time = old_time / 3.154e16
        elif old_unit.name == 'microseconds':
            new_time = old_time / 3.154e13
        elif old_unit.name == 'milliseconds':
            new_time = old_time / 3.154e10
        elif old_unit.name == 'seconds':
            new_time = old_time / 3.154e7
        elif old_unit.name == 'minutes':
            new_time = old_time / 525600
        elif old_unit.name == 'hours':
            new_time = old_time / 8760
        elif old_unit.name == 'days':
            new_time = old_time / 365
        elif old_unit.name == 'weeks':
            new_time = old_time / 52.143
        elif old_unit.name == 'months':
            new_time = old_time / 12
        elif old_unit.name == 'decades':
            new_time = old_time * 10
        else:
            new_time = old_time * 100
        return new_time

class Decades():
    def __init__(self):
        self.name = 'decades'
        self.symbol = 'dec'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_time):
        if old_unit.name == 'nanoseconds':
            new_time = old_time / 3.154e17
        elif old_unit.name == 'microseconds':
            new_time = old_time / 3.154e14
        elif old_unit.name == 'milliseconds':
            new_time = old_time / 3.154e11
        elif old_unit.name == 'seconds':
            new_time = old_time / 3.154e8
        elif old_unit.name == 'minutes':
            new_time = old_time / 5.256e6
        elif old_unit.name == 'hours':
            new_time = old_time / 87600
        elif old_unit.name == 'days':
            new_time = old_time / 3650
        elif old_unit.name == 'weeks':
            new_time = old_time / 521.4
        elif old_unit.name == 'months':
            new_time = old_time / 120
        elif old_unit.name == 'years':
            new_time = old_time / 10
        else:
            new_time = old_time * 10
        return new_time

class Centuries():
    def __init__(self):
        self.name = 'centuries'
        self.symbol = 'c'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_time):
        if old_unit.name == 'nanoseconds':
            new_time = old_time / 3.154e18
        elif old_unit.name == 'microseconds':
            new_time = old_time / 3.154e15
        elif old_unit.name == 'milliseconds':
            new_time = old_time / 3.154e12
        elif old_unit.name == 'seconds':
            new_time = old_time / 3.154e9
        elif old_unit.name == 'minutes':
            new_time = old_time / 5.256e7
        elif old_unit.name == 'hours':
            new_time = old_time / 876000
        elif old_unit.name == 'days':
            new_time = old_time / 36500
        elif old_unit.name == 'weeks':
            new_time = old_time / 5214
        elif old_unit.name == 'months':
            new_time = old_time / 1200
        elif old_unit.name == 'years':
            new_time = old_time / 100
        else:
            new_time = old_time / 10
        return new_time

# Speed Units ===================================================================

class MetresPerSecond():
    def __init__(self):
        self.name = 'metres per second'
        self.symbol = 'm/s'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_speed):
        if old_unit.name == 'kilometres per hour':
            new_speed = old_speed / 3.6
        elif old_unit.name == 'feet per second':
            new_speed = old_speed / 3.281
        elif old_unit.name == 'miles per hour':
            new_speed = old_speed / 2.237
        else:
            new_speed = old_speed / 1.944
        return new_speed

class KilometresPerHour():
    def __init__(self):
        self.name = 'kilometres per hour'
        self.symbol = 'km/h'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_speed):
        if old_unit.name == 'metres per second':
            new_speed = old_speed * 3.6
        elif old_unit.name == 'feet per second':
            new_speed = old_speed * 1.097
        elif old_unit.name == 'miles per hour':
            new_speed = old_speed * 1.609
        else:
            new_speed = old_speed * 1.852
        return new_speed

class FeetPerSecond():
    def __init__(self):
        self.name = 'feet per second'
        self.symbol = 'ft/s'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_speed):
        if old_unit.name == 'metres per second':
            new_speed = old_speed * 3.281
        elif old_unit.name == 'kilometres per hour':
            new_speed = old_speed / 1.097
        elif old_unit.name == 'miles per hour':
            new_speed = old_speed * 1.467
        else:
            new_speed = old_speed * 1.688
        return new_speed

class MilesPerHour():
    def __init__(self):
        self.name = 'miles per hour'
        self.symbol = 'mph'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_speed):
        if old_unit.name == 'metres per second':
            new_speed = old_speed * 2.237
        elif old_unit.name == 'kilometres per hour':
            new_speed = old_speed / 1.609
        elif old_unit.name == 'feet per second':
            new_speed = old_speed / 1.467
        else:
            new_speed = old_speed * 1.151
        return new_speed

class Knots():
    def __init__(self):
        self.name = 'knots'
        self.symbol = ' knots'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_speed):
        if old_unit.name == 'metres per second':
            new_speed = old_speed * 1.944
        elif old_unit.name == 'kilometres per hour':
            new_speed = old_speed / 1.852
        elif old_unit.name == 'feet per second':
            new_speed = old_speed / 1.688
        else:
            new_speed = old_speed / 1.151
        return new_speed

# Angle Units ===================================================================

class Degrees():
    def __init__(self):
        self.name = 'degrees'
        self.symbol = '°'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_angle):
        if old_unit.name == 'radians':
            new_angle = old_angle * (180/math.pi)
        elif old_unit.name == 'milliradians':
            new_angle = old_angle * (180/(1000 * math.pi))
        elif old_unit.name == 'gradians':
            new_angle = old_angle * (180/200)
        elif old_unit.name == 'arcseconds':
            new_angle = old_angle / 3600
        else:
            new_angle = old_angle / 60
        return new_angle

class Radians():
    def __init__(self):
        self.name = 'radians'
        self.symbol = ' rad'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_angle):
        if old_unit.name == 'degrees':
            new_angle = old_angle * (math.pi/180)
        elif old_unit.name == 'milliradians':
            new_angle = old_angle / 1000
        elif old_unit.name == 'gradians':
            new_angle = old_angle * (math.pi/200)
        elif old_unit.name == 'arcseconds':
            new_angle = old_angle * (math.pi/(180 * 3600))
        else:
            new_angle = old_angle * (math.pi/(60 * 180))
        return new_angle

class Milliradians():
    def __init__(self):
        self.name = 'milliradians'
        self.symbol = ' mrad'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_angle):
        if old_unit.name == 'degrees':
            new_angle = old_angle * ((1000 * math.pi)/180)
        elif old_unit.name == 'radians':
            new_angle = old_angle * 1000
        elif old_unit.name == 'gradians':
            new_angle = old_angle * ((1000 * math.pi)/200)
        elif old_unit.name == 'arcseconds':
            new_angle = old_angle * ((1000 * math.pi)/(180 * 3600))
        else:
            new_angle = old_angle * ((1000 * math.pi)/(60 * 180))
        return new_angle

class Gradians():
    def __init__(self):
        self.name = 'gradians'
        self.symbol = ' gon'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_angle):
        if old_unit.name == 'degrees':
            new_angle = old_angle * (200/180)
        elif old_unit.name == 'radians':
            new_angle = old_angle * (200/math.pi)
        elif old_unit.name == 'milliradians':
            new_angle = old_angle * (200/(1000 * math.pi))
        elif old_unit.name == 'arcseconds':
            new_angle = old_angle / 3240
        else:
            new_angle = old_angle / 54
        return new_angle

class Arcseconds():
    def __init__(self):
        self.name = 'arcseconds'
        self.symbol = '"'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_angle):
        if old_unit.name == 'degrees':
            new_angle = old_angle * 3600
        elif old_unit.name == 'radians':
            new_angle = old_angle * ((3600 * 180)/math.pi)
        elif old_unit.name == 'milliradians':
            new_angle = old_angle * ((3600 * 180)/(1000 * math.pi))
        elif old_unit.name == 'gradians':
            new_angle = old_angle * 3240
        else:
            new_angle = old_angle * 60
        return new_angle

class Arcminutes():
    def __init__(self):
        self.name = 'arcminutes'
        self.symbol = "'"

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_angle):
        if old_unit.name == 'degrees':
            new_angle = old_angle * 60
        elif old_unit.name == 'radians':
            new_angle = old_angle * ((60 * 180)/math.pi)
        elif old_unit.name == 'milliradians':
            new_angle = old_angle * ((60 * 180)/(1000 * math.pi))
        elif old_unit.name == 'gradians':
            new_angle = old_angle * 54
        else:
            new_angle = old_angle / 60
        return new_angle

# Area Units ===================================================================

class SquareMetres():
    def __init__(self):
        self.name = 'square metres'
        self.symbol = 'm²'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_area):
        if old_unit.name == 'square kilometres':
            new_area = old_area * 1e6
        elif old_unit.name == 'square miles':
            new_area = old_area * 2.59e6
        elif old_unit.name == 'square yards':
            new_area = old_area / 1.196
        elif old_unit.name == 'square feet':
            new_area = old_area / 10.764
        elif old_unit.name == 'square inches':
            new_area = old_area / 1550
        elif old_unit.name == 'hectares':
            new_area = old_area * 10000
        else:
            new_area = old_area * 4047
        return new_area

class SquareKilometres():
    def __init__(self):
        self.name = 'square kilometres'
        self.symbol = 'km²'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_area):
        if old_unit.name == 'square metres':
            new_area = old_area / 1e6
        elif old_unit.name == 'square miles':
            new_area = old_area * 2.59
        elif old_unit.name == 'square yards':
            new_area = old_area / 1.196e6
        elif old_unit.name == 'square feet':
            new_area = old_area / 1.076e7
        elif old_unit.name == 'square inches':
            new_area = old_area / 1.55e9
        elif old_unit.name == 'hectares':
            new_area = old_area / 100
        else:
            new_area = old_area / 247.1
        return new_area

class SquareMiles():
    def __init__(self):
        self.name = 'square miles'
        self.symbol = 'mi²'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_area):
        if old_unit.name == 'square metres':
            new_area = old_area / 2.59e6
        elif old_unit.name == 'square kilometres':
            new_area = old_area / 2.59
        elif old_unit.name == 'square yards':
            new_area = old_area / 3.098e6
        elif old_unit.name == 'square feet':
            new_area = old_area / 2.788e7
        elif old_unit.name == 'square inches':
            new_area = old_area / 4.014e9
        elif old_unit.name == 'hectares':
            new_area = old_area / 259
        else:
            new_area = old_area / 640
        return new_area

class SquareYards():
    def __init__(self):
        self.name = 'square yards'
        self.symbol = 'yd²'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_area):
        if old_unit.name == 'square metres':
            new_area = old_area * 1.196
        elif old_unit.name == 'square kilometres':
            new_area = old_area * 1.196e6
        elif old_unit.name == 'square miles':
            new_area = old_area * 3.098e6
        elif old_unit.name == 'square feet':
            new_area = old_area / 9
        elif old_unit.name == 'square inches':
            new_area = old_area / 1296
        elif old_unit.name == 'hectares':
            new_area = old_area * 11960
        else:
            new_area = old_area * 4840
        return new_area

class SquareFeet():
    def __init__(self):
        self.name = 'square feet'
        self.symbol = 'ft²'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_area):
        if old_unit.name == 'square metres':
            new_area = old_area * 10.764
        elif old_unit.name == 'square kilometres':
            new_area = old_area * 1.076e7
        elif old_unit.name == 'square miles':
            new_area = old_area * 2.788e7
        elif old_unit.name == 'square yards':
            new_area = old_area * 9
        elif old_unit.name == 'square inches':
            new_area = old_area / 144
        elif old_unit.name == 'hectares':
            new_area = old_area * 107600
        else:
            new_area = old_area * 43560
        return new_area

class SquareInches():
    def __init__(self):
        self.name = 'square inches'
        self.symbol = 'in²'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_area):
        if old_unit.name == 'square metres':
            new_area = old_area * 1550
        elif old_unit.name == 'square kilometres':
            new_area = old_area * 1.55e9
        elif old_unit.name == 'square miles':
            new_area = old_area * 4.014e9
        elif old_unit.name == 'square yards':
            new_area = old_area * 1296
        elif old_unit.name == 'square feet':
            new_area = old_area * 144
        elif old_unit.name == 'hectares':
            new_area = old_area * 1.55e7
        else:
            new_area = old_area * 6.273e6
        return new_area

class Hectares():
    def __init__(self):
        self.name = 'hectares'
        self.symbol = ' ha'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_area):
        if old_unit.name == 'square metres':
            new_area = old_area / 10000
        elif old_unit.name == 'square kilometres':
            new_area = old_area * 100
        elif old_unit.name == 'square miles':
            new_area = old_area * 259
        elif old_unit.name == 'square yards':
            new_area = old_area / 11960
        elif old_unit.name == 'square feet':
            new_area = old_area / 107600
        elif old_unit.name == 'square inches':
            new_area = old_area / 1.55e7
        else:
            new_area = old_area / 2.471
        return new_area

class Acres():
    def __init__(self):
        self.name = 'acres'
        self.symbol = ' ac'

    def __repr__(self):
        return self.name.capitalize()

    def conversion(self, old_unit, old_area):
        if old_unit.name == 'square metres':
            new_area = old_area / 4047
        elif old_unit.name == 'square kilometres':
            new_area = old_area * 247.1
        elif old_unit.name == 'square miles':
            new_area = old_area * 640
        elif old_unit.name == 'square yards':
            new_area = old_area / 4840
        elif old_unit.name == 'square feet':
            new_area = old_area / 43560
        elif old_unit.name == 'square inches':
            new_area = old_area / 6.273e6
        else:
            new_area = old_area * 2.471
        return new_area

# Digital Storage ===================================================================

class Bits():
    def __init__(self):
        self.name = 'bits'
        self.symbol = 'b'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_digi):
        if old_unit.name == 'bytes':
            new_digi = old_digi * 8
        elif old_unit.name == 'kilobytes':
            new_digi = old_digi * 8000
        elif old_unit.name == 'megabytes':
            new_digi = old_digi * 8e6
        elif old_unit.name == 'gigabytes':
            new_digi = old_digi * 8e9
        elif old_unit.name == 'terabytes':
            new_digi = old_digi * 8e12
        elif old_unit.name == 'petabytes':
            new_digi = old_digi * 8e15
        elif old_unit.name == 'kibibytes':
            new_digi = old_digi * 8192
        elif old_unit.name == 'mebibytes':
            new_digi = old_digi * 8.389e6
        elif old_unit.name == 'gibibytes':
            new_digi = old_digi * 8.59e9
        elif old_unit.name == 'tebibytes':
            new_digi = old_digi * 8.796e12
        else:
            new_digi = old_digi * 9.007e15
        return new_digi

class Bytes():
    def __init__(self):
        self.name = 'bytes'
        self.symbol = 'B'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_digi):
        if old_unit.name == 'bits':
            new_digi = old_digi / 8
        elif old_unit.name == 'kilobytes':
            new_digi = old_digi * 1000
        elif old_unit.name == 'megabytes':
            new_digi = old_digi * 1e6
        elif old_unit.name == 'gigabytes':
            new_digi = old_digi * 1e9
        elif old_unit.name == 'terabytes':
            new_digi = old_digi * 1e12
        elif old_unit.name == 'petabytes':
            new_digi = old_digi * 1e15
        elif old_unit.name == 'kibibytes':
            new_digi = old_digi * 1024
        elif old_unit.name == 'mebibytes':
            new_digi = old_digi * 1.049e6
        elif old_unit.name == 'gibibytes':
            new_digi = old_digi * 1.074e9
        elif old_unit.name == 'tebibytes':
            new_digi = old_digi * 1.1e12
        else:
            new_digi = old_digi * 1.126e15
        return new_digi

class Kilobytes():
    def __init__(self):
        self.name = 'kilobytes'
        self.symbol = 'KB'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_digi):
        if old_unit.name == 'bits':
            new_digi = old_digi / 8000
        elif old_unit.name == 'bytes':
            new_digi = old_digi / 1000
        elif old_unit.name == 'megabytes':
            new_digi = old_digi * 1000
        elif old_unit.name == 'gigabytes':
            new_digi = old_digi * 1e6
        elif old_unit.name == 'terabytes':
            new_digi = old_digi * 1e9
        elif old_unit.name == 'petabytes':
            new_digi = old_digi * 1e12
        elif old_unit.name == 'kibibytes':
            new_digi = old_digi * 1.024
        elif old_unit.name == 'mebibytes':
            new_digi = old_digi * 1048.58
        elif old_unit.name == 'gibibytes':
            new_digi = old_digi * 1.074e6
        elif old_unit.name == 'tebibytes':
            new_digi = old_digi * 1.1e9
        else:
            new_digi = old_digi * 1.126e12
        return new_digi

class Megabytes():
    def __init__(self):
        self.name = 'megabytes'
        self.symbol = 'MB'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_digi):
        if old_unit.name == 'bits':
            new_digi = old_digi / 8e6
        elif old_unit.name == 'bytes':
            new_digi = old_digi / 1e6
        elif old_unit.name == 'kilobytes':
            new_digi = old_digi / 1000
        elif old_unit.name == 'gigabytes':
            new_digi = old_digi * 1000
        elif old_unit.name == 'terabytes':
            new_digi = old_digi * 1e6
        elif old_unit.name == 'petabytes':
            new_digi = old_digi * 1e9
        elif old_unit.name == 'kibibytes':
            new_digi = old_digi / 976.6
        elif old_unit.name == 'mebibytes':
            new_digi = old_digi * 1.049
        elif old_unit.name == 'gibibytes':
            new_digi = old_digi * 1074
        elif old_unit.name == 'tebibytes':
            new_digi = old_digi * 1.1e6
        else:
            new_digi = old_digi * 1.126e9
        return new_digi

class Gigabytes():
    def __init__(self):
        self.name = 'gigabytes'
        self.symbol = 'GB'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_digi):
        if old_unit.name == 'bits':
            new_digi = old_digi / 8e9
        elif old_unit.name == 'bytes':
            new_digi = old_digi / 1e9
        elif old_unit.name == 'kilobytes':
            new_digi = old_digi / 1e6
        elif old_unit.name == 'megabytes':
            new_digi = old_digi / 1000
        elif old_unit.name == 'terabytes':
            new_digi = old_digi * 1000
        elif old_unit.name == 'petabytes':
            new_digi = old_digi * 1e6
        elif old_unit.name == 'kibibytes':
            new_digi = old_digi / 976600
        elif old_unit.name == 'mebibytes':
            new_digi = old_digi / 953.7
        elif old_unit.name == 'gibibytes':
            new_digi = old_digi * 1.074
        elif old_unit.name == 'tebibytes':
            new_digi = old_digi * 1100
        else:
            new_digi = old_digi * 1.126e6
        return new_digi

class Terabytes():
    def __init__(self):
        self.name = 'terabytes'
        self.symbol = 'TB'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_digi):
        if old_unit.name == 'bits':
            new_digi = old_digi / 8e12
        elif old_unit.name == 'bytes':
            new_digi = old_digi / 1e12
        elif old_unit.name == 'kilobytes':
            new_digi = old_digi / 1e9
        elif old_unit.name == 'megabytes':
            new_digi = old_digi / 1e6
        elif old_unit.name == 'gigabytes':
            new_digi = old_digi / 1000
        elif old_unit.name == 'petabytes':
            new_digi = old_digi * 1000
        elif old_unit.name == 'kibibytes':
            new_digi = old_digi / 9.766e8
        elif old_unit.name == 'mebibytes':
            new_digi = old_digi / 953700
        elif old_unit.name == 'gibibytes':
            new_digi = old_digi / 931.3
        elif old_unit.name == 'tebibytes':
            new_digi = old_digi * 1.1
        else:
            new_digi = old_digi * 1126
        return new_digi

class Petabytes():
    def __init__(self):
        self.name = 'petabytes'
        self.symbol = 'PB'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_digi):
        if old_unit.name == 'bits':
            new_digi = old_digi / 8e15
        elif old_unit.name == 'bytes':
            new_digi = old_digi / 1e15
        elif old_unit.name == 'kilobytes':
            new_digi = old_digi / 1e12
        elif old_unit.name == 'megabytes':
            new_digi = old_digi / 1e9
        elif old_unit.name == 'gigabytes':
            new_digi = old_digi / 1e6
        elif old_unit.name == 'terabytes':
            new_digi = old_digi / 1000
        elif old_unit.name == 'kibibytes':
            new_digi = old_digi / 9.766e11
        elif old_unit.name == 'mebibytes':
            new_digi = old_digi / 9.537e8
        elif old_unit.name == 'gibibytes':
            new_digi = old_digi / 931300
        elif old_unit.name == 'tebibytes':
            new_digi = old_digi / 909.5
        else:
            new_digi = old_digi * 1.126
        return new_digi

class Kibibytes():
    def __init__(self):
        self.name = 'kibibytes'
        self.symbol = 'KiB'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_digi):
        if old_unit.name == 'bits':
            new_digi = old_digi / 8192
        elif old_unit.name == 'bytes':
            new_digi = old_digi / 1024
        elif old_unit.name == 'kilobytes':
            new_digi = old_digi / 1.024
        elif old_unit.name == 'megabytes':
            new_digi = old_digi * 976.6
        elif old_unit.name == 'gigabytes':
            new_digi = old_digi * 976600
        elif old_unit.name == 'terabytes':
            new_digi = old_digi * 9.766e8
        elif old_unit.name == 'petabytes':
            new_digi = old_digi * 9.766e11
        elif old_unit.name == 'mebibytes':
            new_digi = old_digi * 1024
        elif old_unit.name == 'gibibytes':
            new_digi = old_digi * 1.049e6
        elif old_unit.name == 'tebibytes':
            new_digi = old_digi * 1.074e9
        else:
            new_digi = old_digi * 1.1e12
        return new_digi

class Mebibytes():
    def __init__(self):
        self.name = 'mebibytes'
        self.symbol = 'MiB'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_digi):
        if old_unit.name == 'bits':
            new_digi = old_digi / 8.389e6
        elif old_unit.name == 'bytes':
            new_digi = old_digi / 1.049e6
        elif old_unit.name == 'kilobytes':
            new_digi = old_digi / 1049
        elif old_unit.name == 'megabytes':
            new_digi = old_digi / 1.049
        elif old_unit.name == 'gigabytes':
            new_digi = old_digi * 953.7
        elif old_unit.name == 'terabytes':
            new_digi = old_digi * 953700
        elif old_unit.name == 'petabytes':
            new_digi = old_digi * 9.537e8
        elif old_unit.name == 'kibibytes':
            new_digi = old_digi / 1024
        elif old_unit.name == 'gibibytes':
            new_digi = old_digi * 1024
        elif old_unit.name == 'tebibytes':
            new_digi = old_digi * 1.049e6
        else:
            new_digi = old_digi * 1.074e9
        return new_digi

class Gibibytes():
    def __init__(self):
        self.name = 'gibibytes'
        self.symbol = 'GiB'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_digi):
        if old_unit.name == 'bits':
            new_digi = old_digi / 8.59e9
        elif old_unit.name == 'bytes':
            new_digi = old_digi / 1.074e9
        elif old_unit.name == 'kilobytes':
            new_digi = old_digi / 1.074e6
        elif old_unit.name == 'megabytes':
            new_digi = old_digi / 1074
        elif old_unit.name == 'gigabytes':
            new_digi = old_digi / 1.074
        elif old_unit.name == 'terabytes':
            new_digi = old_digi * 931.3
        elif old_unit.name == 'petabytes':
            new_digi = old_digi * 931300
        elif old_unit.name == 'kibibytes':
            new_digi = old_digi / 1.049e6
        elif old_unit.name == 'mebibytes':
            new_digi = old_digi / 1024
        elif old_unit.name == 'tebibytes':
            new_digi = old_digi * 1024
        else:
            new_digi = old_digi * 1.049e6
        return new_digi

class Tebibytes():
    def __init__(self):
        self.name = 'tebibytes'
        self.symbol = 'TiB'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_digi):
        if old_unit.name == 'bits':
            new_digi = old_digi / 8.796e12
        elif old_unit.name == 'bytes':
            new_digi = old_digi / 1.1e12
        elif old_unit.name == 'kilobytes':
            new_digi = old_digi / 1.1e9
        elif old_unit.name == 'megabytes':
            new_digi = old_digi / 1.1e6
        elif old_unit.name == 'gigabytes':
            new_digi = old_digi / 1100
        elif old_unit.name == 'terabytes':
            new_digi = old_digi / 1.1
        elif old_unit.name == 'petabytes':
            new_digi = old_digi * 909.5
        elif old_unit.name == 'kibibytes':
            new_digi = old_digi / 1.074e9
        elif old_unit.name == 'mebibytes':
            new_digi = old_digi / 1.049e6
        elif old_unit.name == 'gibibytes':
            new_digi = old_digi / 1024
        else:
            new_digi = old_digi * 1024
        return new_digi

class Pebibytes():
    def __init__(self):
        self.name = 'pebibytes'
        self.symbol = 'PiB'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_digi):
        if old_unit.name == 'bits':
            new_digi = old_digi / 9.007e15
        elif old_unit.name == 'bytes':
            new_digi = old_digi / 1.126e15
        elif old_unit.name == 'kilobytes':
            new_digi = old_digi / 1.126e12
        elif old_unit.name == 'megabytes':
            new_digi = old_digi / 1.126e9
        elif old_unit.name == 'gigabytes':
            new_digi = old_digi / 1.126e6
        elif old_unit.name == 'terabytes':
            new_digi = old_digi / 1126
        elif old_unit.name == 'petabytes':
            new_digi = old_digi / 1.126
        elif old_unit.name == 'kibibytes':
            new_digi = old_digi / 1.1e12
        elif old_unit.name == 'mebibytes':
            new_digi = old_digi / 1.074e9
        elif old_unit.name == 'gibibytes':
            new_digi = old_digi / 1.049e6
        else:
            new_digi = old_digi / 1024
        return new_digi

# Pressure Units ===================================================================
    
class Pascals():
    def __init__(self):
        self.name = 'pascals'
        self.symbol = 'Pa'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_pressure):
        if old_unit.name == 'pounds per square inch':
            new_pressure = old_pressure * 6895
        elif old_unit.name == 'bars':
            new_pressure = old_pressure * 100000
        elif old_unit.name == 'standard atmospheres':
            new_pressure = old_pressure * 101300
        else:
            new_pressure = old_pressure * 133.3
        return new_pressure

class PoundsPerSquareInch():
    def __init__(self):
        self.name = 'pounds per square inch'
        self.symbol = 'psi'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_pressure):
        if old_unit.name == 'pascals':
            new_pressure = old_pressure / 6895
        elif old_unit.name == 'bars':
            new_pressure = old_pressure * 14.504
        elif old_unit.name == 'standard atmospheres':
            new_pressure = old_pressure * 14.696
        else:
            new_pressure = old_pressure / 51.715
        return new_pressure

class Bars():
    def __init__(self):
        self.name = 'bars'
        self.symbol = ' bar'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_pressure):
        if old_unit.name == 'pascals':
            new_pressure = old_pressure / 100000
        elif old_unit.name == 'pounds per square inch':
            new_pressure = old_pressure / 14.504
        elif old_unit.name == 'standard atmospheres':
            new_pressure = old_pressure * 1.013
        else:
            new_pressure = old_pressure / 750.1
        return new_pressure

class StandardAtmospheres():
    def __init__(self):
        self.name = 'standard atmospheres'
        self.symbol = 'atm'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_pressure):
        if old_unit.name == 'pascals':
            new_pressure = old_pressure / 101300
        elif old_unit.name == 'pounds per square inch':
            new_pressure = old_pressure / 14.696
        elif old_unit.name == 'bars':
            new_pressure = old_pressure / 1.013
        else:
            new_pressure = old_pressure / 760
        return new_pressure

class Torrs():
    def __init__(self):
        self.name = 'torrs'
        self.symbol = ' Torr'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_pressure):
        if old_unit.name == 'pascals':
            new_pressure = old_pressure / 133.3
        elif old_unit.name == 'pounds per square inch':
            new_pressure = old_pressure * 51.715
        elif old_unit.name == 'bars':
            new_pressure = old_pressure * 750.1
        else:
            new_pressure = old_pressure * 760
        return new_pressure
    
# Frequency Units ===================================================================

class Hertz():
    def __init__(self):
        self.name = 'hertz'
        self.symbol = 'Hz'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_freq):
        if old_unit.name == 'kilohertz':
            new_freq = old_freq * 1000
        elif old_unit.name == 'megahertz':
            new_freq = old_freq * 1e6
        else:
            new_freq = old_freq * 1e9
        return new_freq

class Kilohertz():
    def __init__(self):
        self.name = 'kilohertz'
        self.symbol = 'kHz'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_freq):
        if old_unit.name == 'hertz':
            new_freq = old_freq / 1000
        elif old_unit.name == 'megahertz':
            new_freq = old_freq * 1000
        else:
            new_freq = old_freq * 1e6
        return new_freq

class Megahertz():
    def __init__(self):
        self.name = 'megahertz'
        self.symbol = 'MHz'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_freq):
        if old_unit.name == 'hertz':
            new_freq = old_freq / 1e6
        elif old_unit.name == 'kilohertz':
            new_freq = old_freq / 1000
        else:
            new_freq = old_freq * 1000
        return new_freq

class Gigahertz():
    def __init__(self):
        self.name = 'gigahertz'
        self.symbol = 'GHz'
    
    def __repr__(self):
        return self.name.capitalize()
    
    def conversion(self, old_unit, old_freq):
        if old_unit.name == 'hertz':
            new_freq = old_freq / 1e9
        elif old_unit.name == 'kilohertz':
            new_freq = old_freq / 1e6
        else:
            new_freq = old_freq / 1000
        return new_freq