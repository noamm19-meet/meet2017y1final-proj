

import turtle


import time

def countdown(t):
    turtle.hideturtle()
    turtle.penup()
    turtle.pensize(5)
    turtle.goto(250, 250)
    turtle.pendown()
    turtle.goto(250, 280)
    turtle.goto(180, 280)
    turtle.goto(180, 250)
    turtle.goto(250, 250)


    timer = turtle.clone()
    
    while t >= 0:
        timer.clear()
        timer.write(t)
        time.sleep(1)
        t -= 1
    print('Goodbye! \n \n \n \n \n')

countdown(5)

##turtle.ontime(time , 1000)
    













turtle.mainloop()
