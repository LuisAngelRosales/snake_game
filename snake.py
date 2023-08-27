from turtle import Turtle

DISTANCE=20
STARTING_POSITION=[(0,0
                    ),(-DISTANCE,0
                          ),(-DISTANCE*2,0)
                            # ,(-DISTANCE*3,0)
                            #     ,(-DISTANCE*4,0
                            #         ),(-DISTANCE*5,0
                            #             ),(-DISTANCE*6,0
                            #                ),(-DISTANCE*7,0)
                             ]
UP=90
RIGHT=0
LEFT=180
DOWN=270
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
        self.update_body()

    def create_snake(self):
        for position in STARTING_POSITION:
            turtle=Turtle()
            turtle.up()
            turtle.shape("square")
            turtle.color("white")
            turtle.goto(position)
            self.segments.append(turtle)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # Mover segmentos fuera de la pantalla
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.update_body()

    def change_direction(self, new_heading):
        if not self.direction_locked:
            self.head.setheading(new_heading)
            self.direction_locked = True

    def update_body(self):
        self.body = self.segments[1:]
    def move_snake(self):
        for segment_number in range(len(self.segments)-1,0,-1):
            self.segments[segment_number].goto(self.segments[segment_number-1].pos())
        self.head.fd(DISTANCE)
        self.direction_locked = False

    def up(self):
        if self.head.heading() !=(DOWN):
            self.change_direction(UP)

    def right(self):
        if self.head.heading() != (LEFT):
            self.change_direction(RIGHT)

    def left(self):
        if self.head.heading() != (RIGHT):
            self.change_direction(LEFT)

    def down(self):
        if self.head.heading() !=(UP):
            self.change_direction(DOWN)

    def grow(self):
        turtle = Turtle()
        turtle.up()
        turtle.shape("square")
        turtle.color("white")
        turtle.goto(self.segments[-1].pos())
        self.segments.append(turtle)
        self.update_body()

    def colision_with_tail(self):
        for segments in self.body:
            if self.head.distance(segments) <19:
                return True


    def colision_with_wall(self):
        if (self.head.xcor() >= 300 or self.head.ycor() >= 300) or (
                self.head.xcor() <= -300 or self.head.ycor() <= -290):
            return True
    def eats(self,food):
        if self.head.distance(food) < 15:
            return True