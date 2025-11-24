names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search = input("Enter name to search: ")
if search in names:
    print(search, "found!")
else:
    print(search,"not found.")
    