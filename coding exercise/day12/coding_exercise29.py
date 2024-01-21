"""
Define a function that takes a list as an argument and returns the average value of the list items. For example,
if I called your function with foo([10, 20, 30, 40]) it should return 25, the average of the numbers of the list.
"""


def calculate_average(lst):
    # I check if I have elements in the list
    if len(lst) == 0:
        return 0  # I return 0 for an empty list; I may choose to handle this case differently

    # I calculate the sum of the list items
    total = sum(lst)

    # I calculate the average
    average = total / len(lst)

    return average


# Example usage
my_list = [10, 20, 30, 40]
result = calculate_average(my_list)
print(result)
