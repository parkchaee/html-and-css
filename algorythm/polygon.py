import turtle
turtle.title('다각형 그리기')
turtle.shape('turtle')
def drawPolygon(num):
    dist=100
    angle=360/num
    for i in range(0,num):
        turtle.forward(dist)
        turtle.right(angle)
n=int(input("몇각형을 그리겠습니까?"))
drawPolygon(n)
turtle.done()