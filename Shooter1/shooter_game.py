import pygame.time
from pygame import *
from Shooter.Shooter1.Player2 import player
from Shooter.Shooter1.Enemy import anemy, return_lost
from random import randint
from BulletPatron import bullet
from Asteroid import asteroid



# создай окно игры
window = display.set_mode((700, 500))
display.set_caption("shooter")

mixer.init()
mixer.music.load('Bye-Bye.mp3')
mixer.music.play()
fire = mixer.Sound("fire.ogg")

font.init()
font1 = font.SysFont("Areal", 36)
font2 = font.SysFont("Areal", 36)

win = font.Font("Areal", 36)
lose = font.Font("Areal", 36)

momsters = sprite.Group()
astrd = sprite.Group()
Bulet = sprite.Group()

ufos = []
for i in range(5):
    ufos.append(anemy('ufo.png', randint(5, 700), 0, randint(1, 4), (65, 65), window))

for i in range(5):
    momsters.add(ufos[i])


asteroide = []
for i in range(3):
    asteroide.append(anemy('asteroid.png', randint(5, 700), 0, randint(2, 6), (65, 65), window))

for i in range(3):
    astrd.add(asteroide[i])

hero = player('rocket.png', 130, 350, 18, (65, 65), window)

# задай фон сцены
background = transform.scale(image.load("galaxy.jpg"), (700, 500))

score = 0
FPS = 30
clock = time.Clock()

fire_rate = 250
last_shot = pygame.time.get_ticks()

game = True
finish = False
while game:
    # Установка ФПС
    clock.tick(FPS)
    #счёт
    text_lose = font1.render("Попущенно: " + str(return_lost()), 1, (128, 0, 128))
    text_kill = font2.render("Избито: " + str(score), 1, (75, 0, 130))
    for e in event.get():
        # обработай событие «клик по кнопке "Закрыть окно"»
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))

        window.blit(text_lose, (0, 0))
        window.blit(text_kill, (0, 40))

        hero.update()

        Bulet.draw(window)
        Bulet.update()
        hero.reset()

        astrd.draw(window)
        astrd.update

        momsters.draw(window)
        momsters.update()

        keys = key.get_pressed()
        if keys[K_SPACE]:
            # Проверка интервала времени с последнего выстрела
            current_time = pygame.time.get_ticks()
            if current_time - last_shot >= fire_rate:
                hero.fire(Bulet, fire)
                last_shot = current_time




    display.update()

