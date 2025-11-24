days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
        7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

m = int(input("Month (1-12): "))

if m == 2:
    if input("Leap year? (yes/no): ") == "yes":
        print("29 days")
    else:
        print("28 days")
elif m in days:
    print(days[m], "days")
else:
    print("Invalid month")