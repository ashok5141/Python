friends_ages = {"Ashok":27, "Bob":20, "Anne":10}
print(friends_ages["Ashok"]) #it print age of user

friends_ages["Kumar"] = 1 # add new friends to the dictonary
friends_ages["Ashok"] = 30 # update the values
print(friends_ages) # it will print updated statement with updated values

friends = (
    {"name": "Ashok", "age":27},
    {"name": "Bob", "age":17},
    {"name": "Anne", "age":7}
    )
print(friends)
print(friends[2]["name"])
friend = friends[0]
print(friend["name"])

frnds = [("Ashok",27),("Bob",17),("Anne",7)]
frnds_age = dict(frnds)
print(frnds)