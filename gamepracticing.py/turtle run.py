#부스트, 스피드, 잡아먹는
import turtle as t #객체 이름 t
import random #random하게 먹은 아이템들이 표시되도록
import time # 시간에 따라서 play 진행

score=0 #점수 저장
playing=False #게임 중인지 확인하는 변수
boost=False #값이 있다 없다로만 판단-> T== 아이템 먹음
tspeed=1 #점점 속도 올릴 수 있도록 하는 변수 


t.title("Turtle Run") #내가 조정하는 터틀
t.setup(1800,1000)
t.bgcolor("orange")
t.shape("turtle") #거북이 커서
t.speed(0) #거북이 속도 가장 빠르게 지정
t.up()
t.color("white")

te=t.Turtle() #악당거북이 te 
te.shape("turtle")
te.color("red")
te.speed(0)
te.up() #펜 들기
te.goto(0,200) #처음 위치

#먹이 
ts=t.Turtle() 
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)

#boost-속도를 올려줌
ta=t.Turtle()
ta.shape("triangle")
ta.color("blue")
ta.speed(0)
ta.up()
ta.goto(0,50)

#shield
tb=t.Turtle()
tb.shape("square")
tb.color("yellow")
tb.speed(0)
tb.up()
tb.goto(0,80)

#호도법에 따른 방향키 바꿈 (이동을 위한)
def turn_right(): #오른쪽으로 방향 바꿈
    t.setheading(0)
def turn_up():
    t.setheading(90) #위
def turn_left(): #왼
    t.setheading(180)
def turn_down(): #아래
    t.setheading(270)

#메세지 화면에 표시
def message(m1,m2,m3):
    t.clear()
    t.goto(0,100) #메세지 위치
    t.write(m1, False,"center",("",30)) #center 쪽에 30 폰트 크기로 표시
    t.goto(0,-100)
    t.write(m2, False, "center",("",25))
    t.goto(0,-135)
    t.write(m3,False, "center",("",15))
    t.home()

def push_A(): 
    t.write("You can use boost",font=("",50)) #먹은 후 문구
    t.forwar(100) #전진


def die():
    
    global playing
    text="Score:"+str(score)
    message("Game Over", text, "you bad")
    playing=False
    score=0

def start(): #게임 시작 
    global playing 
    if playing==False:
        playing=True
        t.clear() #메세지 지움 t에 대해(t가 썼음)
        play()

def speeditem(): #speed 조절
    global tspeed,canitem
    if tspeed>10:
        canitem=55
    if tspeed>20:
        canitem=60
    if tspeed>25:
        canitem=65
    if tspeed>30:
        canitem=70
    if tspeed>40:
        canitem=80
    if tspeed>60:
        canitem=110
    if tspeed>70:
        canitem=130
    if tspeed>80:
        canitem=150

def play(): 
    canitem=30
    global boost
    global score
    global playing
    global tspeed
    for i in range(tspeed):
        t.forward(4)
        speeditem()
    if random.randint(1,50)==5: #2%확률 뽑은 수가 5
        ang=te.towards(t.pos())
        te.setheading(ang) #악당 거북이가 주인공을 바라보도록
    speed=score-4

    for x in range(speed):
        if random.randint(1,50)==3: 
            ang=te.towards(t.post())
            te.setheading(ang)
        te.forward(3)
    
    if t.distance(ts)<canitem: #주인공과 먹이 거리가 12보다 작으면
        score=score+10
        t.write("Score:"+str(score), font=("",20))
        star_x=random.randint(-400,400)
        star_y=random.randint(-230,230)
        ts.goto(star_x,star_y) #먹이를 다른 곳으로 이동
    if t.distance(ta)<canitem:#주인공, 레벨 거리<12
        tspeed=tspeed+3
        t.write("turtle speed:"+str(tspeed))
        star2_x=random.randint(-400,400)
        star2_y=random.randint(-230,230)
        ta.goto(star2_x,star2_y) #레벨을 다른 곳으로
    if t.distance(tb)<canitem:
        if boost==True:
            t.write('you have boost')
        if boost==False:
            boost=True
            star3_x=random.randint(-700,700)
            star3_y=random.randint(-400,400)
            tb.goto(star3_x,star3_y)

        if t.distance(te<canitem):#주인공, 악당 거리<12
            if boost==True:
                score+=5
                t.write("Score:"+str(score),font=("",20))
                star_x=random.randint(-1500,1500)
                star_y=random.randint(-1500,1500)
                te.goto(star_x,star_y) #먹이를 다른 곳으로
                boost=False
            else:
                text="Score:"+str(score)
                message("Game Over",text,"you bad")
                playing= False
                score=0
            

        

    if playing:
        t.ontimer(play,200) #게임 플레이 중이면 0.1초후 플레이


#방향키 이용
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(start,"space") #실행
t.listen()  #onkeypress를 사용했으면 응답을 한번 해줘야 함
#그래야 움직임
message("Turtle Run","[Space]","SM University")
#세 매개변수 호출되면 def message의 문구 실현
