short_tuple = "Ashok","Bob"
a_bit_clearer = ("Ashok","Bob")
tuple_in_clearer = ["Ashok","Bob"] # not valid because we seen in the list
valid_tuple_clearer = [("Ashok","Bob")] # valid one because, first you check bracket(tuple) and then outside list 
#a_bit_clearer.append("Anne") # can not add new friend in the tuple, like list. make error MAKING IN COMMENT
a_bit_clearer = a_bit_clearer + ("Anne",) # if you use single value and must put comma
print(a_bit_clearer)

"""
List are used in whn you need modification like add or remove from the list,
Tuple used for fixed purpose 
Recommneded use Tuple overthe list
"""