
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("Make your bet", "Which turtle win the race, enter the color name:")
colors = ["red","green","yellow","blue","orange","purple"]
all_turtle_list = []
y_axis = -100
is_race_on = True
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_axis)
    new_turtle.color(colors[i])
    y_axis += 50
    all_turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle_list:
        winning_color = turtle.pencolor()
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            if winning_color == user_bet:
                print(f"You win, the winning turtle color is {winning_color}")
            else:
                print(f"You lost, the winning turtle color is {winning_color}")




screen.exitonclick()