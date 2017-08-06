import turtle

#window
turtle.hideturtle()
turtle.setup(550,550)

#border
border = turtle.clone()
border.hideturtle()
border.pensize(5)
border.penup()
border.goto(250,250)
border.pendown()
border.goto(250,-250)
border.goto(-250,-250)
border.goto(-250,250)
border.goto(250,250)
border.penup()

#making maze 1
maze1 = turtle.clone()
maze1.hideturtle()

