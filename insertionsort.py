def insertionSort(list):
  for index in range(1, len(list)):
    currentvalue = list[index]
    position = index
    print(list)

    while position>0 and list[position-1] > currentvalue:
      list[position] = list[position-1]
      position = position - 1

    list[position] = currentvalue

list = [55, 41, 190, 2, 10, 56, 28, 100, 9]
insertionSort(list)
print(list)
