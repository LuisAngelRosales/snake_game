from turtle import Turtle
ALIGNMENT="center"
FONT="Courier"
FONT_SIZE=15
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt",mode="r") as f:
            self.high_score=int(f.read())
        self.score_initial_position()
        self.show_score()
        self.pause_turtle = Turtle()
        self.pause_turtle.penup()
        self.pause_turtle.color("white")
        self.pause_turtle.hideturtle()

    def score_initial_position(self):
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
    def increase_score(self):
        self.score+=1
        self.show_score()
    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=(FONT, FONT_SIZE),align=ALIGNMENT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER\nPress Intro to reset\nEsc to Exit",font=(FONT, FONT_SIZE),align=ALIGNMENT)

    def pause(self, on_pause, game_is_on):
        if game_is_on:
            if on_pause:
                self.pause_turtle.goto(0, 0)
                self.pause_turtle.write("PAUSE", font=(FONT, FONT_SIZE), align=ALIGNMENT)
            else:
                self.pause_turtle.clear()

    def restore(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("high_score.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.score_initial_position()
        self.show_score()
        self.clear()
        self.pause_turtle.clear()
