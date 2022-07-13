# Linear Search
def Linear_Search(array,son):
    for i in range(len(array)):
        if array[i]==son:
            return i
    return "Topilmadi"
def Binary_Search1(array,son,l,r):
    while l<=r:
        mid=l+(r-l)//2
        if array[mid]==son:
            return mid
        elif array[mid]<son:
            l=mid+1
        else:
            r=mid-1
    return "Topilmadi"
def Binary_Search2(array,son,l,r):
    if r>=l:
        mid=l+(r-l)//2
        if array[mid]==son:
          return mid
        elif array[mid]<son:
          return Binary_Search2(array,son,mid+1,r)
        else:
         return Binary_Search2(array,son,l,mid-1)
    else:
        return "Topilmadi"
ls=[1,2,3,4,5,5,5]
#print(Linear_Search(ls,5))
print(Binary_Search2(ls,5,0,len(ls)-1))