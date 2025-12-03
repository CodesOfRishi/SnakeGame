from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")

class Snake:
    def __init__(self):
        self.body = [Turtle("turtle"), Turtle("square"), Turtle("square")]

        distance = 0
        for body_block in self.body:
            body_block.penup()
            body_block.color("white")
            body_block.setheading(180)
            body_block.goto(body_block.pos()[0] + distance, body_block.pos()[1])
            distance += 22
        
    def locomotion(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i-1].pos())
        self.body[0].forward(22)

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
        head_position_x = round(self.body[0].xcor(), 2)
        head_position_y = round(self.body[0].ycor(), 2)

        for i in range(1, len(self.body)):
            if head_position_x == round(self.body[i].xcor(), 2) and head_position_y == round(self.body[i].ycor(), 2):
                return True
        return False

    def hit_boundry_line(self):
        head_position_x = round(self.body[0].xcor(), 2)
        head_position_y = round(self.body[0].ycor(), 2)
        return head_position_x >= 484 or head_position_y > 396 or head_position_x <= -484 or head_position_y < -396

def draw_boundry_line():
    t = Turtle()
    t.speed(0)
    t.pencolor("white")
    t.teleport(x=-484.00, y=418.00)
    t.goto(484.00, 418.00)
    t.right(90)
    t.goto(484.00, -418.00)
    t.right(90)
    t.goto(-484.00, -418.00)
    t.right(90)
    t.goto(-484.00, 418.00)
    t.hideturtle()
    del t

draw_boundry_line()

snake = Snake()
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

while not (snake.hit_itself() or snake.hit_boundry_line()):
    snake.locomotion()

# -------------
screen.exitonclick()
