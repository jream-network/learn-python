person = {
    # Key: Value
    'first_name': 'Barney',
    'last_name': 'Rubble',
    'hobbies': [
        'swimming',
        'tennis'
    ],
    'details': {
        'age': 20,
        'location': 'Bedrock'
    }
}

print "My name is {0} {1}".format(
        person['first_name'],
        person['last_name'])

print person['hobbies']
print person['hobbies'][1]

print person['details']
print person['details']['age']
