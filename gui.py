from tkinter import *
from measurement_units import *

window = Tk()
window.title('Converter')
window.geometry('340x90')

class Temperature():
    def __init__(self):
        self.celsius, self.fahrenheit, self.kelvin = Celsius(), Fahrenheit(), Kelvin()
        self.units = {self.celsius: (self.celsius_b, self.celsius_a), self.fahrenheit: (self.fahrenheit_b, self.fahrenheit_a), 
                      self.kelvin: (self.kelvin_b, self.kelvin_a)}
        current_measurment('Temperature')
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

class Speed():
    def __init__(self):
        self.mps, self.kph, self.fps, self.mph, self.knots = MetresPerSecond(), KilometresPerHour(), FeetPerSecond(), MilesPerHour(), Knots()
        self.units = {self.mps: (self.mps_b, self.mps_a), self.kph: (self.kph_b, self.kph_a), self.fps: (self.fps_b, self.fps_a,),
                      self.mph: (self.mph_b, self.mph_a), self.knots: (self.knots_b, self.knots_a)}
        current_measurment('Speed')
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

class Angle():
    def __init__(self):
        self.degree, self.radian, self.milli, self.gradian, self.arcsec, self.arcmin = Degrees(), Radians(), Milliradians(), Gradians(), Arcseconds(), Arcminutes()
        self.units = {self.degree: (self.degree_b, self.degree_a), self.radian: (self.radian_b, self.radian_a), self.milli:
                      (self.milli_b, self.milli_a), self.gradian: (self.gradian_b, self.gradian_a), self.arcsec:
                      (self.arcsec_b, self.arcsec_a), self.arcmin: (self.arcmin_b, self.arcmin_a)}
        current_measurment('Angle')
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

def unit_before(unit):
    result.config(text='-')
    global before_unit
    before_unit = unit
    before.config(text=before_unit)
    before.menu = Menu(before, font=(0), tearoff=0)
    before['menu'] = before.menu

def unit_after(unit):
    result.config(text='-')
    global after_unit
    after_unit = unit
    after.config(text=after_unit)
    after.menu = Menu(after, font=(0), tearoff=0)
    after['menu'] = after.menu

def current_measurment(label):
    measurements.config(text=label)
    textbox.delete(0, END)
    result.config(text='-')

def equals_button():
    try:
        number = float(textbox.get())
        if before_unit.name == after_unit.name:
            result.config(text=f'{number}{after_unit.symbol}')
        else:
            new_number = after_unit.conversion(before_unit, number)
            result.config(text=f'{new_number:.3f}{after_unit.symbol}')
    except ValueError:
        result.config(text='-')
    
measure_types = {'Temperature': Temperature, 'Speed': Speed, 'Angle': Angle}
measurements = Menubutton(window, text='Temperature', font=(0))
measurements.menu = Menu(measurements, font=(0), tearoff=0)
measurements['menu'] = measurements.menu
for key, value in measure_types.items():
    measurements.menu.add_command(label=key, command=value)
measurements.grid(column=0, row=0)

textbox = Entry(window, width=16, font=(0))
result = Label(window, text='-', font=(0))
equals = Button(window, text=' = ', font=(0), command=equals_button)
textbox.grid(column=0, row=1)
result.grid(column=2, row=1)
equals.grid(column=1, row=1)

before = Menubutton(window, font=(0))
before_unit = None
after = Menubutton(window, font=(0))
after_unit = None
before.grid(column=0, row=2)
after.grid(column=2, row=2)

Temperature()

window.mainloop()