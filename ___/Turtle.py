import turtle
turtle.getscreen()
#intro
turtle.shape("turtle")
turtle.forward(100)
turtle.left(45)
#turtle.shape("arrow")
turtle.bk(200)
turtle.rt(45)
print(turtle.shape())
#square
turtle.shape("turtle")
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.rt(45)
turtle.forward(100)
print(turtle.shape())
turtle.exitonclick()
"""                                    """
import turtle
turtle.getscreen()
#intro
turtle.shape("turtle") #arrow
turtle.forward(100)
turtle.left(45)
turtle.bk(200)
turtle.rt(45)
print(turtle.shape())
#square
turtle.shape("turtle")
turtle.speed(1) # 3 / 6 / 10 / 0
turtle.forward(100)
turtle.lt(90)
turtle.forward(100)
turtle.lt(90)
turtle.forward(100)
turtle.lt(90)
turtle.forward(100)
turtle.circle(100)
print(turtle.shape())
turtle.exitonclick()
#turtle.done()
#turtle.mainloop()
"""                                    """
from turtle import Turtle, Screen
#s = Screen()
x = Turtle()
y = Turtle()
x.shape("turtle")
x.pencolor("red")
x.forward(100)
x.fillcolor("green")
#x.pencolor("red")
#x.pencolor("red", "green")
print(x.pencolor())
x.color("red", "green")
x.begin_fill()
x.circle(100)
x.end_fill()
x.rt(90)
x.penup()
print(x.isdown())
x.forward(100)
x.pendown()
x.pensize(10)
x.hideturtle()
print(x.isvisible())
x.circle(50)
print(x.pos())
x.goto(-100, -100)
x.showturtle()
#x.forward(100)
#s.mainloop()
x.screen.mainloop()
"""                                    """
"""            Desh Line                """
from turtle import Turtle, Screen
s = Screen(); x = Turtle()
for _ in range(10):
    x.forward(10)
    x.penup()
    x.forward(10)
    x.pendown()
s.exitonclick()
"""                   shape           """
from turtle import Turtle, Screen
x = Turtle()
colors = ["red", "green", " pink", "orange", " blue", "black", " bromn"]
for i in range(3, 9):
    angle = 360 / i
    x.pencolor(random.choice(colors))
    for _ in range(i):
        x.forward(100)
        x.right(angle)
x.screen.mainloop()
"""          COLORSHAPE         """
from turtle import Turtle
import random
directions = [0, 90, 180, 270]
turtle.colormode(255)
x = Turtle()
x.width(10)
x.speed("fastest")
x.shape("turtle")
for _ in range(100):
    r = random.randint(255)
    g = random.randint(255)
    b = random.randint(255)
    #x.setheading(random.randrange(0, 360, 90))
    x.seth(random.choice(directions))
    x.pencolor((r, g, b))
    x.forward(90)
x.screen.mainloop()
"""                STAR                """
from turtle import Turtle, Screen
s = Screen()
x = turtle()
x.color("red", "color")
#print(x.heading())
x.begin_fill()
while True:
    x.forward(200)
    x.left(170)
    if x.heading() == 0
        break
x.end_fill()
x.exitonclick()
"""                CIRCLE               """
from turtle import Turtle, Screen
turtle.colormode(255)
x = turtle()
x.speed("fastest")
s = Screen()
while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    x.pencolor((r, g, b))
    x.circle(100)
    x.left(5)
    if x.heading == 0:
        break
x.exitonclick()
"""            DOT                    """
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
x = Turtle()
s = Screen()
s.screensize(500, 500)
print(s.screensize())
x.dot(20)
x.penup()
x.speed(10)
for _ in range(300):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    x.pencolor((r, g, b))
    x.goto(random.randint(-300, 300), random.randint(-300, 300))
    x.dot(20)
s.exitonclick()
"""									TURTLE RACE								"""
import random
from turtle import Turtle, Screen
WIDTH, HEIGHT = 400, 400
colorList= ["red", "green", " pink", "yellow", "black", "brown", "blue", "orange", "gray", " black4"]
def numTurtle():
    cnt = 0
    while True:
        cnt = int(input("How many turtle will participate: "))
        if 2 <= cnt <= 10:
            return cnt
        else:
            print("Try again")
trt = numTurtle()
s = Screen()
s.setup(400, 400)
x_spacing = WIDTH // (trt + 1)
lst = []
for i in range(1, trt + 1):
    x = Turtle()
    x.shape("turtle")
    x.left(90)
    x.color(colorList[i - 1])
    x.penup()
    x.goto(-WIDTH // 2 + (i * x_spacing), -HEIGHT // 2 + 10)
    lst.append(x)
def race():
    isRaceOn = True
    while isRaceOn:
        for t in lst:
            dist = random.randrange(1, 20)
            t.forward(dist)
            x, y = t.pos()
            if y >= HEIGHT // 2 - 20:
                print(f"winner is: {t.pencolor} ")
                isRaceOn = False
race()
s.exitonclick()
"""           EVENT LISTENERS          """
import turtle
from turtle import Turtle, Screen
s = Screen()
x = Turtle()
def up():
    x.heading(90)
    x.forward(20)
def down():
    x.heading(270)
    x.forward(20)
def left():
    x.heading(180)
    x.forward(20)
def right():
    x.heading(0)
    x.forward(20)
def clearScreen():
    x.clear()
    x.penup()
    x.home()
    x.pendown()
turtle.listen()
s.onkey(fun = up, key = "Up")
s.onkey(fun = down, key = "Down")
s.onkey(fun = left, key = "Left")
s.onkey(fun = right, key = "Right")
s.onkey(fun = clearScreen, key = "C")
s.exitonclick()
"""                            """
from turtle import Turtle, Screen
x = Turtle()
s = Screen()
def moveForward():
    x.forward(10)
def moveBackWard():
    x.backward(10)
def turnLeft():
    newHead = x.heading() + 20
    x.setheading(newHead)
    x.forward(10)
def turnRight():
    newHead = x.heading() + 20
    x.setheading(newHead)
    x.forward(10)
def clearScreen():
    x.clear()
    x.penup()
    x.home()
    x.pendown()
s.listen()
s.onkey(fun = moveForward, key = "f")
s.onkey(fun = moveBackward, key = "b")
s.onkey(fun = turnLeft, key = "l")
s.onkey(fun = turnRight, key = "r")
