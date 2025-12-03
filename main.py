from turtle import Turtle, Screen
from random import choice
from time import sleep

screen = Screen()
screen.setup(width=1000, height=800)
screen.tracer(0)
screen.bgcolor("black")
screen.title("The Snake Game")

class Snake:
    def __init__(self):
        self.body = [Turtle("turtle"), Turtle("square"), Turtle("square")]

        distance = 0
        for body_block in self.body:
            body_block.penup()
            body_block.color("white")
            body_block.setheading(180)
            body_block.speed(0)
            body_block.teleport(body_block.pos()[0] + distance, body_block.pos()[1])
            distance += 20
        
    def locomotion(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i-1].pos())
        self.body[0].forward(20)

    def add_body_segment(self):
        self.body.append(Turtle("square"))
        self.body[-1].penup()
        self.body[-1].color("white")
        self.body[-1].setheading(self.body[-2].heading())
        self.body[-1].speed(0)
        self.body[-1].goto(self.body[-2].pos())
        self.body[-1].backward(20)

    def turn_left(self):
        self.body[0].left(90)

    def turn_right(self):
        self.body[0].right(90)

    def move_up(self):
        if self.body[0].heading() == 180: # facing west
            self.turn_right()
        elif self.body[0].heading() == 0: # facing east
            self.turn_left()

    def move_down(self):
        if self.body[0].heading() == 180: # facing west
            self.turn_left()
        elif self.body[0].heading() == 0: # facing east
            self.turn_right()

    def move_right(self):
        if self.body[0].heading() == 90: # facing north
            self.turn_right()
        elif self.body[0].heading() == 270: # facing south
            self.turn_left()

    def move_left(self):
        if self.body[0].heading() == 90: # facing north
            self.turn_left()
        elif self.body[0].heading() == 270: # facing south
            self.turn_right()

    def hit_itself(self):
        for _ in range(1, len(self.body)):
            if round(self.body[_].distance(self.body[0]), 2) < 20:
                return True
        return False

    def hit_boundry(self):
        head_position_x = round(self.body[0].xcor(), 2)
        head_position_y = round(self.body[0].ycor(), 2)
        x_boundry = screen.window_width() // 2 - 20
        y_boundry = screen.window_height() // 2 - 20
        return not ((-1 * x_boundry) <= head_position_x <= x_boundry and (-1 * y_boundry) <= head_position_y <= y_boundry)

def generate_food_coordinate():
    x_body_positions = []
    y_body_positions = []

    for body_part in snake.body:
        x_body_positions.append(body_part.xcor())
        y_body_positions.append(body_part.ycor())

    x_available = []
    for x_cor in range(-483, 484):
        if not (x_cor in x_body_positions):
            x_available.append(x_cor)

    y_available = []
    for y_cor in range(-395, 395):
        if not (y_cor in y_body_positions):
            y_available.append(y_cor)

    return (choice(x_available), choice(y_available))

snake = Snake()
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

food = Turtle("circle")
food.penup()
food.color("red")
food.goto(generate_food_coordinate())

while not (snake.hit_itself() or snake.hit_boundry()):
    if round(snake.body[0].distance(food), 2) < 20:
        snake.add_body_segment()
        food.goto(generate_food_coordinate())

    snake.locomotion()
    screen.update()
    sleep(0.1)

# -------------
screen.exitonclick()
