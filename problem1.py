"""Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""

def bsort(L):
    n = len(L)
    for i in range(n,0,-1):
        for j in range(n-1):
            if(L[j]>L[j+1]):
                L[j],L[j+1]=L[j+1],L[j]
        


def triplet1(L):
    # bsort(L)
    n=len(L)
    li=[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(L[i]+L[j]+L[k]==0):
                    if([L[i],L[j],L[k]] not in li):
                        li.append(bsort([L[i],L[j],L[k]]))
    return li


print(triplet1(([-1,0,1,2,-1,-4])))
