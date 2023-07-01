frined1 = "Ashok"
frined2 = "Ram" #If you crating multiple friend can't manage code
friends = ["Ashok","Bob","Anne"] # instead of creating multiple values use list
print("Second name",friends[2]) # in will access the 3 element because starting 0
print("Length of string ",len(friends)) # it will print length of the list

frind_age = [
    ["Ashok",20],
    ["Bob",10],
    ["Anne",1],
    ["Kumar",2],
    ["Ram",3]
    ]
print("print complete list",frind_age[1])
print("List with specific value :",frind_age[3][0])
print(frind_age)
frind_age.remove(["Ram",3])
print(frind_age)
