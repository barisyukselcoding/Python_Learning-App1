"""
Bug-Fixing Exercise 1
Alina has created a speed calculation function. She traveled a total of 200 miles today which took her two hours.
She wants to use her function to calculate the average speed.

def speed(distance, time):
    return distance / time

print(speed([200, 4]))
However, when she calls the function (as you see below), she gets an error:

TypeError: speed() missing 1 required positional argument: 'time'

Try fixing the code, so she gets 50 as output.
"""


def speed(distance, time):
    return distance / time


# Unpack the list when calling the function
print(speed(*[200, 4]))

# Or another solution would be

print(speed(200, 4))

# We remove the square brackets around 200, 4 here because the function expects two numbers as arguments, not a list.
