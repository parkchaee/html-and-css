#합 구하는 속도 비교
import time
def sum_n(n):
    s=0
    for i in range(1,n+1):
        #i를 더하는 거니까 0,n으로 범위를 잡으면 안됨 
        s+=i
    return s
print(sum_n(10))
def sum_n2(n):
    return n*(n+1)//2 #//는 몫, %는 나머지
print(sum_n2(10))
start=time.time() #시작시간
print(sum_n(1000000))
print(time.time()-start) #경과 시간=현재시간-처음 시간
start=time.time()
print(sum_n2(100000))
print(time.time()-start) 