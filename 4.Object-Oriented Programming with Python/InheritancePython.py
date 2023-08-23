class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
#s1 = Student('Bob','UL',[80,80,80,100])
#Another Class below implementing the inheritance
# class WorkingStudent: 
#     def __init__(self, name, school, salary):
#         self.name = name
#         self.school = school
#         self.marks = []
#         self.salary = salary

    # def average(self):
    #     return sum(self.marks) / len(self.marks)
class WorkingStudent(Student):  # Inherting Student class to the WorkingStudent
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary =salary

    def weekly_salary(self):
        return self.salary * 20
    
ashok = WorkingStudent('Ashok', 'ULL', 8)
print(f"{ashok.name} is student at {ashok.school} he working as RA with funding {ashok.salary} per hour")
print(ashok.salary)
ashok.marks.append(57)
ashok.marks.append(99)
print(ashok.average())
print(ashok.weekly_salary())
