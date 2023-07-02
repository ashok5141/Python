currencies = 0.8, 1.2
usd, eur = currencies

friends = [("Ashok",27),("Bob",17),("Anne",7),("Kumar",0)]
for name, age in friends:
    print(f"{name} is {age} years old.")


'''
All are identical cases
for name, age in friends:
    name , age = friend
    name = friend[0]
    age = friend[1]
        print(f"{name} is {age} years old.")
'''
