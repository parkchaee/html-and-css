import time 
def sum_n(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
def sum2(n):
    return n*(n+1)/2
start=time.time()
print(sum_n(10),time.time()-start)

def sum1(n):
    s=0
    for i in range(1,n+1):
        s+=i
