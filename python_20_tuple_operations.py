tup1 = (1, 4, 6, 8, 0, 4, 34)

print(tup1)
#converting into list
list1 = list(tup1)
print(list1)
list1.append(True)
print(list1)

#converting into list to tuple
tuple2 = tuple(list1)
print(tuple2)

print(tuple2.count(34))
print(tuple2.index(4))
print(tuple2.index(6, 0, len(tuple2)))
print(tuple2[0:2])
