# string
# list
# tuple

for i in "abcd":
    pass
    # print i

# Lists are Mutable
for j in [1,2,3]:
    pass
    # print j

# Tuples are not Mutable
for k in (1,2,3):
    pass
    # print k

db = {
    'server': 'localhost',
    'user': 'john',
    'pass': 'smith'
}

print db.keys()
print db.values()
print db.items()[0][1]

n = (1,2,3)
n[1] = 33
print n[1]
