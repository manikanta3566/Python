def test():
  str = int(input("enter the number 0 or 1 "))
  if (str != 0 and str != 1):
    raise ValueError("please enter the value 0 or 1")
  else:
    print(str)


def demo():
  try:
    test()
  except ValueError:
    print("exception occured")


demo()
