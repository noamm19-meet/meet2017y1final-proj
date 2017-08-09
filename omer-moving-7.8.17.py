import turtle

pos_list = []
stamp_list= []
car_pos_l = []
car_stamps_l= []

SIZE_X = 400
SIZE_Y = 600

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

turtle.setup(SIZE_X, SIZE_Y)
##makes the border box for the game:
##turtle.pensize(10)
##turtle.penup()
##turtle.goto(RIGHT_EDGE, UP_EDGE)
##turtle.pendown()
##turtle.goto(RIGHT_EDGE, DOWN_EDGE)
##turtle.goto(LEFT_EDGE, DOWN_EDGE)
##turtle.goto(LEFT_EDGE-10, UP_EDGE-10)
##turtle.goto(RIGHT_EDGE-10, UP_EDGE-10)
##turtle.penup()


turtle.register_shape('car3.gif')
car = turtle.clone()
car.shape("car3.gif")

car.penup()
turtle.hideturtle()



UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

TIME_STEP = 500

SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
SPACBAR = 5
direction  = UP
SQUARE_SIZE = 20

move_comand = [UP, DOWN, RIGHT, LEFT]

##food = turtle.clone()
##food.shape("square")
##food.hideturtle()


def up():
    global direction
    direction= UP
    move_car()
    print("You pressed the UP key")

def down():
    global direction
    direction= DOWN
    move_car()
    print("You pressed the DOWN key")

def left():
    global direction
    direction= LEFT
    move_car()
    print("You pressed the LEFT key")

def right():
    global direction
    direction= RIGHT
    move_car()
    print("You pressed the RIGHT key")

def stop_move():
    global direction
    direction = SPACBAR
    for i in range(1):
        print("You pressed the SPACBAR key")

turtle.onkeypress( up, UP_ARROW)
turtle.onkeypress( down, DOWN_ARROW)
turtle.onkeypress( left, LEFT_ARROW)
turtle.onkeypress( right, RIGHT_ARROW)
turtle.onkeypress( stop_move , SPACEBAR)
turtle.listen()


def move_car():
    my_pos = car.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

##MOVE THE CAR BY STEPS:
    if direction == RIGHT:
        car.goto( x_pos+ SQUARE_SIZE, y_pos)
        print("you moved right!")
    elif direction==LEFT:
        car.goto(x_pos-SQUARE_SIZE, y_pos)
        print("you moved left!")
    elif direction == UP:
        car.goto( x_pos , y_pos+SQUARE_SIZE)
        print("you moved up!")
    elif direction == DOWN:
        car.goto( x_pos , y_pos-SQUARE_SIZE)
        print("you moved down!")
    elif direction == SPACBAR:
        print()
        

    newcar_pos = car.pos()
    new_x_pos = newcar_pos[0]
    new_y_pos = newcar_pos[1]
    car_pos_l.append(newcar_pos)
    
    new_car_stamp = car.stamp()
    car_stamps_l.append(new_car_stamp)
    old_car_stamp = car_stamps_l.pop(0)
    car.clearstamp(old_car_stamp)
    car_pos_l.pop(0)
   
##BORDER    
##    if new_x_pos >= RIGHT_EDGE:
##        for t in range(200):
##            print("you hit the RIGHT edge! GAME OVER!")
##        quit()
##
##    if new_x_pos <= LEFT_EDGE:
##        for t in range(200):
##            print("you hit the LEFT edge! GAME OVER!")
##        quit()
##
##    if new_y_pos >= UP_EDGE:
##        for t in range(200):
##            print("you hit the TOP edge! GAME OVER!")
##        quit()
##
##    if new_y_pos <= DOWN_EDGE:
##        for t in range(200):
##            print("you hit the DOWN edge! GAME OVER!")
##        quit()
##     
        
    #turtle.ontimer(move_car, TIME_STEP)


