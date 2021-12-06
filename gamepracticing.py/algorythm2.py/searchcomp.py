#무작위로 리스트 생성
#이들을 이진 탐색, 순차 탐색으로 속도 비교 
import random
import time
def generate_list(list,n):
    for i in range(0,n): #for은 숫자 세는 용도 
        list.append(random.randrange(0,100))
        #무작위로 0~99 중에서 선택해 list로 만들기
#이진탐색 
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
def linear_search(a,x): #순차 탐색, alist(전체 출력)x
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