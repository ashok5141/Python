my_name = "Ashok"
your_name = input("Enter your name :") # taking data from user and printing statement
print(f"Hello {your_name}. My name is {my_name}")

age = input("Enter your age : ")
print(f"You have lived for {age * 12} months") #it printing string age 12 times
age_num = int(age) # the age_num useless because using only below state, use below example, directly convering interger
print(f"You have lived for {age_num * 12} months") # here we are converting the age variable into interger

age = int(input("Enter your age again :")) # python will execute inside bracket run first, after pressing enter it will conver into interger
print(f"You have lived for  {age * 12} months") #converting the user input into interger