def bubble_sort(a):
    for p in range(len(a)-1,0,-1):
        for i in range(p):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
    return a
input_list=[9,3,3,4,2,1,]
print(bubble_sort(input_list))