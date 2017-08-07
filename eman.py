###########the food and the score#############
import turtle
import random

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
