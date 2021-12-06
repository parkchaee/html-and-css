#리스트에서 특정 숫자 위치 찾기
#이분 탐색 
def binary_search(a,x):
    start=0
    end=len(a)-1
    step=0
    
    while start<=end:
        mid=(start+end)//2 #중앙값
        #//:몫 %:나머지 
        step+=1
        print("%d 단계, mid =%d,value=%d"%(step,mid,a[mid]))
        if x==a[mid]: #중앙값과 일치한다면 
            return mid #중앙값 반환 
        elif x>a[mid]: #중앙값보다 크다면 
            start=mid+1 #시작을 mid+1부터 / start =0부터 시작임 
        else:
            end=mid-1
    return -1
d=[1,4,9,16,25,36,49,64,81]
print(binary_search(d,36))
print(binary_search(d,50))
