#name = raw_input("Whats your name?\n")
#print "Hello {0}".format(name)

while True:

    try:
        age = int(raw_input("Whats your age?"))
        print "In 10 years you will be {0}".format(age + 10)

    except ValueError:
        print "Error: You must enter a digit"
        continue


