from part import Part
# from linkedList import LinkedList
import pygame as pg

class Snake:
    def __init__(self, surface, loc, color=(0, 255, 0), size=20):
        self.surface = surface
        self.color = color
        self.size = size
        
        self.loc = loc
        self.body = [self.createPart(self.loc), self.createPart(self.loc + pg.Vector2(0, 20))]
        self.tail = self.body[len(self.body)-1]
    
    def createPart(self, loc):
        return Part(self.surface, loc, self.color, self.size)

    def updateLoc(self, vel):
        n = len(self.body)
        self.loc = self.loc + vel
        self.tail = self.body[n-1]
        self.body = self.body[:n-1]
        self.body = [self.createPart(self.loc)] + self.body
    
    def draw(self):
        for part in self.body:
            part.draw()

    def addToHead(self, location):
        self.body.addBegin((Part(self.surface, location, self.color,self.size)))

    def addToTail(self):
        self.body.append(self.tail)

    def ateFood(self, food):
        return self.body[0].getLoc() == food

    def getLoc(self):
        return self.loc