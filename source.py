import json

# If you want to change to a different type of verse
# i.e. without teamim, or without nekudot
# change the file path below.
def source(book, chapter, verse = 0):
    file_path = f"./sources/tanakh/{book}/teamim.json"
    with open(file_path) as json_file:
        data = json.load(json_file)
        if verse == 0:
            return data["text"][chapter-1]
        else:
            return data["text"][chapter-1][verse-1]
