p = "12345"
a = 5

while a > 0:
    x = input("Password: ")

    if x == p:
        print("Access granted!")
        break
    else:
        a -= 1
        print("Wrong! Left:", a)

if a == 0:
    print("Authorities alerted!")