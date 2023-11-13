contents = ["Philadelphia is a nice city",
            "Because it is the city where ISA lives",
            "Isa is my love"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)