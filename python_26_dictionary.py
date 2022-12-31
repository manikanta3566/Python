students = {"1": "john", "2": "paul", "3": "amith", "4": "jim", "5": "arnould"}

print(students)
print(students.get("1"))
print(students.keys())
print(students.values())

for key in students.keys():
  print(f"the student key is {key} and the value is {students.get(key)}")

print(students.items())

for key, value in students.items():
  print(f" the key is {key} and value is {value}")
