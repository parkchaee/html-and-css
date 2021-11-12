#오각형 그리기 
#range-5, angle-72로 바꿔주기
import turtle
turtle.title("무지개 빛 삼각형 그리기")
turtle.shape('turtle')
turtle.speed(10)
dist=0
angle=72
for dist in range(10,71,10):

    if dist==10:
        turtle.pencolor('red')
    elif dist==20:
        turtle.pencolor('orange')
    elif dist==30:
        turtle.pencolor('yellow')
    elif dist==40:
        turtle.pencolor('green')
    elif dist==50:
        turtle.pencolor('blue')
    elif dist==60:
        turtle.pencolor('navyblue')
    elif dist==70:
        turtle.pencolor('purple')
    for i in range(5):
        turtle.forward(dist)
        turtle.right(angle)

turtle.done()

