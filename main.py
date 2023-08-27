import time
from snake import Snake
from turtle import Screen
from food import Food
from wall import Wall
from scoreboard import Scoreboard
import random

SPEED=0.15

scoreboard=Scoreboard()
screen=Screen()
screen.bgcolor("black")
screen.setup(620,620)
screen.tracer(0)


snake=Snake()
food = Food()
wall=Wall()
wall.create_walls()
def turn_off():
    global game_is_on
    game_is_on=False
def game_speed(speed):
    screen.update()
    time.sleep(speed)

paused = False

# Función para pausar o reanudar
def toggle_pause():
    global paused, game_is_on
    paused = not paused
    scoreboard.pause(paused,game_is_on)

def reset_game():
    global game_is_on, SPEED,paused
    paused = False
    SPEED = 0.15
    snake.reset()
    food.refresh(snake.segments)
    scoreboard.restore()
    scoreboard.show_score()
    screen.onkeypress(None, "Return")
    screen.onkeypress(toggle_pause, "space")
    screen.listen()  # Volver a escuchar las teclas



# Configuración de la tecla para pausar/reanudar


screen.onkeypress(toggle_pause, "space")
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")
screen.onkeypress(turn_off,"Escape")
screen.listen()




game_is_on = True
paused = False
while game_is_on:
    if not paused:
        game_speed(SPEED)
        snake.move_snake()
        if snake.eats(food):
            food.refresh(snake.segments)
            snake.grow()
            scoreboard.increase_score()
            if scoreboard.score % 3 == 0 and SPEED>0.03:
                SPEED -= 0.01
        if snake.colision_with_wall() or snake.colision_with_tail():
            paused = True  # Establecer el estado de pausa al chocar
            scoreboard.game_over()
            screen.onkeypress(reset_game, "Return")
            screen.onkeypress(None, "space")
    screen.update()
    screen.delay(100)