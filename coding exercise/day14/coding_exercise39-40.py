"""
Define a water_state function that:

1. gets a temperature argument

2. returns the string "Solid" if the temperature is less than or equal to 0

3. returns "Liquid" if the temperature is greater than 0, but less than 100.

4. returns "Gas" if the temperature is greater than or equal to 100.

In the previous exercise, we hardcoded the values 0 and 100. However, it is better to place those values in constants.
Therefore, your task is to:

1. create a FREEZING_POINT and a BOILING_POINT variable and store the values 0 and 100 in them respectively.

2. modify the function of the previous exercise by using those variables instead of the hardcoded 0 and 100 values.
The previous function is given in the code area.
"""

# Define constants for freezing point and boiling point of water
FREEZING_POINT = 0
BOILING_POINT = 100


# Define a function named water_state that takes one parameter: temperature
def water_state(temperature):
    # Check if the temperature is less than or equal to the freezing point
    if temperature <= FREEZING_POINT:
        return "Solid"
        # Check if the temperature is between the freezing point and boiling point
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
        # Return "Gas" for all other cases
    else:
        return "Gas"
