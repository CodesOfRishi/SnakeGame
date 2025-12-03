from turtle import Turtle, Screen
from random import randint
from time import sleep

screen = Screen()
screen.setup(width=1000, height=800)
screen.tracer(0)
screen.bgcolor("black")
screen.title("The Snake Game")

DISTANCE_GAP = 20

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
            distance += DISTANCE_GAP
        
    def locomotion(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i-1].pos())
        self.body[0].forward(DISTANCE_GAP)

    def add_body_segment(self):
        self.body.append(Turtle("square"))
        self.body[-1].penup()
        self.body[-1].color("white")
        self.body[-1].setheading(self.body[-2].heading())
        self.body[-1].speed(0)
        self.body[-1].goto(self.body[-2].pos())
        self.body[-1].backward(DISTANCE_GAP)

    def up(self):
        if self.body[0].heading() != 270: # not facing down/south
            self.body[0].setheading(90)

    def down(self):
        if self.body[0].heading() != 90: # not facing up/north
            self.body[0].setheading(270)

    def right(self):
        if self.body[0].heading() != 180: # not facing left/west
            self.body[0].setheading(0)

    def left(self):
        if self.body[0].heading() != 0: # not facing right/east
            self.body[0].setheading(180)

    def hit_itself(self):
        for _ in range(1, len(self.body)):
            if round(self.body[_].distance(self.body[0]), 2) < (DISTANCE_GAP - 5):
                return True
        return False

    def hit_boundry(self):
        head_position_x = round(self.body[0].xcor(), 2)
        head_position_y = round(self.body[0].ycor(), 2)
        x_boundry = screen.window_width() // 2 - DISTANCE_GAP
        y_boundry = screen.window_height() // 2 - DISTANCE_GAP
        return not ((-1 * x_boundry) <= head_position_x <= x_boundry and (-1 * y_boundry) <= head_position_y <= y_boundry)

class Food:
    def __init__(self):
        self.food_unit = Turtle("circle")
        self.food_unit.penup()
        self.food_unit.color("red")
        self.set_new_position()

    def set_new_position(self):
        snake_body_positions = []
        for segment in snake.body:
            snake_body_positions.append((segment.xcor(), segment.ycor()))

        y_boundry = screen.window_height()
        x_boundry = screen.window_height()

        food_position = ()
        while True:
            y_coordinate = randint((-1 * y_boundry) // 2 + DISTANCE_GAP, y_boundry // 2 - DISTANCE_GAP) 
            x_coordinate = randint((-1 * x_boundry) // 2 + DISTANCE_GAP, x_boundry // 2 - DISTANCE_GAP) 
            y_coordinate = DISTANCE_GAP * (y_coordinate // DISTANCE_GAP)
            x_coordinate = DISTANCE_GAP * (x_coordinate // DISTANCE_GAP)

            food_position = (x_coordinate, y_coordinate)
            if not food_position in snake_body_positions:
                break

        self.food_unit.teleport(food_position[0], food_position[1])

snake = Snake()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

food = Food()

while not (snake.hit_itself() or snake.hit_boundry()):
    if snake.body[0].distance(food.food_unit) < (DISTANCE_GAP - 5):
        snake.add_body_segment()
        food.set_new_position()

    snake.locomotion()
    screen.update()
    sleep(0.1)

# -------------
screen.exitonclick()
