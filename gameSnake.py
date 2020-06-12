import pygame
from random import *

pygame.init()

# config the game
screenWidth = 640
screenHeight = 360
init_time = 75
speed = 0
run = True
scl = 20

# generate a new food when old one ate
food_loc = [9 * scl, 9 * scl, scl, scl]


def food_generate(eaten):
    global scl, food_loc
    if eaten:
        x = randrange(0, screenWidth / scl)
        y = randrange(0, screenHeight / scl)

        food_loc = [x * scl, y * scl, scl, scl]


# define the snake
class Snake:
    def __init__(self, x, y, width=scl, height=scl, direction=None):
        if direction is None:
            direction = [0, 0]

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction

        self.head = [self.x, self.y, self.width, self.height]
        self.body = [self.head]

    def move_head(self):
        self.head[0] += self.direction[0]
        self.head[1] += self.direction[1]

    def move_tail(self):
        if len(self.body) > 1:
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i] = self.body[i - 1].copy()

    def draw(self):
        for i in range(len(self.body) - 1, -1, -1):
            pygame.draw.rect(win, (0, 255, 0), self.body[i])

    def get_key(self, con):

        if con[pygame.K_LEFT] and self.direction != [scl / 2, 0]:
            self.direction = [-scl / 2, 0]

        elif con[pygame.K_RIGHT] and self.direction != [-scl / 2, 0]:
            self.direction = [scl / 2, 0]

        elif con[pygame.K_UP] and self.direction != [0, scl / 2]:
            self.direction = [0, -scl / 2]

        elif con[pygame.K_DOWN] and self.direction != [0, -scl / 2]:
            self.direction = [0, scl / 2]

    def food_ate(self):
        global food_loc
        if self.head == food_loc:
            self.body.append([])
            return True

        return False

    def crashed(self):
        if len(self.body) >= 2:
            for i in range(1, len(self.body)):
                if self.head == self.body[i]:
                    print('Stop hitting yourself!')
                    return True

        if self.head[0] < 0 or self.head[0] > screenWidth - scl or self.head[1] < 0 or self.head[1] > screenHeight - scl:
            print('\nYou crashed through the wall!')
            return True

        return False


# the main loop
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Snake game!')

mySnake = Snake(0, 0)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    control = pygame.key.get_pressed()
    mySnake.get_key(control)

    # control before draw for smooth control
    pygame.time.delay(init_time)
    win.fill((0, 0, 0))

    mySnake.move_tail()
    mySnake.move_head()
    mySnake.draw()

    pygame.time.delay(init_time)
    win.fill((0, 0, 0))
    mySnake.move_tail()
    mySnake.move_head()

    # after ate the food, you must move the tail before drawing the snake or error will happen
    mySnake.draw()

    food_generate(mySnake.food_ate())

    if mySnake.crashed():
        run = False

    pygame.draw.rect(win, (255, 0, 0), food_loc)

    pygame.display.update()

print('\nGame Over!\nYour score is: %d\n' % len(mySnake.body))

pygame.quit()
