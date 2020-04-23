import math

a = int(input("enter A value: "))
b = int(input("enter B value: "))
c = int(input("enter C value: "))

d = b ** 2 - 4 * a * c

if d < 0:
    print("number of real roots: 0")
elif d==0:
    root = (-b + math.sqrt(d)) / (2 * a)
    print("number of real roots: 1")
    print("x= " + str(root))
elif d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("number of real roots: 2")
    print("x= " + str(root1) + " and " + "x= " + str(root2))