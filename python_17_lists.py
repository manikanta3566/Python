color = ["red", "white", "blue", "pink", "green"]

print(color)
print(type(color))
print(color[0])
print(color[1])

print(color[0:3])
print(color[:2])
print(color[-4:-3])  #len(color)-4:len(color)-3
print(color[len(color) - 4:len(color) - 3])

if "red" in color:
  print("yes")
else:
  print("no")

print(color[0:5])
print(color[0:5:2])

list1 = [i * 2 for i in range(0, 20)]
print(list1)

list2 = [i for i in range(0, 21) if i % 2 == 0]
print(list2)
