"""python game 쓸 경우 재설치 시 add Python PATH 체크
명령 프롬프트
python -m pip install --upgrade pip #최신 버전으로 업데이트
pip install pygame # 파이썬 게임 이용
exit #command 창에서 나옴
"""
import pygame
pygame.init()
#색상에 대한 변수 설정
#rgb 모듈을 기본으로 함
BLACK=(0,0,0) #색상이 없으면 검정으로 나옴
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)

size=[400,300]
screen=pygame.display.set_mde(size)
#해상도 (화면크기) 설정 x축 400 y축 300
pygame.display.set_caption("Game Title")
done=False
clock=pygame.time.Clock()
while not done:
    clock.tick(10) #0.001초 의미 - 화면이 계속 돌아가도록 함
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(WHITE) 
    pygame.display.flip()
    #0.001초마다 무한루프-> 색상 변경을 화면으로 보여줄 것
    #screen 위로, 색상, 좌표 이동값으로 표현, 선의 굵기 

    pygame.draw.polygon(screen,GREEN, [[30,150],[125,100],[220,150]],5)
    pygame.draw.polygon(screen,GREEN,[[30,150],[125,100],[220,150]],0)
    pygame.drwa.lines(screen,RED,False,[[50,150],[50,250],[200,250],[200,150]],5)
    #이 부분에서는 거짓으로 하겠다 :False
    pygame.draw.rect(screen, BLACK,[75,175,75,50],5)
    #테두리를 검정색으로
    pygame.draw.rect(screen,BLUE,[75,175,75,50],0)
    #창문
    pygame.draw.line(screen,BLACK,[112,175],[112,225],5)
    pygame.draw.line(screen,BLACK,[75,200],[150,200],5)
    #태양
    pygame.draw.circle(screen,RED,[350,50],40)

    pygame.display.flip()
