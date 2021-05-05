from lxml.objectify import ElementMaker
from os import remove

def serialize_to_xml(obj):
    elem_maker = ElementMaker(annotate=False)
    root = elem_maker("Customer")
    for key, val in obj.__dict__.items():
        if val == None:
            attr = elem_maker(key, "")
        else:
            attr = elem_maker(key, val)
        root.append(attr)
    return root

def remove_encoding_dec(temp_filename, output_filename):
    with open(filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            if line.strip() == '''<?xml version='1.0' encoding='ASCII'?>''':
                output_file.write('<?xml version="1.0"?>\n')
            else:
                output_file.write(line)
    remove(filename)