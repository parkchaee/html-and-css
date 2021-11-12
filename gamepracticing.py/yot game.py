#윷놀이 1:배 0:등
import random as r #r은 객체, random library에서 모듈을 가져옴
#간편함을 위해 
import random
input() #enter key를 interpreter 창에서 누르면 계속 결과 도출 반복

yot1=random.randint(0,1)
yot2=random.randint(0,1)
yot3=random.randint(0,1)
yot4=random.randint(0,1)
print(yot1,yot2,yot3,yot4)


#무한반복 설정하기 => 조건 반복문 사용
#enter을 칠때마다 게임의 진행
while True: 
    total=0
    game=int(input("1.play/2.end "))
    if game==1: 


        yot1=random.randint(0,1)
        yot2=random.randint(0,1)
        yot3=random.randint(0,1)
        yot4=random.randint(0,1)
        print(yot1,yot2,yot3,yot4)
        total=yot1+yot2+yot3+yot4
        if total==0: #전부 등=모
            print("모")
        elif total==1: 
            print("도")
        elif total==2:
            print("개")
        elif total==3:
            print("걸")
        elif total==4:
            print("윷")

    elif game==2:
        print("game over")
        break


    print(yot1,yot2,yot3,yot4)

