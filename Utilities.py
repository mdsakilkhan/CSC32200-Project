from lxml.objectify import ElementMaker
from os import remove

def serialize_object(obj, obj_name):
    elem_maker = ElementMaker(annotate=False)
    root = elem_maker(obj_name)
    for key, val in obj.__dict__.items():
        if val == None:
            attr = elem_maker(key, "")
        elif not type(val) == str:
            attr = elem_maker(key)
            for elt in val:
                item = elem_maker("item",elt.id)
                if elt.date == None:
                    item.set('date',"")
                else:
                    item.set('date',elt.date)
                attr.append(item)
        else:
            attr = elem_maker(key, val)
        root.append(attr)
    return root

def remove_encoding_dec(temp_filename, output_filename):
    with open(temp_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            if line.strip() == '''<?xml version='1.0' encoding='ASCII'?>''':
                output_file.write('<?xml version="1.0"?>\n')
            else:
                output_file.write(line)
    remove(temp_filename)