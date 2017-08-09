

import turtle


import time



turtle.hideturtle()
turtle.penup()
turtle.pensize(5)
turtle.goto(250, 250)
turtle.pendown()
turtle.goto(250, 280)
turtle.goto(180, 280)
turtle.goto(180, 250)
turtle.goto(250, 250)
turtle.penup() 
turtle.goto(215, 255)


timer = turtle.clone()
b = turtle.clone()
b.penup()
b.showturtle()
b.shape("square")

b.color("white")
b.goto(223,265)

def countdown(t):    
    while t >= 0:
        b.stamp()
        timer.write(t)
        time.sleep(1)
        t -= 1        
    quit()

countdown(180)
