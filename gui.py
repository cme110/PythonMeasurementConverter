'''The main GUI module for running the measurement converter. Used for converting
between different measurements.

All classes have these attributes:
    One attribute for each unit in the measurement class (class)
    units (dict): Containing the two methods establishing the before and after units
    for each unit

All classes have these methods:
    __init__():
        Initialises class by assigning attributes, running current_measurement function
        and calling one before method and one after method.
        
    One method for each unit in the measurement class displayed in the before menu:
        Assigns unit to be the before unit, changes before menu button to the unit's name,
        Adds the remaining units to the menu.

    One method for each unit in the measurement class displayed in the after menu:
        Assigns unit to be the after unit, changes after menu button to the unit's name,
        Adds the remaining units to the menu.
'''

from tkinter import *
from typing import Any
from measurement_units import *

window = Tk()
window.title('Measurement Converter')
window.geometry('395x90')

# Temperature Menus ============================================================

class Temperature():
    def __init__(self):
        self.celsius, self.fahrenheit, self.kelvin = Celsius(), Fahrenheit(), Kelvin()
        self.units = {self.celsius: (self.celsius_b, self.celsius_a),
                      self.fahrenheit: (self.fahrenheit_b, self.fahrenheit_a), 
                      self.kelvin: (self.kelvin_b, self.kelvin_a)}
        current_measurement('Temperature')
        self.celsius_b()
        self.fahrenheit_a()

    def celsius_b(self):
        units = self.units.copy()
        del units[self.celsius]
        unit_before(self.celsius)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def fahrenheit_b(self):
        units = self.units.copy()
        del units[self.fahrenheit]
        unit_before(self.fahrenheit)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def kelvin_b(self):
        units = self.units.copy()
        del units[self.kelvin]
        unit_before(self.kelvin)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def celsius_a(self):
        units = self.units.copy()
        del units[self.celsius]
        unit_after(self.celsius)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def fahrenheit_a(self):
        units = self.units.copy()
        del units[self.fahrenheit]
        unit_after(self.fahrenheit)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def kelvin_a(self):
        units = self.units.copy()
        del units[self.kelvin]
        unit_after(self.kelvin)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

# Length Menus =================================================================

class Length():
    def __init__(self):
        self.metre, self.kilo, self.centi = Metres(), Kilometres(), Centimetres()
        self.milli, self.micro, self.nano = Millimetres(), Micrometres(), Nanometres()
        self.mile, self.yard, self.feet = Miles(), Yards(), Feet()
        self.inch, self.nautical = Inches(), NauticalMiles()
        self.units = {self.metre: (self.metre_b, self.metre_a), self.kilo: (self.kilo_b, self.kilo_a),
                     self.centi: (self.centi_b, self.centi_a), self.milli: (self.milli_b, self.milli_a),
                     self.micro: (self.micro_b, self.micro_a), self.nano: (self.nano_b, self.nano_a),
                     self.mile: (self.mile_b, self.mile_a), self.yard: (self.yard_b, self.yard_a),
                     self.feet: (self.feet_b, self.feet_a), self.inch: (self.inch_b, self.inch_a),
                     self.nautical: (self.nautical_b, self.nautical_a)}
        current_measurement('Length')
        self.kilo_b()
        self.metre_a()

    def metre_b(self):
        units = self.units.copy()
        del units[self.metre]
        unit_before(self.metre)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def kilo_b(self):
        units = self.units.copy()
        del units[self.kilo]
        unit_before(self.kilo)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def centi_b(self):
        units = self.units.copy()
        del units[self.centi]
        unit_before(self.centi)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def milli_b(self):
        units = self.units.copy()
        del units[self.milli]
        unit_before(self.milli)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def micro_b(self):
        units = self.units.copy()
        del units[self.micro]
        unit_before(self.micro)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def nano_b(self):
        units = self.units.copy()
        del units[self.nano]
        unit_before(self.nano)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def mile_b(self):
        units = self.units.copy()
        del units[self.mile]
        unit_before(self.mile)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def yard_b(self):
        units = self.units.copy()
        del units[self.yard]
        unit_before(self.yard)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def feet_b(self):
        units = self.units.copy()
        del units[self.feet]
        unit_before(self.feet)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def inch_b(self):
        units = self.units.copy()
        del units[self.inch]
        unit_before(self.inch)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def nautical_b(self):
        units = self.units.copy()
        del units[self.nautical]
        unit_before(self.nautical)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def metre_a(self):
        units = self.units.copy()
        del units[self.metre]
        unit_after(self.metre)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def kilo_a(self):
        units = self.units.copy()
        del units[self.kilo]
        unit_after(self.kilo)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def centi_a(self):
        units = self.units.copy()
        del units[self.centi]
        unit_after(self.centi)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def milli_a(self):
        units = self.units.copy()
        del units[self.milli]
        unit_after(self.milli)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def micro_a(self):
        units = self.units.copy()
        del units[self.micro]
        unit_after(self.micro)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def nano_a(self):
        units = self.units.copy()
        del units[self.nano]
        unit_after(self.nano)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def mile_a(self):
        units = self.units.copy()
        del units[self.mile]
        unit_after(self.mile)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def yard_a(self):
        units = self.units.copy()
        del units[self.yard]
        unit_after(self.yard)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def feet_a(self):
        units = self.units.copy()
        del units[self.feet]
        unit_after(self.feet)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def inch_a(self):
        units = self.units.copy()
        del units[self.inch]
        unit_after(self.inch)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def nautical_a(self):
        units = self.units.copy()
        del units[self.nautical]
        unit_after(self.nautical)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

# Mass Menus ==================================================================

class Mass():
    def __init__(self):
        self.gram, self.kilo, self.tonne = Grams(), Kilograms(), Tonnes()
        self.milli, self.micro, self.ounce = Milligrams(), Micrograms(), Ounces()
        self.pound, self.stone, self.imperial, self.us = Pounds(), Stone(), ImperialTons(), USTons()
        self.units = {self.gram: (self.gram_b, self.gram_a), self.kilo: (self.kilo_b, self.kilo_a),
                      self.tonne: (self.tonne_b, self.tonne_a), self.milli: (self.milli_b, self.milli_a),
                      self.micro: (self.micro_b, self.micro_a), self.ounce: (self.ounce_b, self.ounce_a),
                      self.pound: (self.pound_b, self.pound_a), self.stone: (self.stone_b, self.stone_a),
                      self.imperial: (self.imperial_b, self.imperial_a), self.us: (self.us_b, self.us_a)}
        current_measurement('Mass')
        self.kilo_b()
        self.gram_a()
    
    def gram_b(self):
        units = self.units.copy()
        del units[self.gram]
        unit_before(self.gram)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def kilo_b(self):
        units = self.units.copy()
        del units[self.kilo]
        unit_before(self.kilo)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def tonne_b(self):
        units = self.units.copy()
        del units[self.tonne]
        unit_before(self.tonne)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def milli_b(self):
        units = self.units.copy()
        del units[self.milli]
        unit_before(self.milli)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def micro_b(self):
        units = self.units.copy()
        del units[self.micro]
        unit_before(self.micro)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def ounce_b(self):
        units = self.units.copy()
        del units[self.ounce]
        unit_before(self.ounce)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def pound_b(self):
        units = self.units.copy()
        del units[self.pound]
        unit_before(self.pound)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def stone_b(self):
        units = self.units.copy()
        del units[self.stone]
        unit_before(self.stone)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def imperial_b(self):
        units = self.units.copy()
        del units[self.imperial]
        unit_before(self.imperial)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def us_b(self):
        units = self.units.copy()
        del units[self.us]
        unit_before(self.us)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def gram_a(self):
        units = self.units.copy()
        del units[self.gram]
        unit_after(self.gram)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def kilo_a(self):
        units = self.units.copy()
        del units[self.kilo]
        unit_after(self.kilo)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def tonne_a(self):
        units = self.units.copy()
        del units[self.tonne]
        unit_after(self.tonne)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def milli_a(self):
        units = self.units.copy()
        del units[self.milli]
        unit_after(self.milli)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def micro_a(self):
        units = self.units.copy()
        del units[self.micro]
        unit_after(self.micro)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def ounce_a(self):
        units = self.units.copy()
        del units[self.ounce]
        unit_after(self.ounce)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def pound_a(self):
        units = self.units.copy()
        del units[self.pound]
        unit_after(self.pound)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def stone_a(self):
        units = self.units.copy()
        del units[self.stone]
        unit_after(self.stone)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def imperial_a(self):
        units = self.units.copy()
        del units[self.imperial]
        unit_after(self.imperial)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def us_a(self):
        units = self.units.copy()
        del units[self.us]
        unit_after(self.us)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

# Time Menus ==================================================================

class Time():
    def __init__(self):
        self.nano, self.micro, self.milli = Nanoseconds(), Microseconds(), Milliseconds()
        self.sec, self.min, self.hour, = Seconds(), Minutes(), Hours()
        self.day, self.week, self.month = Days(), Weeks(), Months()
        self.year, self.deca, self.cent = Years(), Decades(), Centuries()
        self.units = {self.nano: (self.nano_b, self.nano_a), self.micro: (self.micro_b, self.micro_a),
                      self.milli: (self.milli_b, self.milli_a), self.sec: (self.sec_b, self.sec_a),
                      self.min: (self.min_b, self.min_a), self.hour: (self.hour_b, self.hour_a),
                      self.day: (self.day_b, self.day_a), self.week: (self.week_b, self.week_a),
                      self.month: (self.month_b, self.month_a), self.year: (self.year_b, self.year_a),
                      self.deca: (self.deca_b, self.deca_a), self.cent: (self.cent_b, self.cent_a)}
        current_measurement('Time')
        self.min_b()
        self.sec_a()
    
    def nano_b(self):
        units = self.units.copy()
        del units[self.nano]
        unit_before(self.nano)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def micro_b(self):
        units = self.units.copy()
        del units[self.micro]
        unit_before(self.micro)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def milli_b(self):
        units = self.units.copy()
        del units[self.milli]
        unit_before(self.milli)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def sec_b(self):
        units = self.units.copy()
        del units[self.sec]
        unit_before(self.sec)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def min_b(self):
        units = self.units.copy()
        del units[self.min]
        unit_before(self.min)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def hour_b(self):
        units = self.units.copy()
        del units[self.hour]
        unit_before(self.hour)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def day_b(self):
        units = self.units.copy()
        del units[self.day]
        unit_before(self.day)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def week_b(self):
        units = self.units.copy()
        del units[self.week]
        unit_before(self.week)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def month_b(self):
        units = self.units.copy()
        del units[self.month]
        unit_before(self.month)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def year_b(self):
        units = self.units.copy()
        del units[self.year]
        unit_before(self.year)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def deca_b(self):
        units = self.units.copy()
        del units[self.deca]
        unit_before(self.deca)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def cent_b(self):
        units = self.units.copy()
        del units[self.cent]
        unit_before(self.cent)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def nano_a(self):
        units = self.units.copy()
        del units[self.nano]
        unit_after(self.nano)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def micro_a(self):
        units = self.units.copy()
        del units[self.micro]
        unit_after(self.micro)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def milli_a(self):
        units = self.units.copy()
        del units[self.milli]
        unit_after(self.milli)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def sec_a(self):
        units = self.units.copy()
        del units[self.sec]
        unit_after(self.sec)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def min_a(self):
        units = self.units.copy()
        del units[self.min]
        unit_after(self.min)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def hour_a(self):
        units = self.units.copy()
        del units[self.hour]
        unit_after(self.hour)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def day_a(self):
        units = self.units.copy()
        del units[self.day]
        unit_after(self.day)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def week_a(self):
        units = self.units.copy()
        del units[self.week]
        unit_after(self.week)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def month_a(self):
        units = self.units.copy()
        del units[self.month]
        unit_after(self.month)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def year_a(self):
        units = self.units.copy()
        del units[self.year]
        unit_after(self.year)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def deca_a(self):
        units = self.units.copy()
        del units[self.deca]
        unit_after(self.deca)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def cent_a(self):
        units = self.units.copy()
        del units[self.cent]
        unit_after(self.cent)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
# Speed Menus ==================================================================

class Speed():
    def __init__(self):
        self.mps, self.kph, self.fps = MetresPerSecond(), KilometresPerHour(), FeetPerSecond()
        self.mph, self.knots = MilesPerHour(), Knots()
        self.units = {self.mps: (self.mps_b, self.mps_a), self.kph: (self.kph_b, self.kph_a),
                      self.fps: (self.fps_b, self.fps_a,), self.mph: (self.mph_b, self.mph_a),
                      self.knots: (self.knots_b, self.knots_a)}
        current_measurement('Speed')
        self.mps_b()
        self.kph_a()

    def mps_b(self):
        units = self.units.copy()
        del units[self.mps]
        unit_before(self.mps)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def kph_b(self):
        units = self.units.copy()
        del units[self.kph]
        unit_before(self.kph)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def fps_b(self):
        units = self.units.copy()
        del units[self.fps]
        unit_before(self.fps)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def mph_b(self):
        units = self.units.copy()
        del units[self.mph]
        unit_before(self.mph)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def knots_b(self):
        units = self.units.copy()
        del units[self.knots]
        unit_before(self.knots)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def mps_a(self):
        units = self.units.copy()
        del units[self.mps]
        unit_after(self.mps)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def kph_a(self):
        units = self.units.copy()
        del units[self.kph]
        unit_after(self.kph)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def fps_a(self):
        units = self.units.copy()
        del units[self.fps]
        unit_after(self.fps)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def mph_a(self):
        units = self.units.copy()
        del units[self.mph]
        unit_after(self.mph)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def knots_a(self):
        units = self.units.copy()
        del units[self.knots]
        unit_after(self.knots)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

# Angle Menus ==================================================================

class Angle():
    def __init__(self):
        self.degree, self.radian, self.milli = Degrees(), Radians(), Milliradians()
        self.gradian, self.arcsec, self.arcmin = Gradians(), Arcseconds(), Arcminutes()
        self.units = {self.degree: (self.degree_b, self.degree_a), self.radian: (self.radian_b, self.radian_a),
                      self.milli: (self.milli_b, self.milli_a), self.gradian: (self.gradian_b, self.gradian_a),
                      self.arcsec: (self.arcsec_b, self.arcsec_a), self.arcmin: (self.arcmin_b, self.arcmin_a)}
        current_measurement('Angle')
        self.degree_b()
        self.radian_a()

    def degree_b(self):
        units = self.units.copy()
        del units[self.degree]
        unit_before(self.degree)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def radian_b(self):
        units = self.units.copy()
        del units[self.radian]
        unit_before(self.radian)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def milli_b(self):
        units = self.units.copy()
        del units[self.milli]
        unit_before(self.milli)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def gradian_b(self):
        units = self.units.copy()
        del units[self.gradian]
        unit_before(self.gradian)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def arcsec_b(self):
        units = self.units.copy()
        del units[self.arcsec]
        unit_before(self.arcsec)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def arcmin_b(self):
        units = self.units.copy()
        del units[self.arcmin]
        unit_before(self.arcmin)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def degree_a(self):
        units = self.units.copy()
        del units[self.degree]
        unit_after(self.degree)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def radian_a(self):
        units = self.units.copy()
        del units[self.radian]
        unit_after(self.radian)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def milli_a(self):
        units = self.units.copy()
        del units[self.milli]
        unit_after(self.milli)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def gradian_a(self):
        units = self.units.copy()
        del units[self.gradian]
        unit_after(self.gradian)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def arcsec_a(self):
        units = self.units.copy()
        del units[self.arcsec]
        unit_after(self.arcsec)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def arcmin_a(self):
        units = self.units.copy()
        del units[self.arcmin]
        unit_after(self.arcmin)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

# Area Menus ===================================================================

class Area():
    def __init__(self):
        self.sqm, self.sqkm, self.sqmi = SquareMetres(), SquareKilometres(), SquareMiles()
        self.sqyd, self.sqft, self.sqin = SquareYards(), SquareFeet(), SquareInches()
        self.hect, self.acre = Hectares(), Acres()
        self.units = {self.sqm: (self.sqm_b, self.sqm_a), self.sqkm: (self.sqkm_b, self.sqkm_a),
                      self.sqmi: (self.sqmi_b, self.sqmi_a), self.sqyd: (self.sqyd_b, self.sqyd_a),
                      self.sqft: (self.sqft_b, self.sqft_a), self.sqin: (self.sqin_b, self.sqin_a),
                      self.hect: (self.hect_b, self.hect_a), self.acre: (self.acre_b, self.acre_a)}
        current_measurement('Area')
        self.sqkm_b()
        self.sqm_a()

    def sqm_b(self):
        units = self.units.copy()
        del units[self.sqm]
        unit_before(self.sqm)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def sqkm_b(self):
        units = self.units.copy()
        del units[self.sqkm]
        unit_before(self.sqkm)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def sqmi_b(self):
        units = self.units.copy()
        del units[self.sqmi]
        unit_before(self.sqmi)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def sqyd_b(self):
        units = self.units.copy()
        del units[self.sqyd]
        unit_before(self.sqyd)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def sqft_b(self):
        units = self.units.copy()
        del units[self.sqft]
        unit_before(self.sqft)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def sqin_b(self):
        units = self.units.copy()
        del units[self.sqin]
        unit_before(self.sqin)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def hect_b(self):
        units = self.units.copy()
        del units[self.hect]
        unit_before(self.hect)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def acre_b(self):
        units = self.units.copy()
        del units[self.acre]
        unit_before(self.acre)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def sqm_a(self):
        units = self.units.copy()
        del units[self.sqm]
        unit_after(self.sqm)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def sqkm_a(self):
        units = self.units.copy()
        del units[self.sqkm]
        unit_after(self.sqkm)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def sqmi_a(self):
        units = self.units.copy()
        del units[self.sqmi]
        unit_after(self.sqmi)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def sqyd_a(self):
        units = self.units.copy()
        del units[self.sqyd]
        unit_after(self.sqyd)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def sqft_a(self):
        units = self.units.copy()
        del units[self.sqft]
        unit_after(self.sqft)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def sqin_a(self):
        units = self.units.copy()
        del units[self.sqin]
        unit_after(self.sqin)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def hect_a(self):
        units = self.units.copy()
        del units[self.hect]
        unit_after(self.hect)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

    def acre_a(self):
        units = self.units.copy()
        del units[self.acre]
        unit_after(self.acre)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

# Digital Storage Menus ===================================================================

class Digital_Storage():
    def __init__(self):
        self.bit, self.byte, self.kilo = Bits(), Bytes(), Kilobytes()
        self.mega, self.giga, self.tera = Megabytes(), Gigabytes(), Terabytes()
        self.peta, self.kibi, self.mebi = Petabytes(), Kibibytes(), Mebibytes()
        self.gibi, self.tebi, self.pebi = Gibibytes(), Tebibytes(), Pebibytes()
        self.units = {self.bit: (self.bit_b, self.bit_a), self.byte: (self.byte_b, self.byte_a),
                      self.kilo: (self.kilo_b, self.kilo_a), self.mega: (self.mega_b, self.mega_a),
                      self.giga: (self.giga_b, self.giga_a), self.tera: (self.tera_b, self.tera_a),
                      self.peta: (self.peta_b, self.peta_a), self.kibi: (self.kibi_b, self.kibi_a),
                      self.mebi: (self.mebi_b, self.mebi_a), self.gibi: (self.gibi_b, self.gibi_a),
                      self.tebi: (self.tebi_b, self.tebi_a), self.pebi: (self.pebi_b, self.pebi_a)}
        current_measurement('Digital Storage')
        self.kilo_b()
        self.byte_a()
    
    def bit_b(self):
        units = self.units.copy()
        del units[self.bit]
        unit_before(self.bit)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def byte_b(self):
        units = self.units.copy()
        del units[self.byte]
        unit_before(self.byte)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])

    def kilo_b(self):
        units = self.units.copy()
        del units[self.kilo]
        unit_before(self.kilo)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def mega_b(self):
        units = self.units.copy()
        del units[self.mega]
        unit_before(self.mega)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def giga_b(self):
        units = self.units.copy()
        del units[self.giga]
        unit_before(self.giga)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def tera_b(self):
        units = self.units.copy()
        del units[self.tera]
        unit_before(self.tera)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def peta_b(self):
        units = self.units.copy()
        del units[self.peta]
        unit_before(self.peta)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def kibi_b(self):
        units = self.units.copy()
        del units[self.kibi]
        unit_before(self.kibi)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def mebi_b(self):
        units = self.units.copy()
        del units[self.mebi]
        unit_before(self.mebi)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def gibi_b(self):
        units = self.units.copy()
        del units[self.gibi]
        unit_before(self.gibi)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def tebi_b(self):
        units = self.units.copy()
        del units[self.tebi]
        unit_before(self.tebi)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def pebi_b(self):
        units = self.units.copy()
        del units[self.pebi]
        unit_before(self.pebi)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def bit_a(self):
        units = self.units.copy()
        del units[self.bit]
        unit_after(self.bit)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def byte_a(self):
        units = self.units.copy()
        del units[self.byte]
        unit_after(self.byte)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def kilo_a(self):
        units = self.units.copy()
        del units[self.kilo]
        unit_after(self.kilo)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def mega_a(self):
        units = self.units.copy()
        del units[self.mega]
        unit_after(self.mega)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def giga_a(self):
        units = self.units.copy()
        del units[self.giga]
        unit_after(self.giga)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def tera_a(self):
        units = self.units.copy()
        del units[self.tera]
        unit_after(self.tera)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def peta_a(self):
        units = self.units.copy()
        del units[self.peta]
        unit_after(self.peta)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def kibi_a(self):
        units = self.units.copy()
        del units[self.kibi]
        unit_after(self.kibi)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def mebi_a(self):
        units = self.units.copy()
        del units[self.mebi]
        unit_after(self.mebi)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def gibi_a(self):
        units = self.units.copy()
        del units[self.gibi]
        unit_after(self.gibi)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
        
    def tebi_a(self):
        units = self.units.copy()
        del units[self.tebi]
        unit_after(self.tebi)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def pebi_a(self):
        units = self.units.copy()
        del units[self.pebi]
        unit_after(self.pebi)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

# Area Menus ===================================================================

class Pressure():
    def __init__(self):
        self.pascal, self.psi, self.bar = Pascals(), PoundsPerSquareInch(), Bars()
        self.atm, self.torr = StandardAtmospheres(), Torrs()
        self.units = {self.pascal: (self.pascal_b, self.pascal_a), self.psi: (self.psi_b, self.psi_a),
                      self.bar: (self.bar_b, self.bar_a), self.atm: (self.atm_b, self.atm_a),
                      self.torr: (self.torr_b, self.torr_a)}
        current_measurement('Pressure')
        self.pascal_b()
        self.psi_a()
    
    def pascal_b(self):
        units = self.units.copy()
        del units[self.pascal]
        unit_before(self.pascal)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def psi_b(self):
        units = self.units.copy()
        del units[self.psi]
        unit_before(self.psi)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def bar_b(self):
        units = self.units.copy()
        del units[self.bar]
        unit_before(self.bar)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def atm_b(self):
        units = self.units.copy()
        del units[self.atm]
        unit_before(self.atm)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def torr_b(self):
        units = self.units.copy()
        del units[self.torr]
        unit_before(self.torr)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def pascal_a(self):
        units = self.units.copy()
        del units[self.pascal]
        unit_after(self.pascal)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def psi_a(self):
        units = self.units.copy()
        del units[self.psi]
        unit_after(self.psi)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def bar_a(self):
        units = self.units.copy()
        del units[self.bar]
        unit_after(self.bar)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def atm_a(self):
        units = self.units.copy()
        del units[self.atm]
        unit_after(self.atm)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def torr_a(self):
        units = self.units.copy()
        del units[self.torr]
        unit_after(self.torr)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

# Frequency Menus ===================================================================

class Frequency():
    def __init__(self):
        self.hertz, self.kilo, self.mega, self.giga = Hertz(), Kilohertz(), Megahertz(), Gigahertz()
        self.units = {self.hertz: (self.hertz_b, self.hertz_a), self.kilo: (self.kilo_b, self.kilo_a),
                      self.mega: (self.mega_b, self.mega_a), self.giga: (self.giga_b, self.giga_a)}
        current_measurement('Frequency')
        self.kilo_b()
        self.hertz_a()
    
    def hertz_b(self):
        units = self.units.copy()
        del units[self.hertz]
        unit_before(self.hertz)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def kilo_b(self):
        units = self.units.copy()
        del units[self.kilo]
        unit_before(self.kilo)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def mega_b(self):
        units = self.units.copy()
        del units[self.mega]
        unit_before(self.mega)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def giga_b(self):
        units = self.units.copy()
        del units[self.giga]
        unit_before(self.giga)
        for key, value in units.items():
            before.menu.add_command(label=key, command=value[0])
    
    def hertz_a(self):
        units = self.units.copy()
        del units[self.hertz]
        unit_after(self.hertz)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def kilo_a(self):
        units = self.units.copy()
        del units[self.kilo]
        unit_after(self.kilo)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def mega_a(self):
        units = self.units.copy()
        del units[self.mega]
        unit_after(self.mega)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])
    
    def giga_a(self):
        units = self.units.copy()
        del units[self.giga]
        unit_after(self.giga)
        for key, value in units.items():
            after.menu.add_command(label=key, command=value[1])

def unit_before(unit):
    '''Assigns a unit to be the before unit and changes the menu button of the
    before menu.

    Args:
        unit (class): The unit chosen to be the before unit
    '''
    result.config(text='-')
    global before_unit
    before_unit = unit
    before.config(text=before_unit)
    before.menu = Menu(before, font=(0), tearoff=0)
    before['menu'] = before.menu

def unit_after(unit):
    '''Assigns a unit to be the after unit and changes the menu button of the
    after menu.

    Args:
        unit (class): The unit chosen to be the after unit
    '''
    
    result.config(text='-')
    global after_unit
    after_unit = unit
    after.config(text=after_unit)
    after.menu = Menu(after, font=(0), tearoff=0)
    after['menu'] = after.menu

def current_measurement(label):
    '''Changes the menu button of the measurements menu and resets the textbox
    and result.

    Args:
        label (str): The text the measurements menu button will be changed to
    '''
    
    measurements.config(text=label)
    textbox.delete(0, END)
    result.config(text='-')

def equals_button():
    '''Perfoms conversion when equals button is pressed. If the user types
    invalid input, the result will be '-'. If the before and after units are
    the same, the result will be the users input.
    '''
    
    try:
        number = float(textbox.get())
        if before_unit.name == after_unit.name:
            if number % 1 == 0:
                result.config(text=f'{number:.0f}{after_unit.symbol}')
            else:
                result.config(text=f'{number}{after_unit.symbol}')
        else:
            new_number = after_unit.conversion(before_unit, number)
            if new_number % 1 == 0:
                result.config(text=f'{new_number:.0f}{after_unit.symbol}')
            else:
                result.config(text=f'{new_number:.3f}{after_unit.symbol}')
    except ValueError:
        result.config(text='-')

# Creates dropdown menu displaying each type of measurement
measure_types = {'Temperature': Temperature, 'Length': Length, 'Mass': Mass, 'Time': Time, 
                 'Speed': Speed, 'Angle': Angle, 'Area': Area, 'Digital Storage': Digital_Storage,
                 'Pressure': Pressure, 'Frequency': Frequency}
measurements = Menubutton(window, text='Temperature', font=(0))
measurements.menu = Menu(measurements, font=(0), tearoff=0)
measurements['menu'] = measurements.menu
for key, value in measure_types.items():
    measurements.menu.add_command(label=key, command=value)
measurements.grid(column=0, row=0)

# Creates textbox for user input, result label for displaying the output and equals button
textbox = Entry(window, width=20, font=(0))
result = Label(window, text='-', font=(0))
equals = Button(window, text=' = ', font=(0), command=equals_button)
textbox.grid(column=0, row=1)
result.grid(column=2, row=1)
equals.grid(column=1, row=1)

# Creates dropdown menus displaying units before and after conversion
before = Menubutton(window, font=(0))
before_unit = None
after = Menubutton(window, font=(0))
after_unit = None
before.grid(column=0, row=2)
after.grid(column=2, row=2)

Temperature()

window.mainloop()
