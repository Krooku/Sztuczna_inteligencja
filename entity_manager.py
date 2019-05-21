import pygame


class Entity_manager:
    def __init__(self):
        self.entites = [[]]

    def add(self, entity, x , y):
        self.entites[y][x] = entity

    def find(self, name):
        for entity_row in self.entites:
            for entity in entity_row:
                if entity != 0 and entity[0] == name:
                    return entity[1]
        return 0

    def render(self, screen):
        for sprite in pygame.sprite.Group():
            screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()


