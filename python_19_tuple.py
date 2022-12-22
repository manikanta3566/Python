tup = (1, 7, 55, 34, 21, 2, 45, "john", True)

print(type(tup))
print(tup)
print(tup[0])
print(tup[3])
print(tup[0:4])
print(tup[-4:-2])

if "john" in tup:
  print("yes")
else:
  print("NO")

tup2 = (1)
print(type(tup2))

tup3 = (1, )
print(type(tup3))
