from turtle import Turtle
class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-310,-310)
        self.pendown()
        self.pensize(10)
        self.pencolor("white")
    def create_walls(self):
        for side in range (4):
            self.fd(620)
            self.left(90)