# Sorting Algorithms
# BubbleSort, SelectionSort, InsertionSort
def Selectionsort(num):
    h=0
    for i in range(len(num)):
        max=i
        for j in range(max+1,len(num)):
            if num[j]<num[max]:
                max=j
                h+=1
        num[i],num[max]=num[max],num[i]
    print(h)
def Bubblesort(number):
    k=0
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            if number[j]<number[i]:
                number[j],number[i]=number[i],number[j]
                k+=1
    print(k)
def Insertionsort(num):
    t=0
    for i in range(1,len(num)):
        a=num[i]
        j=i-1
        while j>=0 and a<num[j]:
            num[j+1]=num[j]
            j-=1
        num[j+1]=a
    print(t)
ls=[0,9,3,4,5,2,7,8,1]
Insertionsort(ls)
print(ls)