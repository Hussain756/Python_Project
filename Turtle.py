import turtle
import random

p1 = turtle.Turtle()  # MAKING PLAYER ONE
p1.color("blue")  # ADDING COLOR
p1.shape("turtle") # MAKING SHAPE

wn = turtle.Screen()
wn.bgcolor("Red")        # adding background color
wn.title("Turtle Game")

p1.penup()
p1.goto(-200, 100)  # SETTING THE POSITION OF TURTLE
p2 = p1.clone()     # CLONING  PLAYER2 WITH PLAYER1
p2.color("green")   # ADDING COLOR
p2.shape("turtle")  # MAKING SHAPE
p2.penup()
p2.goto(-200, -100)

p1.goto(300, 60)  # SETTING THE POSITION OF HOME
p1.pendown()
p1.circle(40)
p1.penup()
p1.goto(-200, 100)
p2.goto(300, -140)
p2.pendown()
p2.circle(40)
p2.penup()
p2.goto(-200, -100)

die = [1, 2, 3, 4, 5, 6]  # MAKING THE DIE

                          # codeto move the turtle and decide the winner
for i in range(20):
    if p1.pos() >= (300, 100):
        print("Player one wins")
        break
    elif p2.pos() >= (300, -100):
        print("Player two wins")

    else:
        p1_turn = input("Press Enter to roll the die")
        die_outcome = random.choice(die)
        print("The outcome is")
        print(die_outcome)
        print("The number of steps is")
        print(20 * die_outcome)
        p1.forward(20 * die_outcome)

        p2_turn = input("Press Enter to roll the die")
        die_outcome = random.choice(die)
        print("The outcome is")
        print(die_outcome)
        print("The number of steps is")
        print(20 * die_outcome)
        p2.forward(20 * die_outcome)

turtle.mainloop()

