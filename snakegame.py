import turtle
import time
import random

delay = 0.1

# Score
s = 0
hs = 0

# Set up the screen
screen = turtle.Screen()
screen.title("Snake")
screen.bgcolor("white")
screen.setup(width=550, height=550)
screen.tracer(0)  # Turns off the screen updates

# Snake head
snakehead = turtle.Turtle()
snakehead.speed(0)
snakehead.shape("circle")
snakehead.color("grey")
snakehead.penup()
snakehead.goto(0, 0)
snakehead.direction = "Stop"

# Snake food
snakefood = turtle.Turtle()
snakefood.speed(0)
snakefood.shape("circle")
snakefood.color("green")
snakefood.penup()
snakefood.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if snakehead.direction != "down":
        snakehead.direction = "up"


def go_down():
    if snakehead.direction != "up":
        snakehead.direction = "down"


def go_left():
    if snakehead.direction != "right":
        snakehead.direction = "left"


def go_right():
    if snakehead.direction != "left":
        snakehead.direction = "right"


def move():
    if snakehead.direction == "up":
        y = snakehead.ycor()
        snakehead.sety(y + 20)

    if snakehead.direction == "down":
        y = snakehead.ycor()
        snakehead.sety(y - 20)

    if snakehead.direction == "left":
        x = snakehead.xcor()
        snakehead.setx(x - 20)

    if snakehead.direction == "right":
        x = snakehead.xcor()
        snakehead.setx(x + 20)


# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")


# Main game loop
while True:
    screen.update()

    # Check for a collision with the border
    if (
        snakehead.xcor() > 260
        or snakehead.xcor() < -260
        or snakehead.ycor() > 260
        or snakehead.ycor() < -260
    ):
        time.sleep(1)
        snakehead.goto(0, 0)
        snakehead.direction = "Stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        s = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(s, hs), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food
    if snakehead.distance(snakefood) < 20:
        # Move the food to a random position
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        snakefood.goto(x, y)

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        s += 10

        if s > hs:
            hs = s

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(s, hs), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = snakehead.xcor()
        y = snakehead.ycor()
        segments[0].goto(x, y)

    move()

    # Check for a collision with the body
    for segment in segments:
        if segment.distance(snakehead) < 20:
            time.sleep(1)
            snakehead.goto(0, 0)
            snakehead.direction = "Stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            s = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(s, hs), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)