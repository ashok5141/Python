class Student:
    def __init__(self,name):
        self.name = name

Movies = ['Ashok', 'Bob']
print(f"Length of ",len(Movies))


class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def __getitem__(self, i):
        return self.cars[i]
    def __repr__(self):#more code oriented
        return f'<Garage {self.cars}>'
    def __str__(self):#more user oriented
        return f'<Garage with {len(self)}>'

ford = Garage()
ford.cars.append('Focus') # assigning value in difffent way PREVIOUSLY assigned using ford = Garage('Focus') now we are using append
ford.cars.append('Fiesta')
print(ford.cars)
print(len(ford))
print("Printing Index : ",ford[0])
print(f" - ",ford)


for car in ford:
    print(car)
