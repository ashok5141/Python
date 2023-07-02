friends = [("Ashok",27),("Bob",17),("Anne",7),("Kumar",0)]
for name in friends:
    print(name)

friends = {"Ashok":27,"Bob":17,"Anne":7,"Kumar":0}
for name in friends:
    print(name)

friends = {"Ashok":27,"Bob":17,"Anne":7,"Kumar":0}
for age in friends.values():
    print(age)

friends = {"Ashok":27,"Bob":17,"Anne":7,"Kumar":0}
for name in friends:
    print(f"{name} is {age} years old !")

friends = {"Ashok":27,"Bob":17,"Anne":7,"Kumar":0}
for name, age in friends.items():
    print(f"{name} is {age} years old !")