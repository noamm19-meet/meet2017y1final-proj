import turtle

pos_list1 = []
stamp_list1= []

turtle.register_shape('car.gif')
car = turtle.clone()
car.shape("turtle")
car.color('blue')

car.penup()
turtle.hideturtle()

square_size = 20
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
SPACBAR = 5
direction  = UP

move_comand = [UP, DOWN, RIGHT, LEFT]


def up():
    global direction
    #if direction!= DOWN:
    direction= UP
    print("You pressed the UP key")

def down():
    global direction
    #if direction != UP:
    direction= DOWN  
    print("You pressed the DOWN key")

def left():
    global direction
    #if direction != RIGHT:
    direction= LEFT
    
    print("You pressed the LEFT key")

def right():
    global direction
    #if direction!=LEFT:
    direction= RIGHT
    print("You pressed the RIGHT key")

def stop_move():
    global direction
    direction = SPACBAR
    for i in range(2):
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

##MOVE THE CAR BY STEPS

    
    if direction == RIGHT:
        car.goto( x_pos+ square_size, y_pos)
        print("you moved right!")
        
    elif direction==LEFT:
        car.goto(x_pos-square_size, y_pos)
        print("you moved left!")
        
    elif direction == UP:
        car.goto( x_pos , y_pos+square_size)
        print("you moved up!")

    elif direction == DOWN:
        car.goto( x_pos , y_pos-square_size)
        print("you moved down!")
    elif direction == SPACBAR:
        print()
        

    my_pos = car.pos()
    new_pos= my_pos
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    pos_list.append(my_pos)
    
    new_stamp = turtle.stamp()
    stamp_list.append(new_stamp)
##    new_stamp.hideturtle()
##    
##    new_stamp.clearstamp()
   
    
    if new_x_pos >= 250:
        print("you hit the RIGHT edge! GAME OVER!")
        quit()

    if new_x_pos <= -250:
        print("you hit the LEFT edge! GAME OVER!")
        quit()

    if new_y_pos >= 250:
        print("you hit the TOP edge! GAME OVER!")
        quit()

    if new_y_pos <= -250:
        print("you hit the DOWN edge! GAME OVER!")
        quit()
     
        
    turtle.ontimer(move_car, TIME_STEP)

if direction in move_comand:
    move_car()

##else:
##    print('f')
##    
##

