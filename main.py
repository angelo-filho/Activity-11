import pygame
from pygame.locals import *
from Mario import Mario

pygame.init()

screen = pygame.display.set_mode([200, 200])
clock = pygame.time.Clock()

mario = Mario(200 / 2, 200 / 2)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                mario.change_animation(mario.jump_anim)
            elif event.key == K_a:
                mario.change_animation(mario.idle_anim)
            elif event.key == K_d:
                mario.change_animation(mario.run_anim)

    screen.fill([0, 0, 0])
    mario.update()
    mario.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()