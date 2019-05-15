import pygame
import entity

TILESIZE = 32

class Main_guy(entity.Entity):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        entity.Entity.__init__(self)
        self.s = Main_guy_Sprite(self, self.x, self.y)

    def use(self, benefitor):
        # TODO
        self.die()

    def die(self):
        self.active = False

class Main_guy_Sprite(pygame.sprite.Sprite):
    def __init__(self, entity, x, y):
        self.entity = entity
        # self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, pygame.sprite.Group())
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image = pygame.image.load("img/main_guy.png")
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE