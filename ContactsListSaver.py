contacts = {}

while True:
    name = input("Enter name: ")
    number = input("Enter number: ")
    contacts[name] = number

    more = input("Add more? (y/n): ")
    if more.lower() != 'y':
        break

print("\nContact List:")
for name, number in contacts.items():
    print(f"{name} : {number}")
