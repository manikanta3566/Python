def sum(a, b):
  sum = a + b
  print(sum)


sum(10, 20)


def printEmail(address, domain="@gmail.com"):
  email = address + domain
  print(email)


printEmail("john")


def addition(a, b=0):
  print(a + b)


addition(a=20)
addition(b=20, a=10)


def printNumbers(*numbers):
  for i in numbers:
    print(i)


printNumbers(1, 3, 4, 5, 6, 7, 8, 8)


def getSquareNumber(number):
  return number * number


squareNum = getSquareNumber(5)
print(squareNum)
