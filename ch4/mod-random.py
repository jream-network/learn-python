import random

random.seed()
print random.randint(10, 20)
print random.randrange(10)

print random.uniform(1, 10)

# For 0.0 to 1
print random.random()

print random.choice('12345ABCDEF')
item = ['Dog', 'Cat', 'Fish', 'Horse']

random.shuffle(item)
print item

print random.sample(item, 2)