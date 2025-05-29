import random
import turtle

turtles = list()

def setup():
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(width=1290, height=720)
    screen.bgpic("pavement.gif")

    turtle_ycor = [-40, -20, 0, 20, 40]
    turtle_color = ["yellow", "red", "blue", "green", "brown"]


    for i in range(0, len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        turtles.append(new_turtle)

def race():
    global turtles
    winner = False
    finishline = 590

    while not winner:
        for current_turtle in turtles:
            move = random.randint(0,30)
            current_turtle.forward(move)

            xcor = current_turtle.xcor()
            if (xcor >= finishline):
                winner = True
                winner_color = current_turtle.color()
                print("The winner is:", winner_color[0])
                break

setup()
race()
turtle.mainloop()
