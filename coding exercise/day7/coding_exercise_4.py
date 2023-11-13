"""
Use Python to create a file with name file.txt and write the text snail there.

"""


text_contents = ["snail"]
filenames = ["file.txt"]

for text_content, filename in zip(text_contents, filenames):
    file = open(f"{filename}", 'w')
    file.write(text_content)






