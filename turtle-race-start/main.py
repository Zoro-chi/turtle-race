from turtle import Turtle, Screen
import random


race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bets", prompt="Which color turtle will win the race? : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_index =[-100, -60, -20, 20, 60, 100]
strawhats = []


for turtle_index in range(6):
    new_strawhat = Turtle(shape="turtle")
    new_strawhat.penup()
    new_strawhat.color(colors[turtle_index])
    new_strawhat.goto(x=-230, y=y_index[turtle_index])
    strawhats.append(new_strawhat)

race_on = True
while race_on:

    for new_strawhat in strawhats:
        move = random.randint(0, 10)
        new_strawhat.fd(move)
        if new_strawhat.xcor() > 230:
            race_on = False
            winning_color = new_strawhat.pencolor()
            if winning_color == user_bet:
                print("You Win")
            else:
                print(f"You loose, the Winning strawhat was {winning_color}")
        


screen.exitonclick()