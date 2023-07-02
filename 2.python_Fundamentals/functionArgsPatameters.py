# car = {
#     "maker": "Ford",
#     "model": "Fiesta",
#     "mileage": 23000,
#     "fuel_consumed": 460
# }
# mpg = car["mileage"] / car["fuel_consumed"]
# name = f"{car['maker']} {car['model']}"
# print(f"{name} does {mpg} miles per gallon.")

#Argument: value you pass in to the function.
#Parameter: variable that accepts a value inside the function.
#variable inside call a function like def function(variable)

# def calculate_mpg():
#     car = {
#         "maker": "Ford",
#         "model": "Fiesta",
#         "mileage": 23000,
#         "fuel_consumed": 460
#     }
#     mpg = car["mileage"] / car["fuel_consumed"]
#     name = f"{car['maker']} {car['model']}"
#     print(f"{name} does {mpg} miles per gallon.")
# calculate_mpg()

def calculate_mpg(car):
    # car = {
    #     "maker": "Ford",
    #     "model": "Fiesta",
    #     "mileage": 23000,
    #     "fuel_consumed": 460
    # }
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['maker']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")
calculate_mpg({
        "maker": "Ford",
        "model": "Fiesta",
        "mileage": 23000,
        "fuel_consumed": 460
    })

cars = [
    {"maker": "Ford","model": "Fiesta","mileage": 23000,"fuel_consumed": 460},
    {"maker": "Toyota","model": "Camry","mileage":17000,"fuel_consumed": 350},
    {"maker": "Mazda","model": "MX-5","mileage": 49000,"fuel_consumed": 900},
    {"maker": "Mini","model": "Cooper","mileage": 31000,"fuel_consumed": 235}
    ]

def calculate(cars):
    mpg = cars["mileage"] / cars["fuel_consumed"]
    name = f"{cars['maker']} {cars['model']}"
    print(f"{name} does {mpg} miles per gallon.")
calculate(cars[1]) # PRINTS one car based parameter you specified
for car in cars:
    calculate(car)

