import pygame
import sys
SCREEN_WIDTH=640
SCREEN_HEIGHT=480
white =(255,255,255)
black=(0,0,0)
pygame.init() #파이게임 초기화 작업
#변수 선언 이후에 해도 ㄱㅊ
pygame.display.set_caption("simple pygame example")
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#->스크린 생성 (x,y축 크기 설정)

x=200
y=200

clock=pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get(): #중간에 발생하는 이벤트 캐치 함수
        if event.type==pygame.QUIT: #창닫기 버튼을 누르면
            sys.exit() #import sys
            #작동중지
    key_event=pygame.key.get_pressed()
    #지금까지는 아직 화면에 나오는 게 없

    #왼쪽 방향으로 이동 

    if key_event[pygame.K_LEFT]:
        x-=1
    if key_event[pygame.K_RIGHT]:
        x+=1
    if key_event[pygame.K_UP]:
        y-=1
    if key_event[pygame.K_DOWN]:
        y+=1

    




    screen.fill(black)
    pygame.draw.circle(screen,white,(x,y),20)#동그라미 생성    
    #x=200,y=200으로 설정 
    #그래픽 좌표계는 일반 좌표계와 달리 왼쪽 상단의 끝 꼭지점을 원점으로
    pygame.display.update()


