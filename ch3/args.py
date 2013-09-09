# Arbitrary Arguments
def color(*args):
    for i in args:
        print i

def moon(**kwargs):
    for key, value in kwargs.iteritems():
        print key, value

def person(name, *args, **kwargs):
    print name
    for i in args:
        print i
    for key, value in kwargs.iteritems():
        print key, value

color(1, 2, 3, 4, 5)
moon(name = "Ben", age = "25")
person("Jimmy", 1,2,3, gender = "Male")
