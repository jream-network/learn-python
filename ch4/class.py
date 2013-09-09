# Classes OOP
# Method/Function ~ Same Thing
class Person:

    name = None
    age = None

    def name(self, n):
        self.name = n

    def age(self, a):
        self.age = a

    def get(self):
        return (self.name, self.age)

p1 = Person()
p1.name('Teddy')
p1.age(25)

print p1.get()

p2 = Person()
p2.name('Betty')
p2.age(13)

print p2.get()