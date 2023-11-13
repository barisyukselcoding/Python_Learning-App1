"""
Write a program that reads the essay.txt file
and returns the number of characters contained in the file.
"""

file = open("essay.txt")
file_content = file.read()
file_content_length = len(file_content)
print(file_content_length)