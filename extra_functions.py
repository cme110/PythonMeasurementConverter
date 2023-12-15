'''The module containing extra functions used in other modules for validating
inputs, printing units and conversions, and processing measurement conversions.
'''

def valid_unit(options, chosen_unit=None):
    '''Chooses prompt based on if there's a chosen unit. Prompt used to ask user
    to pick a unit. If there's no chosen unit, while unit is not one of the options 
    and is not 'Q' or 'q', error message is printed and user is asked to try again until 
    input is a valid option. If there is a chosen unit, while unit is not one of the
    options, error message is printed and user is asked to try again until input is a 
    valid option.

    Args:
        options (str): Possible input options for the user
        chosen_unit (str): The unit that the user wants to convert to
            (default is None)

    Returns:
        unit (str): The valid user input
    '''
    
    if chosen_unit == None:
        prompt = "Select a unit to convert to, or type 'Q' to go back: "
        unit = input(prompt)
        while unit not in options and unit not in ['Q', 'q']:
            print("Invalid. Try again")
            unit = input(prompt)
    else:
        prompt = f"Which unit are you converting to {chosen_unit}? "
        unit = input(prompt)
        while unit not in options:
            if unit in ['Q', 'q']:
                print("You cannot quit now. Try again")
            else:
                print("Invalid. Try again")
            unit = input(prompt)
    return unit

def valid_number(measurement, unit):
    '''Makes prompt using measurement type and unit. Prompt used to ask user to
    input a number. If ValueError occurs, error message is printed and user is
    asked to try again until input is valid.

    Args:
        measurement (str): The type of measurement
        unit (str): The unit of measurement

    Returns:
        number (float): The valid user input
    '''
    
    prompt = f"Input {measurement} in {unit}: "
    while ValueError:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid. Try again")

def print_units(units, units_title):
    '''Prints all units numbered one by one.

    Args:
        units (list): All units to be printed
        units_title (str): Measurement group the units belong to
    '''
    
    print(f"\n{units_title} Units:")
    for i in range(len(units)):
        print(f"{i+1}: {units[i]}")

def print_conversion(before_num, before_symbol, after_num, after_symbol):
    '''Prints measurement conversion based on if before_num and/or after_num 
    are a floating point numbers.

    Args:
        before_num (float): The amount of the old unit before conversion
        before_symbol (str): The symbol of the old unit
        after_num (float): The amount of the new unit after conversion
        after_symbol (str): The symbol of the new unit
    '''
    if before_num % 1 == 0 and after_num % 1 == 0:
        print(f"\n{before_num:.0f}{before_symbol} = {after_num:.0f}{after_symbol}")
    elif before_num % 1 == 0 and after_num % 1 != 0:
        print(f"\n{before_num:.0f}{before_symbol} = {after_num:.3f}{after_symbol}")
    elif before_num % 1 != 0 and after_num % 1 == 0:
        print(f"\n{before_num}{before_symbol} = {after_num:.0f}{after_symbol}")
    else:
        print(f"\n{before_num}{before_symbol} = {after_num:.3f}{after_symbol}")

def process_conversion(units, options, title, new_unit):
    '''Assigns new unit to convert to. Prints remaining units. Gets and assigns
    old unit to convert from. Gets and assigns old number to do conversion.
    Assigns a new number after the conversion and conversion is printed

    Args:
        units (list): All units to choose from
        options (str): Possible input options
        title (str): Type of measurement conversion
        new_unit (str): Selected option from unit list
    '''
    new_unit = units.pop(int(new_unit) - 1)
    print_units(units, f'Remaining {title}')
    old_unit = valid_unit(options[:-1], new_unit.name)
    old_unit = units.pop(int(old_unit) - 1)
    old_number = valid_number(title.lower(), old_unit.name)
    new_number = new_unit.conversion(old_unit, old_number)
    print_conversion(old_number, old_unit.symbol, new_number, new_unit.symbol)
