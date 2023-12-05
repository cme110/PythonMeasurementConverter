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
