list = [4, 2, 89, 0, 2, 34, 6, 78, 4, 4]

list.append(100)
list.sort()
list.reverse()
print(list)
print(list.index(89))
print(list.count(4))
list.insert(0, 3)
print(list)
list2 = list.copy()
list2.append("list2")
print(list2)
list2.extend(list)
print(list2)
