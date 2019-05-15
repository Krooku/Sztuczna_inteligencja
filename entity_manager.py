import pygame


class Entity_manager:
    def __init__(self):
        self.entites = [[]]

    def add(self, entity, x , y):
        self.entites[y][x] = entity

    def render(self, screen):
        for sprite in pygame.sprite.Group():
            screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()


