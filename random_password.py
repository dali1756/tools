import random, sys, string
length = int(sys.argv[1])
print("".join(random.choices(string.ascii_lowercase + string.digits, k=length)))
