from pygame import *
from GameCpire import GameSprite
from Shooter.Shooter1.BulletPatron import bullet

class player(GameSprite):

    def update(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed

    def fire(self, group, sound):
        group.add(bullet('bullet.png', self.rect.x + 27, self.rect.y - 15, 10, (15, 15), self.window))
        sound.play()



