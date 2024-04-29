from pygame import *
from GameCpire import GameSprite
from random import randint

lost = 0

class anemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 550:
            self.rect.x = randint(20, 700-85)
            self.rect.y = 0
            lost += 1


def return_lost():
    global lost
    return lost
