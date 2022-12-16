# break
i = 1
while (i < 11):
  if (i == 11):
    break
  print("5*", i, "=", 5 * i)
  i = i + 1

# continue
j = 1
while (j <= 10):
  if (j % 2 != 0):
    j = j + 1
    continue
  print(j)
  j = j + 1

for k in range(1, 11):
  if (k % 2 != 0):
    continue
  print(k)
