my_string = "Hello, world!"
print(my_string)

another_with_quotes = 'He said "You are amazing!" yesterday'
print(another_with_quotes)

multiline = """Hello, world!

multiline commant print using in variable and 3 double codes"""
print(multiline)

age = 34
age = 35
age_as_str = str(age)
print("You are : " + age_as_str)
print(f"You are {age}")
print(f"You are {age}")  # in f string printed same age variable printed, use below format name to print diffrent variables

name = "Ashok"  # add strings together
greeting = "Hello, " + name
print(greeting)
ash_greet = "How are you, {}"
ashok_greeting = ash_greet.format(name)
print(ashok_greeting)

name = "Reddy"
#red_greet = ash_greet.format(name) # in f string printed twice in the above age case
print(ash_greet.format(name)) # reduced one line

description = "{} is {} years old."
print(description.format("Bob", 30)) # declaring the objects in print statement using format


description = "{} is {age} years old."
print(description.format("Bob", age=30))





