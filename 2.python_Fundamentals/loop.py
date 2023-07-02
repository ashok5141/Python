friends = ["Ashok", "Bob", "Anne"]
for friend in friends:
    print(friend)
numbers = [0,1,2,3,4,5,6,7,8,9]
for index in numbers:
    print("Hello World!")
for index in range(2,20,3):
    print(index)
for index in range(10):
    print(index)

students = [
    {"name": "Ashok", "grade": 90},
    {"name": "Bob", "grade": 70},
    {"name": "Anne", "grade": 60},
    {"name": "Kumar", "grade": 50}
]
print(students)
for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}.")