"""
Coding Exercise 3
colors = [11, 34, 98, 43, 45, 54, 54]
Loop over the colors items and print out the item in every loop only if the item is greater than 50.
So, the output of your program would be:

98
54
54
"""
colors = [11, 34, 98, 43, 45, 54, 54]


for c in colors:
    if int(c) > 50:
        print(c)


