def search_list(a,x):
    alist=[]
    n=len(a)
    for i in range(0,n):
        if x==a[i]:
            alist.append(i)
    return alist
v=[17,92,18,33,58,7,33,42]
print(search_list(v,40))
print(search_list(v,33))
print(search_list(v,900))