#<순차>
#리스트에서 특정 숫자 위치 찾기
#입력: 리스트 a, 찾는 값 x
#출력: 찾으면 그 값의 위치, 찾지 못하면 -1
#!!특정값이 있는 모든 위치 찾기 !!
def search_list(a,x):
    alist=[]
    n=len(a)
    for i in range(0,n):
        if x==a[i]:
            alist.append(i)
    return alist #alist의 경우 모두 추가한 이후 반환해야하므로
v=[17,92,18,33,58,7,33,42]
print(search_list(v,40))
print(search_list(v,33))
print(search_list(v,900))