"""
On the side panel there's a bear.txt file. The existing code opens that file in read mode.
file = open("bear.txt")

Below that code, please read the file content and print out the content.
"""

file = open("bear.txt")
file_content = file.read()
print(file_content)
