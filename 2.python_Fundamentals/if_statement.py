friend = "Ashok"
user_name = input("Enter your name: ")
print(bool(user_name)) # if user not enter any thing it print false.
if user_name == friend: # if statement must ends with colen
    print("Hello, friend!") # indentation is important in python 4 spaces or 1 tab space is mandatory in python, BEGINNERS MAKES MISTAKES IN PYTHON
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