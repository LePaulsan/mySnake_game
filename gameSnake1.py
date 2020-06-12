import pygame
from random import *
from Snake import *

pygame.init()

# config the game
width = 640
height = 360
frame_rate = 75
speed_up = 0
run = True
scl = 20

# generate a new food when old one ate
food_loc = [9 * scl, 9 * scl, scl, scl]


def food_generate(eaten):
    global scl, food_loc
    if eaten:
        x = randrange(0, width / scl)
        y = randrange(0, height / scl)

        food_loc = [x * scl, y * scl, scl, scl]

    pygame.draw.rect(win, (255, 0, 0), food_loc)

# the main loop
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game!')

mySnake = Snake(0, 0, scl)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    control = pygame.key.get_pressed()
    mySnake.get_key(control)

    # control before draw for smooth control
    pygame.time.delay(frame_rate)
    win.fill((0, 0, 0))

    mySnake.move()
    mySnake.draw(win)

    pygame.time.delay(frame_rate)
    win.fill((0, 0, 0))
    mySnake.move()
    mySnake.draw(win)

    # after ate the food, you must move the tail before drawing the snake or error will happen

    food_generate(mySnake.food_ate(food_loc))

    if mySnake.crashed(width, height):
        run = False



    pygame.display.update()

print('\nGame Over!\nYour score is: %d\n' % len(mySnake.body))

pygame.quit()
