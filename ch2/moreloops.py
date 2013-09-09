# Nested List
ages = [2, 3, 4, [12, 13, 15]]
print ages

for age in ages:
    if type(age) is list:
        for a in age:
            print a
    else:
        print age

# Loop a String
for s in "ThisDay":
    print s

# Nested Dictionary
movies = {
    "Action": {
        "X-Men": "A",
        "Iron Man": "A",
    },
    "Romance": {
       "Titanic": "A+"
    },
    "Color": "Red"
}

# Keep track of displayed categories
displayed = []

for key, value in movies.iteritems():
    if type(value) is dict:
        for k, v in value.iteritems():
            if key not in displayed:
                print "Category: " + key
                print '---------'
                displayed.append(key)
            print k + ' is ' + v
    else:
        print key, value

