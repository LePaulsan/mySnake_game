import pygame as pg

class Part:
    def __init__(self, surface, loc, color, size):
        self.surface = surface
        self.loc = loc
        self.color = color
        self.size = size

    def getLoc(self):
        return self.loc
    def updateLoc(self, vel):
        self.loc = self.loc + vel

    def draw(self):
        pg.draw.rect(self.surface, self.color, (self.loc.x, self.loc.y, self.size, self.size))
