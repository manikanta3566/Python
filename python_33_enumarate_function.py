#without enumaration function
numbers=[1,55,3,22,44,89,77,55,88]
i=0
for num in numbers:
  print(num)
  if(i==1):
    print("done")
  i=i+1

#with enumaration function
for index,num in enumerate(numbers):
  print(index,num)
  if(index==1):
    print("done")
