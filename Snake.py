import pygame


class Snake:

    def __init__(self, x, y, scl, direction=None):
        if direction is None:
            direction = [0, 0]

        self.x = x
        self.y = y
        self.scl = scl
        self.direction = direction

        self.head = [self.x, self.y, self.scl, self.scl]
        self.body = [self.head]

    def move(self):
        if len(self.body) > 1:
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i] = self.body[i - 1].copy()

        self.head[0] += self.direction[0]
        self.head[1] += self.direction[1]

    def draw(self, surface):
        for i in range(len(self.body) - 1, -1, -1):
            pygame.draw.rect(surface, (0, 255, 0), self.body[i])

    def get_key(self, con):

        if con[pygame.K_LEFT] and self.direction != [self.scl / 2, 0]:
            self.direction = [-self.scl / 2, 0]

        elif con[pygame.K_RIGHT] and self.direction != [-self.scl / 2, 0]:
            self.direction = [self.scl / 2, 0]

        elif con[pygame.K_UP] and self.direction != [0, self.scl / 2]:
            self.direction = [0, -self.scl / 2]

        elif con[pygame.K_DOWN] and self.direction != [0, -self.scl / 2]:
            self.direction = [0, self.scl / 2]

    def food_ate(self, food_loc):
        if self.head == food_loc:
            self.body.append([])
            return True

        return False

    def crashed(self, screenWidth, screenHeight):
        if len(self.body) >= 2:
            for i in range(1, len(self.body)):
                if self.head == self.body[i]:
                    print('Stop hitting yourself!')
                    return True

        if self.head[0] < 0 or self.head[0] > screenWidth - self.scl or self.head[1] < 0 or self.head[
            1] > screenHeight - self.scl:
            print('\nYou crashed through the wall!')
            return True

        return False
