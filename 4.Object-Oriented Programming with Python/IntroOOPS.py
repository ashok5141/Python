my_student = {
    'name' : 'Ashok',
    'grades' : [70,88,90,99],
    'average' : None
}

def average_grade(student):
        return sum(student['grades']) / len(student['grades'])

print(average_grade(my_student))


class Student:
        def __init__(self, new_name, new_grades): #dunder function double Underscore
                self.name = new_name
                self.grades = new_grades

        def average(self):
                return sum(self.grades) / len(self.grades)
        

student_one = Student('Ashok',[70,88,90,99])
print(student_one.name)
print(student_one.average())
print(Student.average(student_one))

def average(student):
       return sum(student.grades) / len(student.grades)
print(average(student_one))





# # Define a Movie class that has two properties: name and director
# class Movie:
#     def __init__(self, new_name, new_director):
#         self.name = new_name
#         self.director = new_director

# # You should be able to create Movie objects like this one:
# my_movie = Movie('The Matrix', 'Wachowski')

# # Exercise
# # We've already defined a movie class like this:
# class Movie:
#     def __init__(self, new_name, new_director):
#         self.name = new_name
#         self.director = new_director
 
#     # let's try to add a method `print_info()` here:
#     def print_info(self):
#         print(f"<<{self.name}>> by {self.director}")
 
# # You only need to finish the method, we will take care of the object creation and call your method for you!