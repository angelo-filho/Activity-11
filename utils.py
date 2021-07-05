import pygame


def load_image_2x(image):
    img = pygame.image.load(image)
    img = pygame.transform.scale2x(img)

    return img
