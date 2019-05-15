from abc import ABCMeta, abstractmethod
import pygame

TILESIZE = 32

class Entity(ABCMeta('ABC', (object,), {'__slots__': ()})):
    def __init__(self):
        self.groupId = 0
        self.activy = True

class Slime(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.s = Slime_Sprite(self, self.x, self.y)

    def die(self):
        self.active = False


class Slime_Sprite(pygame.sprite.Sprite):
    def __init__(self, entity, x, y):
        self.entity = entity
        # self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, pygame.sprite.Group())
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image = pygame.image.load("img/slime.png")
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
