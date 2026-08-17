students =  ["syed","abdullah","muahammed","ali","hammad"]
students [0] = "syed_ibrahim"
last_student = students.pop()
student_add = students.append("hamdan")
print(len(students))
print(students)

numbers = [1,49,27,44,22,10,5,4,6,8,]

for n in numbers :
    if n % 2 == 0 :
        print(n,"is even")
    else:
        print(n,"is odd")