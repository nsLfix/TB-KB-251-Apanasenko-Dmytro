student = {
    "name": "Vanya",
    "age": 19,
    "city": "Kiev"
}
print("word :", student)

print("1.(keys):", list(student.keys()))

print("2.(values):", list(student.values()))

print("3.(items):", list(student.items()))

student.update({"age": 20, "group": "KB-251"})
print("4.update({'age': 20, 'group': 'KB-251'}):", student)

del student["city"]
print("5.del student['city']:", student)

student.clear()
print("6.clear():", student)