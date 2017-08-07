import turtle

pos_list = []
stamp_list= []
food_pos = []
food_stamps= []

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

#turtle.setup(SIZE_X, SIZE_Y)
## makes the border box for the game:
##turtle.pensize(10)
##turtle.penup()
##turtle.goto(RIGHT_EDGE, UP_EDGE)
##turtle.pendown()
##turtle.goto(RIGHT_EDGE, DOWN_EDGE)
##turtle.goto(LEFT_EDGE, DOWN_EDGE)
##turtle.goto(LEFT_EDGE-10, UP_EDGE-10)
##turtle.goto(RIGHT_EDGE-10, UP_EDGE-10)
##turtle.penup()


turtle.register_shape('car.gif')
car = turtle.clone()
car.shape("car.gif")

car.penup()


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
SQUARE_SIZE = 20



food = turtle.clone()
food.shape("square")
food.hideturtle()


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

def stop_move():
    global direction
    direction = SPACBAR
    print("You pressed the RIGHT key")

turtle.onkeypress( up, UP_ARROW)
turtle.onkeypress( down, DOWN_ARROW)
turtle.onkeypress( left, LEFT_ARROW)
turtle.onkeypress( right, RIGHT_ARROW)
turtle.onkeypress( stop_move , SPACBAR)
turtle.listen()


def move_car():
    my_pos = car.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

##MOVE THE CAR BY STEPS

    
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
            print("you r stock")

    my_pos = car.pos()
    new_pos= my_pos
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    pos_list.append(my_pos)
    
    new_stamp = car.stamp()
    stamp_list.append(new_stamp)
    ###pop 0 ele. in pos_list to get #RID OF THE TAIL LAST PIECE#######
    
    

    # the car is eating the food
    if car.pos() in food_pos:
        food_ind = food_pos.index(car.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        make_food()
    else:
        old_stamp = stamp_list.pop(0)
        car.clearstamp(old_stamp)
        pos_list.pop(0)
##BORDER TUCHED - GAME OVER
    
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right edge! GAME OVER!")
        quit()

    if new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! GAME OVER!")
        quit()

    if new_y_pos >= UP_EDGE:
        print("you hit the top edge! GAME OVER!")
        quit()

    if new_y_pos <= DOWN_EDGE:
        print("you hit the down edge! GAME OVER!")
        quit()
     ### car DONT EAT YOURSELF !!!
    
    if new_pos in pos_list[:-1]:
        print("you eat yourslef ! GAME OVER!")
        quit()

        
    turtle.ontimer(move_car, TIME_STEP)

move_car()
