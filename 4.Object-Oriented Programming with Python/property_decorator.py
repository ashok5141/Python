class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
class WorkingStudent(Student):
    def __init__(self, name, school,salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 20
    
ash = WorkingStudent('Ashok','ULL',8)
print(ash.weekly_salary) # Not using () because not passing any object, 
#just calling self function, if it's take any other object other then self you need to mention() 
