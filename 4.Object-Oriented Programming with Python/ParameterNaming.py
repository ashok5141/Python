class Movie:
    def __init__(self,name,year):
        self.name = name     #name is VARIABLE or PROPERTY creating inside the self, that variable exits in name variable in scope
        self.year = year

# Matrix = Movie('The Matrix',1996) we can do this as well
# print(Matrix.year)

print(Movie('The Matrix',1996).name)