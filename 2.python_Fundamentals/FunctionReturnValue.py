cars = [
    {"maker": "Ford","model": "Fiesta","mileage": 23000,"fuel_consumed": 460},
    {"maker": "Toyota","model": "Camry","mileage":17000,"fuel_consumed": 350},
    {"maker": "Mazda","model": "MX-5","mileage": 49000,"fuel_consumed": 900},
    {"maker": "Mini","model": "Cooper","mileage": 31000,"fuel_consumed": 235}
    ]


def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg


def calculate_name(car):
    name = f"{car['maker']} {car['model']}"
    return name

def calculate(car):
    mpg = calculate_mpg(car)
    name = calculate_name(car)
    print(f"{name} does {mpg} miles per gallon.")


for car in cars:
    calculate(car) # mpg = calculate(car)
    #print(calculate(car)) it print None to each execution


def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"
    else:
        return x / y

print(divide(10,2))
print(divide(6,0))