"""
Define a function that:

(1) takes a string as a parameter

(2) returns False if the string contains less than eight characters

(3) returns True if the string contains eight or more characters

In other words, if I called your function with foo("mypass"), it would return False.
If I called it with foo("mylongpassword") it would return True, and so on.
"""


def pass_control(x):
    if len(x) < 8:
        return False
    else:
        return True


# Example
print(pass_control("Baris"))
