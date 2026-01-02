def binarySearchIndexAndComparisons(L,k):
    n=0
    l=0
    r=len(L)-1
    while r>l:
        mid = (r+l)//2
        n+=1
        if(L[mid]>k):
            r=mid-1
        elif(L[mid]<k):
            l=mid+1
        elif(L[mid]==k):
            return (True,n)
            
    return (False,n)

print(binarySearchIndexAndComparisons([2, 6, 8, 11, 17, 23, 33, 44, 46, 50, 65, 11],11))