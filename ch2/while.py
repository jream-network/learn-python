import time

count = 1
while True:

    print "Hello #{0}".format(count)
    count += 1

    if count >= 16:
        print "End of Loop!"
        break

    time.sleep(.5)