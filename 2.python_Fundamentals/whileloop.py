is_learning = True
#while is_learning:
 #   print("You're learning")
  #  is_learning = input("Are you still learning ?")

while is_learning:
    print("You're learning!")
    user_input = input("Are you still learning ( yes / no )?")
    is_learning = user_input == "yes"
print("You stopped Learning !")
