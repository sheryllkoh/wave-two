import random

g = "00"
g1 = "0"

n = [g, g1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

green = (g, g1)
black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)


n1 = random.choice(n)

print("the spin resulted in " + str(n1))
print("pay " + str(n1))

if n1 in black:
    print("pay black")
elif n1 in red:
    print("pay red")

if int(n1) > 0 and (n1%2==0):
    print("pay even")
elif int(n1) > 0:
    print("pay odd")

if int(n1) > 0 and n1 <= 18:
    print("pay 1 to 18")
elif int(n1) > 0:
    print("pay 19 to 36")   



