# def divide(x,y):
#     return x / y   same funtion define in lambda

divide = lambda x,y : x / y #first lambda function
print(divide(15,3))

(lambda x,y: x / y) (6,2) # it will create function and if realizes no name it immediatly distry it
print((lambda x,y: x / y) (8,2)) # it print like first lambda function

# def avarage(sequence):
#     return sum(sequence) / len(sequence) converting in lambda function

avarage = lambda sequence: sum(sequence) / len(sequence)  # their are  better secnarios to use not recommended to store values in OBJECT in AVARAGE

students = [
    {"name":"Ashok","grade":(67,90,95,100)},
    {"name":"Bob","grade":(56,78,80,90)},
    {"name":"Anne","grade":(98,90,80,99)},
    {"name":"Kumar","grade":(100,100,95,100)}
]

for student in students:
    print(avarage(student["grade"]))

