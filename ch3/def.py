# Def means definition, or function

def name(a, b = None):
    if b != None:
        print b
    return "Welcome here, {0}".format(a)

hello = name("Jesse", "Extra Parameter")
print hello


