from abc import ABCMeta, abstractmethod
import pygame
import os

BLACK = (0, 0, 0)
TILESIZE = 32
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Item(ABCMeta('ABC', (object,), {'__slots__': ()})):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = True
        self.id = id(self)
        self.name = self.__class__.__name__
        self.logic_attribute_name_list = ['logic_attribute_name_list', 'name', 'id', 'x', 'y',
                                          'alive']

    def __getstate__(self):
        state = self.__dict__.copy()
        newstate = {k: state[k] for k in self.logic_attribute_name_list}
        return newstate

    def __setstate__(self, state):
        self.__dict__.update(state)

    @abstractmethod
    def use(self, benefitor):
        pass


class Health_Potion(Item):
    def __init__(self, x, y):
        Item.__init__(self, x, y)
        self.s = Health_Potion_Sprite(self, self.x, self.y)

    def use(self, benefitor):
        # TODO
        self.die()

    def get_active(self):
        return self.active

    def die(self):
        self.active = False


class Health_Potion_Sprite(pygame.sprite.Sprite):
    def __init__(self, entity, x, y):
        self.entity = entity
        # self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, pygame.sprite.Group())
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image = pygame.image.load("img/health_potion.png")
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
