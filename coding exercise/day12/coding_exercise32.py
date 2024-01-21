"""
Implement a function that gets a person's name (e.g. john) as a parameter and returns a greeting (e.g. Hi John).
Note that the first letter of the person's name should always be uppercase.
"""


def greet_person(name):
    return f"Hi {name.capitalize()}"


# Example usage:
person_name = "lisa"
greeting = greet_person(person_name)
print(greeting)
