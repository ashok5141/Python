friends = ["Ashok","Bob","Anne","kumar","Ram"]
# time_since_seen = [27,17,7,0,1]

# counter = 0
# for friend in friends:
#     print(counter)
#     print(friend)
#     counter = counter + 1

for counter, friend in enumerate(friends, start=1): # Optionally choose where to start number by default 0, if wish set a number in start perameter
    print(counter)
    print(friend)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))
print(list(zip([0,1,2,3,4,5], friends))) # do the same thing with enumarate