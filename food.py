from turtle import Turtle
import random
from snake import Snake

class Food(Turtle,Snake):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.goto(random.randint(-280,280),random.randint(-280,280))

    def refresh(self, snake_segments):
        free_food = False
        while not free_food:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            free_food = True
            for segment in snake_segments:
                if segment.distance(x, y) < 15:
                    free_food = False
                    break
        self.goto(x, y)