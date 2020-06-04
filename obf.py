import sys, time, string, random

while True:
    arrl = list(string.ascii_lowercase)
    a, b, c, d, e = arrl[random.randint(0, len(arrl) - 1)], arrl[random.randint(0, len(arrl) - 1)], arrl[random.randint(0, len(arrl) - 1)], arrl[random.randint(0, len(arrl) - 1)], arrl[random.randint(0, len(arrl) - 1)]
    sys.stdout.write("\r{0}{1}{2}{3}{4}".format(a, b, c, d, e))
    time.sleep(.04)