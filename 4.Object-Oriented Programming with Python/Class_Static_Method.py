class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def avarage(self):
        return sum(self.marks) / len(self.marks)
    
ash = Student('Ashok', 'ULL')
ash.marks.append(50)
ash.marks.append(50)
print(ash.avarage())    
print(ash.name)

class Foo:
    @classmethod  # 
    def hi(cls):
        print("Class methods print the class name :",cls.__name__)

my_object = Foo()
my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print("Static methods don't take parameters")

another_object = Bar()
another_object.hi()