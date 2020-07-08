import pygame as pg
from pygame import Vector2

class Controller:
    def __init__(self):
        self.lastState = Vector2(0,0)

    def getKey(self, keyState):
        if keyState[pg.K_LEFT] and self.lastState != Vector2(-1, 0) and self.lastState != Vector2(1, 0): 
            self.lastState = Vector2(-1, 0)
            return Vector2(-1, 0)
        elif keyState[pg.K_RIGHT] and self.lastState != Vector2(-1, 0) and self.lastState != Vector2(1, 0): 
            self.lastState = Vector2(1, 0)
            return Vector2(1, 0)
        elif keyState[pg.K_UP] and self.lastState != Vector2(0, -1) and self.lastState != Vector2(0, 1): 
            self.lastState = Vector2(0, -1)
            return Vector2(0, -1)
        elif keyState[pg.K_DOWN] and self.lastState != Vector2(0, -1) and self.lastState != Vector2(0, 1): 
            self.lastState = Vector2(0, 1)
            return Vector2(0, 1)
        else:
            return self.lastState
