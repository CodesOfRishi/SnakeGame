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
        self.body = []
        for _ in range(0,3):
            self.add_body_segment()
        
        self.last_move_turned = False

    def locomotion(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i-1].pos())
        self.body[0].forward(DISTANCE_GAP)
        self.last_move_turned = False

    def add_body_segment(self):
        self.body.append(Turtle("square"))
        self.body[-1].penup()
        self.body[-1].color("white")
        
        if len(self.body) >= 2:
            self.body[-1].setheading(self.body[-2].heading())
            self.body[-1].goto(self.body[-2].pos())
            self.body[-1].backward(DISTANCE_GAP)
        else:
            self.body[-1].setheading(180)

        # self.body[-1].speed(9)

    def up(self):
        if self.body[0].heading() != 270: # not facing down/south
            if self.last_move_turned:
                self.locomotion()
            self.body[0].setheading(90)
            self.last_move_turned = True

    def down(self):
        if self.body[0].heading() != 90: # not facing up/north
            if self.last_move_turned:
                self.locomotion()
            self.body[0].setheading(270)
            self.last_move_turned = True

    def right(self):
        if self.body[0].heading() != 180: # not facing left/west
            if self.last_move_turned:
                self.locomotion()
            self.body[0].setheading(0)
            self.last_move_turned = True

    def left(self):
        if self.body[0].heading() != 0: # not facing right/east
            if self.last_move_turned:
                self.locomotion()
            self.body[0].setheading(180)
            self.last_move_turned = True

    def hit_itself(self):
        for _ in range(1, len(self.body)):
            if round(self.body[_].distance(self.body[0]), 2) < (DISTANCE_GAP - 5):
                return True
        return False

    def hit_boundry(self):
        head_position_x = self.body[0].xcor()
        head_position_y = self.body[0].ycor()
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

        x_boundry = screen.window_width() // 2 - DISTANCE_GAP
        y_boundry = screen.window_height() // 2 - DISTANCE_GAP

        while True:
            x_coordinate = DISTANCE_GAP * (randint(-1 * x_boundry, x_boundry) // DISTANCE_GAP)
            y_coordinate = DISTANCE_GAP * (randint(-1 * y_boundry, y_boundry) // DISTANCE_GAP)

            if not (x_coordinate, y_coordinate) in snake_body_positions:
                break

        self.food_unit.teleport(x_coordinate, y_coordinate)

snake = Snake()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

food = Food()

score = 0
display_score = Turtle()
display_score.hideturtle()
display_score.color("green")

while not (snake.hit_itself() or snake.hit_boundry()):
    if snake.body[0].distance(food.food_unit) < (DISTANCE_GAP - 5):
        snake.add_body_segment()
        food.set_new_position()
        score += 1
        display_score.clear()
        display_score.write(arg=f"Scored {score}", align="center", font=('Ariel', 36, "bold"))

    snake.locomotion()
    screen.update()
    sleep(0.1)


# -------------
screen.exitonclick()
