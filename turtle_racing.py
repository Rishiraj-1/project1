import turtle
import time
import random

WIDTH, HEIGHT = 500, 600
COLORS = ['red', 'black', 'blue', 'cyan', 'pink', 'yellow', 'green', 'brown', 'orange', 'purple','red', 'black', 'blue', 'cyan', 'pink', 'yellow', 'green', 'brown', 'orange', 'purple'
          ]

def init_turtle():
    screen = turtle.Screen()
    turtle.screensize(WIDTH, HEIGHT)
    turtle.title("Turtle Racing")

def get_no_of_racers():
    while True:
        racers = input("Enter no of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid Input!")
            continue

        if 2 <= racers <= 20:
            return racers
        else:
            print("Invalid Input!")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT//2:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingX = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.speed(2)
        racer.shape('turtle')
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingX, -HEIGHT//2 + 0)
        racer.pendown()
        turtles.append(racer)
    return turtles

racers = get_no_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
time.sleep(2)
print(f"{winner.upper()} WON!")