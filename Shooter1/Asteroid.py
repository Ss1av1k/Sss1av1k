from GameCpire import GameSprite
from random import randint


class asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= 550:
            self.rect.x = randint(20, 700-85)
            self.rect.y = 0
