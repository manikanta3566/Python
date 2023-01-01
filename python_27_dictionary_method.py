
emp1 = {1: "john", 2: "mike"}
emp2 = {3: "jim", 4: "charles"}

# emp1.clear()
emp1.update(emp2)
# del emp1[3]
print(emp1)
# del emp1

emp1.pop(1)
emp1.popitem()
print(emp1)
