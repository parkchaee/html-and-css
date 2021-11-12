print(5)
print(-10)
print(3.14) #실수
#저장을 먼저 하고 실행 ctrl s + f5
print(5+3)
print(2*8) # 우선순위 연산 적용
print('풍선') 
print("z"*6) #==print("zzzzzz")
print(5>10) # boolean False or True
print(not True) # ==False
# 변수 지정- 애완동물 소개하기
name="연탄이"
animal="강이지"
age=4
hobby="산책"
is_adult=age>=1
print("우리 집의"+ animal+"는"+ name)
hobby="공놀이" # 변수 변경 가능
print(name+"는 "+str(age)+"살, "+hobby+"을 좋아함")
print(name,"는 ","어른일까요?", is_adult) # ,는 str 생략가능, 쉼표 추가됨
# 주석 
'''1.여러 문장
주석처리 
2. ctrl+/ 로 집합시켜주면 주석 & 해제 가능'''
#quiz 
station="사당"
print(station+"행 열차가 들어오고 있습니다.")
station="신도림"
print(station+"행 열차가 들어오고 있습니다.")
station="인천공항"
print(station+"행 열차가 들어오고 있습니다.")
# 연산
print(5%3) #나머지 구하기
print(10//2) #몫만 구하기
print(10>3) #boolean
#|==or, \는 \n할때
number=1
number +=2 # number=number+2
print(number)
print(abs(-5)) # 절댓값
print(pow(4,2)) # 4**2
print(max(2,4)) #최댓값, 반대는 min 함수
print(round(3.14)) #  반올림 0.5 기준 내리고 올리기

from math import *
print(floor(4.99)) #내림, 4
print(ceil(3.14)) # 올림, 4
print(sqrt(16)) #제곱근, 16의 제곱근 == 4


'''import와 from의 차이
from은 random.을 붙이지 않아도 됨, 
똑같은 이름의 함수 가능
단 중복의 가능성은 있음

import는 필요하지 않은 함수까지 포함'''

import random
print(random.randrange(1,46))

from random import *  
print(random()) #0.0이상 ~1.0 미만의 임의의 값 생성
print(random()*10) #0.0 이상 ~10.0 미만
print(int(random()*10)) #0 이상 ~10 미만
print(int(random()*10+1)) #1 이상 10 이하
print(int(random()*45+1)) #1 이상 45 이하
print(randint(1, 45)) # 1~ 45 이하

print("z")
print(randrange(1, 46)) #1~46미만
