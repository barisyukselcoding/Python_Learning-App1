"""
Implement a function that gets a person's name as a parameter and greets the person with Hi Person. For example,
if I call your function using foo("lisa") the function should return Hi lisa
"""


def greet_person(name):
    return f"Hi {name}"


# Example usage:
person_name = "Lisa"
greeting = greet_person(person_name)
print(greeting)
