ages = [27,17,7,0,2,4,6]
odds = [age for age in ages if age % 2 == 1]
print(odds)

friends = ["Ashok","Bob","Anne","kumar","Ram"]
guests = ["Anne","kumar","Mathaew"]
friends_lower = [f.lower() for f in friends]

present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
]
print(present_friends)