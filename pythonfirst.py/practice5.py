
#자료 구조의 변경 list, tuple, set으로의 변경
menu={"커피","우유","주스"}
print(menu, type(menu))

menu=list(menu)
print(menu, type(menu))

'''참석률을 높이기 위한 댓글 이벤트
댓글 중 추첨으로 1명 치킨,3명은 쿠폰
1. 편의상 20명이 작성, 아이디는 1~20
2.댓글과 상관없이 무작위, 중복 불가
3.random모듈의 shuffle, sample 활용
--당첨자 발표--
치킨 당첨자:1
커피 당첨자:[2,3,4]
--축하합니다--'''

from random import * #shuffle, sample이 필요하니까
lst=[1,2,3,4,5]
shuffle(lst) #무작위로 섞기
print(lst)
print(sample(lst,1)) #숫자를 1개 뽑기

from random import *
users=range(1,21) #type가 range -> list에서 쓸 함수의 한정
users=list(users)
shuffle(users)
winners=sample(users,4) #중복될 수 있기 때문에 같이 뽑
print("치킨 당첨자:{0}".format(winners[0]))
print("커피 당첨자{0}".format(winners[1:]))


#my answer
#set가 있어야 나중에 coffee 당첨자 제외 set로 변형 
#difference 이용할 수 있어서 list 안한거 
from random import *
lstt=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

shuffle(lstt) #shuffle은 set가 순서가 없음, tuple도 불가( 정보 변경 안됨) 확실 x
lstt=set(lstt)
chi=set(sample(lst,1))
print(chi)

#lstti=lstt.remove(chi)  chi가 아니라 list 안의 원소여야함
lssti=lstt-chi
list(lssti)
#shuffle(lssti)
cof=set(sample(lssti,3))
print("--당첨자 발표--")
print("치킨 당첨자:", chi)
print("커피 당첨자:", cof)
print("--축하합니다--")
'''set로 sampling은 deprecated 되어서 사라질 예정
list로 이용할 것!'''


#if
#elif 0<=temp and temp < 10 : -> and 사이의 괄호 생략
#for
for waiting_no in range(1,6):
    print("대기번호:{0}".format(waiting_no))
names=['thor','groot']
for customers in names:
    print("{0}님, 커피 준비 되었습니다".format(names))
#한명씩 돌아가며 출력

#while
customer="thor"
index=5
while index>=1:
    print("{0}, 커피 나왔습니다.".format(customer))
    index-=1
    if index==0:
        print("커피는 폐기 처분되었습니다")

'''customer="man"
index=1
while True: # always True=> 무한 루프
    print("{0}, coffee ready, called{1} times".format(customer, index))
    index+=1 '''
#ctrl c로 종료








