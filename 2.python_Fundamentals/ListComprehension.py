numbers = [0,1,2,3,4]
# doubled_numbers = []

# for number in numbers:
#     doubled_numbers.append(number * 2)

doubled_numbers = [number * 2 for number in numbers] # the above commented code and this line will do same thing
print(doubled_numbers)

friend_ages = [27,17,7,0,1]
age_string = [f"My friend is {age} years old!" for age in friend_ages] # here age friend name can't able print same time
print(age_string)

friend = input("Enter your friend name: ")
friends = ["Ashok","Bob","Anne","Kumar","Ram"]
friend_lower = [name.lower() for name in friends]
#if friend in friend_lower USER might enter lower or upper cases so we can convert both user input and list friends lower case letters and then comapre
if friend.lower() in friend_lower:
    #friend_titlecased = friend.title()
    print(f"{friend} is one of your friends.") #print(f"{friend.title()} is one of your friends.") PRINTS LIKE THIS Anne is one of your friends.
else:
    print(f"{friend} is not in your list")