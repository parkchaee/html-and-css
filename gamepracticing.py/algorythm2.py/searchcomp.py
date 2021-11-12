import random
import time
def generate_list(list,n):
    for i in range(0,n):
        list.append(random.randrange(0,100))
def binary_search(a,x):
    start=0
    end=len(a)-1
    while start<=end:
        mid=(start+end)//2
        if x==a[mid]:
            return mid
        elif x>a[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1
def linear_search(a,x):
    n=len(a)
    for i in range(0,n):
        if x==a[i]:
            return i
    return -1
v=[]
start=time.time()
generate_list(v,1000000)
print("generate list time:",time.time()-start)
start=time.time()
v.sort()
print("sort time :",time.time()-start)
print(linear_search(v,15))
print(linear_search(v,45))
print(linear_search(v,200))
print("linear search time:",time.time()-start)
start=time.time()
print(binary_search(v,15))
print(binary_search(v,45))
print(binary_search(v,200))
print("binary search time:",time.time()-start)