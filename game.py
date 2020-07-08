import pygame as pg
from snake import Snake
from control import Controller
import random as r

class Game:
    def __init__(self, width, height, initLoc=pg.Vector2(0, 0), delay=200):
        self.width = width
        self.height = height
        self.win = pg.display.set_mode((width, height))
        self.snake = Snake(self.win, initLoc)
        self.control = Controller()
        self.running = True
        self.delay = delay
        self.food = pg.Vector2(60, 60)
        pg.display.set_caption("Smake!")

    def display(self):
        pg.init()
        while self.running:
            self.getInput()
            self.main()
        pg.quit()

    def main(self):
        self.win.fill((0, 0, 0))
        vel = 20 * self.getControll()
        self.drawFood(self.food)
        pg.time.delay(self.delay)
        
        self.snake.updateLoc(vel)
        if self.snake.ateFood(self.food):
            self.snake.addToTail()
            self.makeFood()
        self.crashChecked()

        self.snake.draw()

        pg.display.update()

    def getInput(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def getControll(self):
        command = pg.key.get_pressed()
        vel = self.control.getKey(command)
        return vel
    
    def makeFood(self):
        x = r.randint(0, self.width/20 - 1)
        y = r.randint(0, self.height/20 - 1)
        self.food = 20 * pg.Vector2(x, y)

    def drawFood(self, loc):
        pg.draw.rect(self.win, (255, 0, 0), (loc.x, loc.y, 20, 20))

    def crashChecked(self):
        snake = self.snake.getLoc()
        if 0 <= snake.x <= self.width and 0 <= snake.y <= self.height:
            return
        
        self.running = False

game = Game(640, 360)
game.display()