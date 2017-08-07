import turtle
import random
square_size = 20
turtle.tracer(1,0)
wall_list = []

def draw_square(x,y,a):
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
        draw_square(all_points[rand_index][0], all_points[rand_index][1], square_size)

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
random_maze(150)


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
number_of_burgers=random.randint(5,15)
turtle.register_shape("burger.gif")
food = turtle.clone()
food.shape("burger.gif")
food_pos=[]
food_stamps=[]
food_list = []
def make_food():
    for i in range(number_of_burgers):
        food_list.append(food.clone())


    if car.pos() in food_pos:
        food_ind=food_pos.index(car.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
        score+=1
    
    for clone in food_list:
        x_pos = random.randint(-250,250) 
        y_pos = random.randint(-250,250)
        position=(x_pos , y_pos)            
    
    food_pos.append(position)
    clone.goto(position)
    b=clone.stamp()
    food_stamps.append(b)
    clone.hideturtle()
    

############################################

