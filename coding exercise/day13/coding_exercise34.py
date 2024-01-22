"""
Write a get_nr_items function that:

1. gets as a parameter one string with commas. E.g., "john,lisa, teresa"

2. the function should return the number of items divided by commas in that string
(i.e., that would be three items in the above example)

2. returns the number of items.
"""


def get_nr_items(input_string):
    # I split the input string by commas and count the number of items
    items = input_string.split(',')
    num_items = len(items)
    return num_items

    # Example usage:


input_string = "john,lisa,teresa"
result = get_nr_items(input_string)
print(result)
