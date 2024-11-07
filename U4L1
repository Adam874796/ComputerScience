import math

limit = input("What is the upper limit: ")
limit = int(limit)

for a in range (3, (limit+1)):
    SqOne = math.pow(a, 2)
    if SqOne % 4 == 0:
        temp = SqOne / 4
        b = int(temp-1)
        c = int(temp+1)
        print("(%d %d %d)" % (a, b, c))
    if a % 2 != 0:
        ForNow = int(a / 2)
        b = ForNow * (a + 1)
        c = (ForNow * (a + 1)) + 1
        print("(%d %d %d)" % (a, b, c))
