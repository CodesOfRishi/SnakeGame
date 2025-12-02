from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")

class Snake:
    def __init__(self):
        self.body = [Turtle("square"), Turtle("square"), Turtle("square")]
        distance = 22
        for body_block in self.body:
            body_block.penup()
            body_block.color("white")
            body_block.setheading(180)
            body_block.goto(body_block.pos()[0] + distance, body_block.pos()[1])
            distance += 22
        
    def move_snake(self):
        body_block_positions = []
        for _ in range(0, len(self.body)-1):
            body_block_positions.append((self.body[_].pos(), self.body[_].heading()))

        self.body[0].forward(22)
        for i in range(0, len(self.body)-1):
            prev_position = body_block_positions[i][0]
            prev_heading = body_block_positions[i][1]
            self.body[i+1].goto(prev_position[0], prev_position[1])
            self.body[i+1].setheading(prev_heading)

    def turn_left(self):
        self.body[0].left(90)

    def turn_right(self):
        self.body[0].right(90)

    def hit_itself(self):
        for i in range(0, len(self.body)):
            for j in range(i+1, len(self.body)):
                x1 = round(self.body[i].xcor(), 2)
                y1 = round(self.body[i].ycor(), 2)
                x2 = round(self.body[j].xcor(), 2)
                y2 = round(self.body[j].ycor(), 2)

                if x1 == x2 and y1 == y2:
                    return True
        return False

    def hit_boundry_line(self):
        head_position = self.body[0].pos()
        return head_position[0] >= 484 or head_position[1] > 396 or head_position[0] <= -484 or head_position[1] < -396

snake = Snake()

while not (snake.hit_itself() or snake.hit_boundry_line()):
    snake.move_snake()

# -------------
screen.exitonclick()
