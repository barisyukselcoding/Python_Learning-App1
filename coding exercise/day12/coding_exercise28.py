"""
Your task for this exercise is to complete the strength function. The function is supposed to check the strength of the
 user's password.

The function should

1. get a password argument

2. return the string "Strong Password" if all of the following conditions are true:

Eight or more characters

At least one uppercase letter.

At least one digit.

3. returns "Weak Password" if at least one of the three conditions is not met.

"""


def strength(password):
    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


# Example usage:
result = strength('Adehl0uNVgD3Na')
print(result)
