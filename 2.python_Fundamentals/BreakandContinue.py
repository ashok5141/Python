cars = ["ok", "ok", "faulty", "ok", "ok"]
for status in cars:
    print(f"This car is {status}.")
print("-----------------Next Statement-----------------")
'''for status in cars:
    if status == "faulty":
        print("Stopping the production checking the faulty car!")
        break
    print(f"This car is {status}.")
    print("The car condition okay, shipping the car!")'''

for status in cars:
    if status == "faulty":
        print("Skippeing the car to shipping")
        continue # we can use brake statement
    print(f"This car is {status}.")
    print("Shipping to production!.")

for i in range(20):
    print(i)
kids_ages = (3,6,9,12)
for age in kids_ages:
    print(f"I have a {age} year old kid.")