#if문
'''
a=99
if a<99:
    print("100보다 작다")
a=200
if a<100:
    print("100보다 작다")
else:
    print("100보다 크다")

score=int(input("성적:"))
if score>=90:
    print("a")
elif score>=80:
    print("b")
elif score>=70:
    print("c")
elif score>=60:
    print("d")
elif score>=50:
    print("f")
print("학점입니다")

print("온도 변환")
print("1.섭씨--> 화씨")
print("2.화씨--> 섭씨")
a=int(input("번호를 입력하세요"))
if a==1:
    temp=int(input("섭씨 온도를 입력하세요"))
    f=temp*9/5+32
    print("섭씨 %d온도는 화씨 %d도입니다"%(temp,f))

import turtle
turtle.title("turtle")
turtle.shape("turtle")
turtle.speed(10)
dist=0 #
while True: #
    num=int(input("몇각형"))
    turtle.clear
    if num==0:
        break
    angle=360/num 

    for i in range(10,71,10):
        if i==10:
            turtle.pencolor('red')
    for i in range(num):
        turtle.forward(dist) #
        turtle.right(angle) #
    turtle.done() #


for j in range(2,10,1):
    for i in range(1,10,1):
        print(i,"x",j,"i*j")

i, k, gugu=0,0,""
for i in range(2,10):
    gugu+=str("#%d단#"%i)
print(gugu)
for i in range(1,10):
    gugu=""
    for k in range(2,10):
        gugu+=str("%2dx%2d=%2d"%(k,i,k*i))
    print(gugu)

i,k,gu=0,0,""
for i in range(1,10,1):
    gu+=str("#%단#",i)
print(gu)
for k in range(2,10,1):
    for j in range(1,10,1):
        gu+=str("%2dx%2d=%2d"%(k,j,k*j))
    print(gu)
while True:
    print("=")
    print("1.정수")
    print("2.짝수")
    print("3.홀수")
    print("배수")
    print("약수")
    print("6.그만")
    men=int(input("메뉴 선택"))
    rec=int(input("반복 횟수"))
    num=int(input("숫자"))
    print("정수값 처리 시작")
    if men==6:
        print("끝냅니다")
        break
    if men==1 or men==2 or men==3 or men==4 or men==5:
        rec=int(input("반복 횟수"))
        num=int(input("숫자"))
        print("정수값 처리 시작")
    if men==1:
        for i in (1,rec+1,1):
            print(i, end="")
    elif men==2:
        for i in (1,rec+1,1):
            if i%2==0:
                print(i,end=" ")
    elif men==3:
        for i in range(1,rec+1,1):
            if i%2==1:
                print(i,end=" ")
    elif men==4:
        for i in range(1,rec+1,1):
            if i/num==0:
                print(i, end=" ")
    elif men==5:
        for i in range(1,num+1,1): #
            if num/i==0:
                print(i,end=" ")#
                print("%d의 약수값은 %d입니다"%(num,i))
print("계속하려면 엔터를 누르세요")
print()

import turtle as t
t.bgcolor("black")
t.shape("turtle")
t.speed(0)
for x in range(200):
    if x%3==0:
        t.color("red")
    if x%3==1:
        t.color("yellow")
    if x%3==2:
        t.color("blue")
    t.forward(x*2) #x*2 변수 길이 확대
    t.left(119) #119도 왼쪽 회전 각도 변화

heroes =[]
heroes.append("m")
print(heroes)
letters=['a'] # index 수 대로 출력 
print(letters[0])
print(letters[:3]) #실제 3번째 전까지 출력
letters=['1','2','3']
print(letters[-3:-1]) #끝번째전까지 출력
#-1이 끝번째
heroes[1]="d" #리스트 항목 변경
heroes.insert(1,"h") #index기준 1자리에 넣기
heroes.remove("d")
if "d" in heroes:
    heroes.remove("d")
del heroes[0]
#pop은 마지막 제거
last=heroes.pop("d")
print(last) #제거하는 원소 출력
print(heroes.index("h")) #위치 찾기
for hero in heroes:
    print(hero) 
heroes.sort() #ㄱㄴㄷ순

list=[]
num=1
print("점수 입력, 0인 경우 종료")
while num!=0:
    num=int(input("점수:"))
    list.append(num)
print("현재 입력된 점수는")
print(list,"이고 모두",len(list),"개")

score=[]
sc=0
print("점수를 입력하세요.0인 경우 종료")
while True:
    sc=int(input("점수"))
    if sc==0:
        break
    score.append(sc)
print("현재 입력된 점수는 ")
print(score,"이고 모두",len(score),"개입니다")

print("리스트 연습")
print("0.exit")
print("1.insert")
print("2.sort")
print("3.reverse")
print("4.index")
print("5.remove")
print("6.del")
print("7.count")
sel=int(input("원하는 번호"))
while True:
    sel=int(input("원하는 번호"))
    list.clear()
    if sel==0:
        break
    else:
        if sel==1: #
            numb=int(input("추가"))
            idx=int(input("위치"))
            list.insert(idx,numb)
        elif sel==2:
            list.sort()
        elif sel==3:
            list.reverse()
        elif sel==4: #
            numb=int(input("인덱스"))
            list.index(numb)
        elif sel==5:    
            numb=int(input("제거"))
            list.remove(numb)
        elif sel==6:
            numb=input("제거")
            del(list[numb])
        elif sel==7: #
            numb=int(input("개수를 알고싶은 값"))
            cnt=score.count(numb) 
            print(score)
            print("%d는%d번 나옴"%(numb,cnt))
dict={'진':'RJ'}
while True:
    cha=input(str(list(dict.keys()))+"중 어떤 캐릭")
    if cha in dict:
        print("%s의 캐릭은 %s입니다"%(cha,dict[cha]))
    elif cha=="끝":
        print("없음")
        break
import random    
print("**로또 추첨을 시작합니다**")
print("추천된 로또 번호",end=" ")
cnt=0
while cnt<6:
    num=random.randint(1,46)
    print(num,end=" ")
    cnt+=cnt
    num=0
#이렇게 하면 겹치는 경우를 제외하지 못함
# list,def 이용 조건

import random
lotto=[]
num=0
def numb():
    return random.randint(1,46)
print("로또 시작")
while True:
    num=numb()
    if lotto.count(num)==0:
        lotto.append(num)
    if len(lotto)==6:
        break
print("로또 번호>",end=" ")
lotto.sort()
for i in range(0,6):
    print("%d"%lotto[i],end="")

import turtle
turtle.title("turtle")
turtle.shape("turtle")
for i in (0,4):
    turtle.forward(10)
    turtle.right(90)
for i in range(0,3):
    turtle.forward(100)
    turtle.right(120)
num=int(input("몇각형"))
for i in range(0,num):
    turtle.forward(10)
    turtle.right(360/num)

import turtle
turtle.title("turtle")
turtle.shape("turtle")
num=int(input("몇각형"))
def draw(num):
    dist=100
    angle=360/num
    for i in range(0,num):
        turtle.forward(dist)
        turtle.right(angle)
draw(num)
turtle.done()

def fib(n):
    num1,num2=0,1
    if n==1 or n==0:
        print("0 1")
    else:
        return fib(n-1)+fib(n-2)
print(fib(1))

#배수랑 홀수만 보면 됨
if sel==4:
    for i in range(1,rec+1):
        if i%num==0:
            print(num)
if sel==5:
    for k in range(1,num+1):
        if num%i==0:
            print(num)

import turtle as t
t.bgcolor("black")
t.shape("turtle")
t.speed(0)

heroes=[]
heroes.append("m")
letters=['a']
score=[]
sc=0
print("점수를 입력하세요.0 입력시 종료")
while True:
    sc=int(input("점수"))
    if sc==0:
        break
    score.append(sc)
print("점수는")
print(score,"이고",len(score),"입니다")

numb=int(input("추가"))
idx=int(input("위치"))
num=int(input("입력할 값"))
list.insert(idx, num)
print(list)

numb=int(input("값"))
cnt=score.count(numb)
print(score)
print("%d는%d번 나옴"%(numb,cnt))

#캐릭 인형
dict={"진":"RJ"}
cha=input("cha")
while True:
    cha=int(input(list(dict.keys()))+"중 어떤 캐릭")

    if cha in dict:
        print("%s %s"%(cha,dict[cha]))
    if cha=="끝":
        print("없음")
        break

import random
lotto=[]
num=0
def numb():
    return random.randint(1,46)
print("로또 시작")
while True:
    num=numb()
    if lotto.count(num)==0:
        lotto.append(num)
    if len(lotto)==6:
        break

import random
lotto=[]
num=0
def getnu():
    return random.randint(1,46)
print("로또 시작")    
while True:
    num=getnu()
    if lotto.count(num):
        lotto.append(num)
    if len(lotto)<=6:
        break
print("로또 번호",end=" ")
lotto.sort()
for i in range(num):
    print("%d"%lotto[i],end=" ")
'''
list=['a','b']
print(list)