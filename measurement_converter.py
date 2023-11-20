'''The main module for running the measurement converter. Used for converting
between different measurements.
'''

from measurement_types import *

MEASURE_TYPES = """Types of measurements:
1: Temperature
2: Speed
3: Angle"""

OPTIONS = ['1', '2', '3', 'Q', 'q']
    
def valid_measurement():
    '''Asks user to input a number for the corresponding measurement or 'Q'
    for quit. If input is not a valid option, error message is printed and
    user is asked to try again until the input is a valid option.
    
    Returns:
        measurement (str): The valid user input
    '''
    
    measurement = input("Select a measurement, or type 'Q' to quit: ")
    while measurement not in OPTIONS:
        print("Invalid. Try again")
        measurement = input("Select a measurement, or type 'Q' to quit: ")
    return measurement

def main():
    '''Measurement types are printed for the user to choose from and user
    inputs a number or 'Q'. While input isn't 'Q', the corresponding measurement
    function is run, measurement types are printed again and user inputs
    another number or 'Q'.
    '''
    
    print(MEASURE_TYPES)
    measurement = valid_measurement()
    while measurement not in 'Qq':
        if measurement == '1':
            temperature()
        elif measurement == '2':
            speed()
        elif measurement == '3':
            angle()
        print(MEASURE_TYPES)
        measurement = valid_measurement()

if __name__ == "__main__":
    main()
