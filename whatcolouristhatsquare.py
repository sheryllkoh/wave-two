letter1 = ("a","c", "e", "g")
letter2 = ("b", "d", "f", "h")
num1 = (1, 3, 5, 7)
num2 = (2, 4, 6, 8)

letter = str(input("enter letter: "))
number = int(input("enter number: "))

if letter in letter1 and number in num1:
    print("square is black")
elif letter in letter1 and number in num2:
    print("sqaure is white")
elif letter in letter2 and number in num1:
    print("square is white")
elif letter in letter2 and number in num2:
    print("square is black")
    

