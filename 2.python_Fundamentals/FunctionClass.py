def greet():
    print("Hello.")

# hello = greet
# hello()  These two lines and below GREET() will do the same thing
greet()

avg = lambda seq: sum(seq) / len(seq) # we can directly declase into the operations LINE 34 like this "average":lambda seq: sum(seq) / len(seq),
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

students = [
    {"name":"Ashok","grade":(67,90,95,100)},
    {"name":"Bob","grade":(56,78,80,90)},
    {"name":"Anne","grade":(98,90,80,99)},
    {"name":"Kumar","grade":(100,100,95,100)}
]

for student in students:
    name = student["name"]
    grades = student["grade"]

    print(f"student: {name}")
    operation = input("Enter 'average', 'Total', 'top': ")

    # if operation == "average":
    #     print(avg(grades))
    # elif operation == "total":
    #     print(total(grades))
    # elif operation == "top":
    #     print(top(grades)) we can simply this code using DICTIONARY

operations = {
        "average":avg,
        "total":total,
        "top":top
    }

operation_function = operations(operation)
print(operation_function(grades))
