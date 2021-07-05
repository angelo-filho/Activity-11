from os.path import join
from utils import *


class Mario:
    def __init__(self, x, y):
        self.idle_anim = []
        self.run_anim = []
        self.jump_anim = []
        self.load_sprites()
        self.anim_index = 0
        self.current_anim = self.idle_anim

        self.image = self.idle_anim[0]

        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(x, y, self.rect.width, self.rect.height)

    def update(self):
        self.anim_index += 0.2

        if self.anim_index >= len(self.current_anim):
            self.anim_index = 0

        self.image = self.current_anim[int(self.anim_index)]

    def change_animation(self, animation):
        self.current_anim = animation

    def load_sprites(self):
        self.idle_anim.append(load_image_2x(join("images", "mario_idle_1.png")))
        self.idle_anim.append(load_image_2x(join("images", "mario_idle_2.png")))

        self.run_anim.append(load_image_2x(join("images", "mario_run_1.png")))
        self.run_anim.append(load_image_2x(join("images", "mario_run_2.png")))
        self.run_anim.append(load_image_2x(join("images", "mario_run_1.png")))
        self.run_anim.append(load_image_2x(join("images", "mario_run_3.png")))

        self.jump_anim.append(load_image_2x(join("images", "mario_jump.png")))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
