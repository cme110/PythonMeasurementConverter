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
        
    conversion(old_unit, old_temp):
        Chooses the conversion calculation based on the name attribute of
        the old measurement unit, then does the calculation. 
        
        Args:
            old_unit (class): Represents the old measurement unit
            old_temp (int): Represents the amount of the old measurement unit

        Returns:
            new_temp (float): The result of the conversion calculation
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
