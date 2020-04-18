m = str(input("enter month: "))

if m=="february":
    print("28 or 29 days")
elif m in ("january", "march", "may", "july", "august", "october", "december"):
    print("31 days")
elif m in ("april", "june", "september", "november"):
    print("30 days")
