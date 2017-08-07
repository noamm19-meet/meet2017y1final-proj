UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

TIME_STEP = 100

SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

food = turtle.clone()
food.shape("square")
food.hideturtle()


def up():
    global direction
    if direction!= DOWN:
        direction= UP
    print("You pressed the UP key")

def down():
    global direction
    if direction != UP:
        direction= DOWN
    
    print("You pressed the DOWN key")

def left():
    global direction
    if direction != RIGHT:
        direction= LEFT
    
    print("You pressed the LEFT key")

def right():
    global direction
    if direction!=LEFT:
        direction= RIGHT
   
    print("You pressed the RIGHT key")

turtle.onkeypress( up, UP_ARROW)
turtle.onkeypress( down, DOWN_ARROW)
turtle.onkeypress( left, LEFT_ARROW)
turtle.onkeypress( right, RIGHT_ARROW)
turtle.listen()

