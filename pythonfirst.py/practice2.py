''' 코딩 동아리를 만들었다. 
월 4회 스터디를 하는데 3번은 온라인, 
1번은 오프라인으로 하기로 했다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는
프로그램 작성하기
1. 랜덤 날짜
2. 월별 날짜는 다름을 감안해 최소 일수은 28일 
이내
3. 매월 1~3일은 준비로 제외
오프라인 날짜는 매월 x일로 선정'''


#1
from random import*
x=randint(4,28)
print(x) 
#2
import random
x=int(random.randrange(4,29))
print("오프라인 날짜는 매월",x,"일로 선정")

# 긴문장 - """이 시작하는 문장부터 담김
sen3="""
나는 소년이고 
파이썬은 쉬워요
"""
print(sen3)

# 슬라이싱
jumin="090903-1234567"
print("성별:"+jumin[7]) #8번째 자리
print("연:"+jumin[:2]) #시작부터 2 직전까지
print("월:"+jumin[2:4])
print("d"+jumin[-7:-1]) 
# 이 경우 123456이 됨, -7자리에서 -1 전으로 
#똑같이 적용되기 때문
#끝까지 적용되는 걸로 하려면
print(jumin[-7:])

#대소문자로 작성
python="Python is Amazing"
print(python.lower()) 
print(python.upper())
print(python[0].isupper()) #boolean
print(len(python))
print(python.replace("Python", "Java"))

#index
index=python.index("n")
print(index)  #slicing처럼 똑같이 0으로 자리세기 시작
index=python.index("n",index+1)
print(index)

#find
print(python.find("n"))

#단 find는 없으면 -1을 반환
#index의 경우 error

#문자 수 세기
print(python.count("n"))

