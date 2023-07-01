art_friends ={"Ashok","Bob"}
art_friends.add("Aane")
print(art_friends) #set print the data dis - order there is no pacticualr order format
art_friends.remove("Aane")
print(art_friends)

cs_friends = {"Ashok","Bob","Anne","yesh"}
info_friends = {"yesh","Kumar"}
cs_but_not_info = cs_friends.difference(info_friends) # it will print only in CS team not both
info_but_not_cs = info_friends.difference(cs_friends) # it will print only in info team not both
not_in_both = info_friends.symmetric_difference(cs_friends) # it will remove both department common friend
both_cs_info = cs_friends.intersection(info_friends) # it will print common friend in both departments
all_friends = cs_friends.union(info_friends) #it will all friends 
print(cs_but_not_info)
print(info_but_not_cs)
print(not_in_both)
print(both_cs_info)
print(all_friends)