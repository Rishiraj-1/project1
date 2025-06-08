import turtle  # we use this to draw and move turtles
import time    # for delays like countdown
import random  # to move turtles random steps

# set the window size
WIDTH = 500
HEIGHT = 600

# some colors to choose from for the turtles
COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'black', 'brown', 'cyan']

# this sets up the turtle screen
def setup_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)  # make the window size fixed
    screen.title("Turtle Race Game")  # set window title
    screen.bgcolor("lightblue")  # just for fun
    return screen

# this asks user how many turtles should race
def get_number_of_racers():
    while True:
        num = input("Enter number of racers (2 to 10): ")
        if num.isdigit():  # check if input is a number
            num = int(num)
            if 2 <= num <= 10:
                return num
        # if input is wrong
        print("Please enter a number between 2 and 10.")

# this makes the turtles and puts them in starting position
def create_turtles(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)  # space between turtles
    for i in range(len(colors)):
        t = turtle.Turtle()
        t.shape("turtle")  # make it look like a turtle
        t.color(colors[i])  # give each turtle a different color
        t.penup()  # so it doesn't draw lines while moving to start
        t.goto(-WIDTH//2 + (i + 1) * spacing, -HEIGHT//2 + 20)  # starting line
        t.left(90)  # face upwards
        t.pendown()  # now ready to race
        turtles.append(t)
    return turtles

# this runs the race
def start_race(turtles, colors):
    while True:
        for i in range(len(turtles)):
            move = random.randint(1, 10)  # move turtle by 1 to 10 pixels randomly
            turtles[i].forward(move)
            # check if the turtle reached the finish line
            if turtles[i].ycor() >= HEIGHT//2 - 20:
                return colors[i]  # return the color of the winning turtle

# now everything starts here
screen = setup_screen()
num_racers = get_number_of_racers()

# mix up the colors randomly
random.shuffle(COLORS)
racer_colors = COLORS[:num_racers]

# create the turtle racers
turtle_list = create_turtles(racer_colors)

# just a fun countdown before race starts
print("Race starting in...")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

# start the race and get the winner
winner = start_race(turtle_list, racer_colors)
print(f"\n🎉 {winner.upper()} turtle wins the race! 🎉")

# keep the turtle window open until user closes it
turtle.done()
