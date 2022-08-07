import turtle
turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)
turtle.title("Circle Circle")
for i in range (5):
    for colours in ['red','magenta','blue','cyan','green','yellow','white']:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
#turtle.hideturtle()        
turtle.done()