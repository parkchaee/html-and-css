arr=[3,0,1,8,7,2,5,4,6,9]
print(arr)
n=len(arr)
for i in range(n-1): #리스트 길이동안 반복
    for j in range(n-1-i): #0자리 혼자 비교할 필요 x 이므로 
        if arr[j]<arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
    print(arr)
print(arr)

