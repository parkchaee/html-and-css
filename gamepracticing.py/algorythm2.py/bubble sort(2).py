#리스트 만드는 방법의 속도 비교
#버블 알고리즘 활용 
#sample, randrange의 차이 
import random
import time
def generate_list(n):
    a=[]
    for i in range(0,n):
        a.append(random.randrange(0,1000))
    return a
def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
array1=random.sample(range(1,1000),100)
array2=generate_list(100)
print(array1)
start=time.time()
print(bubbleSort(array1))
print("time:", time.time()-start)
print(array2)
start=time.time()
print(bubbleSort(array2))
print("time:",time.time()-start)