from turtle import Turtle, Screen
from random import randint
from time import sleep

screen = Screen()
screen.setup(width=1000, height=800)
screen.tracer(0)
screen.bgcolor("black")
screen.title("The Snake Game")

SEGMENT_DISTANCE = 20
X_BOUNDRY = screen.window_width() // 2 - SEGMENT_DISTANCE
Y_BOUNDRY = screen.window_height() // 2 - SEGMENT_DISTANCE

class Snake:
    def __init__(self):
        self.body = []
        self.add_body_segment()
        
        self.last_move_turned = False

    def locomotion(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i-1].pos())
        self.body[0].forward(SEGMENT_DISTANCE)
        self.last_move_turned = False

    def add_body_segment(self):
        self.body.append(Turtle("square"))
        self.body[-1].penup()
        
        if len(self.body) >= 2:
            self.body[-1].color("LightGray")
            self.body[-1].setheading(self.body[-2].heading())
            self.body[-1].goto(self.body[-2].pos())
            self.body[-1].backward(SEGMENT_DISTANCE)
        else:
            self.body[-1].color("white")
            self.body[-1].setheading(180)

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
        for segment in self.body[1:]:
            if segment.distance(self.body[0]) < (SEGMENT_DISTANCE - 5):
                return True
        return False

    def hit_boundry(self):
        head_position_x = self.body[0].xcor()
        head_position_y = self.body[0].ycor()
        
        if head_position_x >= X_BOUNDRY or head_position_x <= -X_BOUNDRY or head_position_y >= Y_BOUNDRY or head_position_y <= -Y_BOUNDRY:
            return True
        else:
            return False

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

        while True:
            x_coordinate = SEGMENT_DISTANCE * (randint(-1 * (X_BOUNDRY-20), (X_BOUNDRY-20)) // SEGMENT_DISTANCE)
            y_coordinate = SEGMENT_DISTANCE * (randint(-1 * (Y_BOUNDRY-20), (Y_BOUNDRY-20)) // SEGMENT_DISTANCE)

            if not (x_coordinate, y_coordinate) in snake_body_positions:
                break

        self.food_unit.teleport(x_coordinate, y_coordinate)

#### Draw Boundry Line ####
t = Turtle()
t.color("white")
t.teleport(-X_BOUNDRY, Y_BOUNDRY)
t.setheading(0)
t.pensize(20)
t.pencolor("DarkRed")
t.goto(X_BOUNDRY, Y_BOUNDRY)
t.right(90)
t.goto(X_BOUNDRY, -Y_BOUNDRY)
t.right(90)
t.goto(-X_BOUNDRY, -Y_BOUNDRY)
t.right(90)
t.goto(-X_BOUNDRY, Y_BOUNDRY)
t.hideturtle()
del t
###########################

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
    screen.update()
    if snake.body[0].distance(food.food_unit) < (SEGMENT_DISTANCE - 5):
        snake.add_body_segment()
        food.set_new_position()
        score += 1
        display_score.clear()
        display_score.write(arg=f"Scored {score}", align="center", font=('Ariel', 36, "bold"))

    snake.locomotion()
    sleep(0.1)

# -------------
screen.exitonclick()
