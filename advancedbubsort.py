import random

def number():
    numinput = int(input("How many numbers?"))
    for i in range (0, numinput):
        num = random.randint(1,100)
        myarray.append(num)

def bubblesort(asc):
    temp=0
    for i in range (0,len(asc)):
        for l in range (0,len(asc)-1):
            if asc[l]>asc[l+1]:
                temp=asc[l+1]
                asc[l+1]=asc[l]
                asc[l]=temp
    print(asc)

def bubblesortdesc(desc):
    temp=0
    for i in range (0,len(desc)):
        for l in range (0,len(desc)-1):
            if desc[l]<desc[l+1]:
                temp=desc[l]
                desc[l]=desc[l+1]
                desc[l+1]=temp
    print(desc)

myarray = []
number()

which = input("ascending or descending? ")

while which == "ascending" or which == "descending":
    if which == "ascending":
        bubblesort(myarray)
        break
    elif which == "descending": 
        bubblesortdesc(myarray)
        break
