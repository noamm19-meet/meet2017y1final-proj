###########the food and the score#############
import turtle
import random

square_size=20
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
wall_list = []

all_points = []
for x in range(-250, 250 - square_size + 1, square_size):
    for y in range(-250 + square_size, 250 + 1, square_size):
        all_points.append((x,y))

s_all_points = set(all_points)
s_wall_points = set(wall_list)
s_free_points = s_all_points - s_wall_points
free_points = list(s_free_points)


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
        rand_index = random.randint(0, len(free_points) - 1)
        position = free_points[rand_index]
        while position in wall_list:
            rand_index = random.randint(0, len(free_points) - 1)
            position = free_points[rand_index]
            

        food_pos.append(position)
        clone.goto(position)
        b=clone.stamp()
        food_stamps.append(b)
        clone.hideturtle()


make_food()        
    
make_food()    
############################################
