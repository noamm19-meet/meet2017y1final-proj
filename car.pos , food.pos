import turtle

sizex = 800
sizey = 500

turtle.setup(sizex,sizey)

turtle.penup()

square_size = 20
starlen = 1
car_pos_list = []
car_stamp_list =[]
car = turtle.clone()
car.shape("turtle")
turtle.hideturtle()

for i in range (starlen):
    mycarx = car.pos()[0]
    mycary = car.pos()[1]
    mycarx += 20
    car.goto(mycarx,mycary)
    car_pos_list.append(car.pos())
    

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

UP  = 0
DOWN = 1
LEFT = 2
RIGHT = 3

direction = UP
def up1():
    global direction
    direction = UP 
    move_car()
    print("u press up")
def left1():
    global direction
    direction = LEFT
    move_car()
    print("u press left")
def right1():
    global direction
    direction = RIGHT
    move_car()
    print("u press right")
def down1():
    global directon
    direction = DOWN
    move_car()
    print("u press down")


turtle.onkeypress(up1 ,UP_ARROW)
turtle.onkeypress(left1 , LEFT_ARROW)
turtle.onkeypress(down1 , DOWN_ARROW)
turtle.onkeypress(right1 , RIGHT_ARROW)
turtle.listen()

def move_car():
    my_car = car.pos()
    carx_pos = my_car[0]
    cary_pos = my_car[1]
    
    if direction == UP:
        car.goto(carx_pos , cary_pos + square_size)
        print("go up")
    elif direction == DOWN:
        car.goto(carx_pos , cary_pos - square_size)
        print("go down")
    elif direction == RIGHT:
        car.goto(carx_pos + square_size , cary_pos)
        print("go right")
    elif direction == LEFT:
        car.goto(carx_pos - square_size , cary_pos)
        print("go left")
    

    my_car = car.pos()
    car_pos_list.append(my_car)
    new_car_stamp = car.stamp()
    car_stamp_list.append(new_car_stamp)
    old_car_stamp = car_stamp_list.pop(0)
    car.clearstamp(old_car_stamp)
    car_pos_list.pop(0)
    
