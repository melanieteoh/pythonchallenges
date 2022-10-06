pyramid = int(input("Enter a number:"))

number = 1
for i in range(1, pyramid + 1):
  print(number * "p")
  number = number + 1
