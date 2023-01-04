# try:
#   i = int(input("enter the index : "))
#   list = [10, 2, 23, 6, 89]
#   print(list[i])
# except:
#   print("exception caught")
# finally:
#   print("connection closed")


def demo():
  try:
    i = int(input("enter the index : "))
    list = [10, 2, 23, 6, 89]
    print(list[i])
    return 1
  except:
    print("exception caught")
    return 0
  finally:
    print("connection closed")


print(demo())
