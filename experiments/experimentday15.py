
# I begin by importing the necessary 'glob' module to handle file path matching.
import glob

# I use the 'glob.glob' function to obtain a list of file paths matching the specified pattern.
myfiles = glob.glob("files/*.txt")

# Next, I iterate over each file path in the obtained list.
for filepath in myfiles:
    # Within a 'with' statement, I open each file in read mode ('r') to ensure proper resource handling.
    with open(filepath, 'r') as file:
        # I read the content of the file, convert it to uppercase using the 'upper()' method,
        # and then print the result to the console.
        print(file.read().upper())
