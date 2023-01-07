a = 10
b = 90
#normal if else statement
if (a > b):
  print("a is greater than b")
else:
  print("b is greater than a")

#short if else
print("a is greater than b") if a > b else print("b is greater than a")

print("a is greater than b") if a > b else print(
  "b is greater than a") if b > a else print("....")
