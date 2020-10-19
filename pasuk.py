import json

# If you want to change to a different type of verse
# i.e. without teamim, or without nekudot change the file path below.
# add extra arg to define how many pesukim to print.
def pasuk(book, chapter, verse, number = 1):
    chapter -= 1
    verse -= 1
    file_path = f"./sources/tanakh/{book}/teamim.json"
    with open(file_path) as json_file:
        data = json.load(json_file)
        print(''.join(data["text"][chapter][verse: verse+number]))
        
# $ python -c 'import foo; print foo.hello()'