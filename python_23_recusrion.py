def recusrion(num):
  if (num == 1 or num == 0):
    return 1
  return num * recusrion(num - 1)

  # 3=>3*2*1=6
  # 3*recusrion(3-1)
  # 3*2*recurison(2-1)
  #3*2*1


print(recusrion(3))
