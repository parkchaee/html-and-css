#리스트에서 특정 숫자 위치 찾기
#입력:리스트 a,찾는 값 x
#출력:찾으면 그 값의 위치, 찾지 못하면 -1 
def search_list(a,x):
    n=len(a) #입력 크기 n
    for i in range(0,n): #리스트 a 의 모든 값을 차례로 
        if x==a[i]: #x값과 비교
            return i #같으면 위치 
    return -1 #끝까지 비교후 없으면 -1
v=[1,2,6,3,4,5,6] 
print(search_list(v,1)) #순서상-1=위치번호로 출력
print(search_list(v,6)) #처음 나온 위치만 출력
print(search_list(v,900)) #-1 (없으면)