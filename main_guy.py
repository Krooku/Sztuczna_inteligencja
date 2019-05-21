import pygame
import entity

TILESIZE = 32

class Main_guy(entity.Entity):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step = TILESIZE
        entity.Entity.__init__(self)
        self.s = Main_guy_Sprite(self, self.x, self.y)

    def move_right(self):
        if self.rect.x + self.rect.width + self.step <= self.window_width:
            self.rect.x += self.step

    def move_left(self):
        if self.rect.x >= self.step:
            self.rect.x -= self.step

    def move_down(self):
        if self.rect.y + self.rect.height + self.step <= self.window_height:
            self.rect.y += self.step

    def move_up(self):
        if self.rect.y >= self.step:
            self.rect.y -= self.step

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