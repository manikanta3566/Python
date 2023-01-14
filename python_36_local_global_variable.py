x = 10  #global variable


def demo():
  y = 9  #local variable
  global x  #changing global variable value by using global keyword
  x = 15
  print(x)
  print(y)


demo()
print(x)
