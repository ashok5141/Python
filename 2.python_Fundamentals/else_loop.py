'''cars = ["ok", "ok", "faulty", "ok", "ok"]
for status in cars:
    if status == "faulty":
        print("Skippeing the car to shipping")
        all_successful = False
        break # we can use brake statement
    print(f"This car is {status}.")
    print("Shipping to new customer!.")

if all_successful:
    print("All cars built in successful. No faulty cars!")'''

cars = ["ok", "ok", "ok", "ok"]
for status in cars:
    if status == "faulty":
        print("Skippeing the car to shipping")
        break # we can use brake statement
    print(f"This car is {status}.")
    print("Shipping to new customer!.")
else:
    print("All cars built in successful. No faulty cars!")