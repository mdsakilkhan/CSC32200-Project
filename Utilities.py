from lxml.objectify import ElementMaker

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