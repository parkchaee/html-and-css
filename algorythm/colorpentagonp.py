for dist in range(10,71,10):
    dist2=dist%70
    if dist==10:
        turtle.pencolor('red')
    elif dist2==20:
        turtle.pencolor('orange')
    elif dist2==30:
        turtle.pencolor('yellow')
    elif dist2==40:
        turtle.pencolor('green')
    elif dist2==50:
        turtle.pencolor('blue')
    elif dist2==60:
        turtle.pencolor('navyblue')
    elif dist2==70:
        turtle.pencolor('purple')
    for i in range(3):
        turtle.forward(dist)
        turtle.right(angle)

turtle.done()