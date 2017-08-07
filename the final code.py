import turtle
import random
square_size = 20
turtle.tracer(1,0)
wall_list = []

def draw_square(x,y,a, color):
    drawer = turtle.clone()
    drawer.penup()
    drawer.hideturtle()
    drawer.goto(x,y)
    drawer.pendown()
    drawer.begin_fill()
    drawer.goto(x,y-a)
    drawer.goto(x+a,y-a)
    drawer.goto(x+a,y)
    drawer.goto(x,y)
    drawer.end_fill()
    drawer.fillcolor(color)
    wall_list.append(drawer.pos())

#making a random maze , duh 
def random_maze(n):
    """
    Choose n random positions
    on the maze board, add them
    to a list which will be returned
    later

    It will also fill the area that
    a block occupies
    """
    all_points = []
    for x in range(-250, 250 - square_size +1, square_size):
        for y in range(-250 + square_size, 250 + 1, square_size):
            all_points.append((x,y))

    set_wall_list = set()
    while len(set_wall_list) != n:
        rand_index = random.randint(0, len(all_points) - 1)
        set_wall_list.add(all_points[rand_index])
        draw_square(all_points[rand_index][0], all_points[rand_index][1], square_size, "black")

    return list(set_wall_list)    
    
    
    
    
#window
x_size = 600
y_size = 600
turtle.hideturtle()
turtle.setup(x_size, y_size)

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

# random_maze ( how many blocks )
wall_list = random_maze(150)


###########the food and the score#############
score=0
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]
turtle.register_shape('car.gif')
car = turtle.clone()
car.shape("car.gif")
turtle.hideturtle()
turtle.penup()
turtle.register_shape("burger.gif")
food = turtle.clone()
food.shape("square")
food.color('blue')
food_pos=[]
food_stamps=[]
food_list = []
xpos = -250, 250 - square_size + 1, square_size
ypos = -250 + square_size, 250 + 1, square_size
all_points = []
for x in range(-250, 250 - square_size + 1, square_size):
    for y in range(-250 + square_size, 250 + 1, square_size):
        all_points.append((x,y))

s_all_points = set(all_points)
s_wall_points = set(wall_list)
s_free_points = s_all_points - s_wall_points
free_points = list(s_free_points)

number_of_burgers=random.randint(5,15)
for num in range(number_of_burgers):
    obj = turtle.clone()
    obj.hideturtle()
    obj.shape("square")
    obj.color("red")
    food_list.append(obj)


def make_food():

##    for i in range(number_of_burgers):
##        food_list.append(food.clone())
##
##
##    if car.pos() in food_pos:
##        food_ind=food_pos.index(car.pos())
##        food.clearstamp(food_stamps[food_ind])
##        food_pos.pop(food_ind)
##        food_stamps.pop(food_ind)
##        print("You have eaten the food!")
##        score+=1
##        print(score)

    for clone in food_list:
        print(free_points)
        rand_index = random.randint(0, len(free_points) - 1)
        position = free_points[rand_index]
        while position in wall_list:
            rand_index = random.randint(0, len(free_points) - 1)
            position = free_points[rand_index]
        food_pos.append(position)
        clone.goto(position)
        draw_square(position[0], position[1], square_size, "red")
##        b=clone.stamp()
##        food_stamps.append(b)
##        clone.hideturtle()
make_food()
    
<<<<<<< HEAD
make_food()
=======
>>>>>>> 480f42d884e96f341ddcb11fbe95f33f42c1c3aa
############################################
