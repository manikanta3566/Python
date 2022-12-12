num=10
#if-else
if(num<15):
  print("if ",num)
else:
  print("else ",num)

#if -elif -else
if(num>10):
  print("if ",num)
elif(num<=10):
  print("elif ",num)
else:
  print("else ",num)

#nested if elif  
if(num<15):
  if(num<=10):
    print("if ",num)
  else:
    print("else ",num)
elif(num>15):
  print("elif ",num)
else:
  print("else ",num)
