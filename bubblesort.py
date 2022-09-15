def BubbleSort(MyArray):
 PassCount = 1
 for n in range(UBound):
   Swapped = False
   for i in range(len(MyArray)-PassCount):
     if MyArray[i] > MyArray[i+1]:
       Swapped = True
       Temp = MyArray[i]
       MyArray[i] = MyArray[i+1]
       MyArray[i+1] = Temp
   if Swapped == False:
     break
   else:
     PassCount = PassCount + 1
  
 
MyArray = [15, 6, 7, 10, 24, 65, 33, 31, 19]
UBound = len(MyArray)+1
BubbleSort(MyArray)
print(MyArray)
