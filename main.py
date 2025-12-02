from turtle import Turtle, Screen

class Snake:
    def __init__(self):
        self.body = [Turtle("square"), Turtle("square"), Turtle("square")]
        distance = 22
        for body_block in self.body:
            body_block.penup()
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


snake = Snake()
for _ in range(0, 5):
    snake.move_snake()

snake.turn_left()

for _ in range(0, 10):
    snake.move_snake()

snake.turn_right()

for _ in range(0, 10):
    snake.move_snake()


# -------------
screen = Screen()
screen.exitonclick()
