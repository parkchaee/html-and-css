print("온도변환")
print(" 1. 섭씨-->화씨")
print(" 2. 화씨-->섭씨")
select=int(input("번호를 선택하세요:"))
if select==1:
    c=int(input("섭씨 온도를 입력하세요:"))
    f=9/5*c+32
    print("섭씨",c,"도는 화씨",f,"도입니다")
elif select==2:
    f=int(input("화씨 온도를 입력하세요:"))
    c=5/9*(f-32)
    print("화씨",f,"도는 섭씨",c,"도입니다")
else:
    print("잘못 입력하였습니다")
