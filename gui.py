from tkinter import *
from measurement_units import *

window = Tk()
window.title('Converter')
window.geometry('340x90')

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

def temperature():
    measurements.config(text='Temperature')
    textbox.delete(0, END)
    result.config(text='-')
    celsius_b()
    fahrenheit_a()

def celsius_b():
    unit_before(Celsius())
    before.menu.add_command(label=Fahrenheit(), command=fahrenheit_b)
    before.menu.add_command(label=Kelvin(), command=kelvin_b)

def fahrenheit_b():
    unit_before(Fahrenheit())
    before.menu.add_command(label=Celsius(), command=celsius_b)
    before.menu.add_command(label=Kelvin(), command=kelvin_b)

def kelvin_b():
    unit_before(Kelvin())
    before.menu.add_command(label=Celsius(), command=celsius_b)
    before.menu.add_command(label=Fahrenheit(), command=fahrenheit_b)

def celsius_a():
    unit_after(Celsius())
    after.menu.add_command(label=Fahrenheit(), command=fahrenheit_a)
    after.menu.add_command(label=Kelvin(), command=kelvin_a)

def fahrenheit_a():
    unit_after(Fahrenheit())
    after.menu.add_command(label=Celsius(), command=celsius_a)
    after.menu.add_command(label=Kelvin(), command=kelvin_a)

def kelvin_a():
    unit_after(Kelvin())
    after.menu.add_command(label=Celsius(), command=celsius_a)
    after.menu.add_command(label=Fahrenheit(), command=fahrenheit_a)
    
def speed():
    units = [MetresPerSecond(), KilometresPerHour(), FeetPerSecond(),
             MilesPerHour(), Knots()]
    measurements.config(text='Speed')
    textbox.delete(0, END)
    result.config(text='-')
    unit_settings(units)

def angle():
    units = [Degrees(), Radians(), Milliradians(), Gradians(), Arcseconds(),
             Arcminutes()]
    measurements.config(text='Angle')
    textbox.delete(0, END)
    result.config(text='-')
    unit_settings(units)

def unit_settings(units, before_index=0, after_index=1):
    units_copy = units[:]
    global before_unit
    before_unit = units_copy.pop(before_index)
    before.config(text=before_unit)
    before.menu = Menu(before, tearoff=0)
    before['menu'] = before.menu
    for unit in units_copy:
        before.menu.add_command(label=unit, font=(0))

    units_copy = units[:]
    global after_unit
    after_unit = units_copy.pop(after_index)
    after.config(text=after_unit)
    after.menu = Menu(after, tearoff=0)
    after['menu'] = after.menu
    for unit in units_copy:
        after.menu.add_command(label=unit, font=(0))

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
    
measure_types = {'Temperature': temperature, 'Speed': speed, 'Angle': angle}
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

temperature()

window.mainloop()