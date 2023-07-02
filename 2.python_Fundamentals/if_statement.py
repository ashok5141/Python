friend = "Ashok"
user_name = input("Enter your name: ")
print(bool(user_name)) # if user not enter any thing it print false.
if user_name == friend:
    print("Hello, friend!")
else:
    print("Bye, Starnger!")


friends = ["Bob", "Anne", "Kumar"]
family = ["Ram", "Kumar"]
user_data = input("Enetr your sweet name again :")
if user_data in friends:
    print("Your my best friend")
elif user_data in family:
    print("Your my family")
else:
    print("I don't recognize you, sorry!")