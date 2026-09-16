student_1 = {"name": "syed",
              "age": 20, 
             "roll_no": 101,
             "class":12}
print(student_1 )
print()
print(student_1.get("name"))

for val in student_1.values():
    print(val, end="; ")