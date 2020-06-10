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


# latex_jinja_env = jinja2.Environment(
# 	block_start_string = '\BLOCK{', block_end_string = '}',
# variable_start_string = '\VAR{', variable_end_string = '}', 
# comment_start_string = '\#{', comment_end_string = '}', 
# line_statement_prefix = '%%', 
# line_comment_prefix = '%#', 
# trim_blocks = True, 
# autoescape = False, 
# loader = jinja2.PackageLoader('app', 'templates'))