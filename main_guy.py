import pygame
import entity

TILESIZE = 32

class Main_guy(entity.Entity):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.attack = 20
        entity.Entity.__init__(self)
        self.s = Main_guy_Sprite(self, self.x, self.y)
        self.font = pygame.font.SysFont("dejavusans", 54)
        self.text_render = self.font.render(str(self.health), 1, (250, 10, 10))

    def move(self, entityManager, map, direction):
        if direction == "right" and map.getTileData(self.x+1, self.y).isCollidable == False:
            if entityManager.entites[self.y][self.x+1] == 0:
                entityManager.entites[self.y][self.x+1] = entityManager.entites[self.y][self.x]
                entityManager.entites[self.y][self.x] = 0
                self.x = self.x + 1
            else:
                self.entity_collision(entityManager.entites[self.y][self.x+1])
                if entityManager.entites[self.y][self.x+1][1].get_active() == False:
                    entityManager.entites[self.y][self.x + 1] = 0
        elif direction == "left" and map.getTileData(self.x-1, self.y).isCollidable == False:
            if entityManager.entites[self.y][self.x-1] == 0:
                entityManager.entites[self.y][self.x-1] = entityManager.entites[self.y][self.x]
                entityManager.entites[self.y][self.x] = 0
                self.x = self.x - 1
            else:
                self.entity_collision(entityManager.entites[self.y][self.x-1])
                if entityManager.entites[self.y][self.x-1][1].get_active() == False:
                    entityManager.entites[self.y][self.x - 1] = 0
        elif direction == "down" and map.getTileData(self.x, self.y+1).isCollidable == False:
            if entityManager.entites[self.y+1][self.x] == 0:
                entityManager.entites[self.y+1][self.x] = entityManager.entites[self.y][self.x]
                entityManager.entites[self.y][self.x] = 0
                self.y = self.y + 1
            else:
                self.entity_collision(entityManager.entites[self.y+1][self.x])
                if entityManager.entites[self.y+1][self.x][1].get_active() == False:
                    entityManager.entites[self.y + 1][self.x] = 0

        elif direction == "up" and map.getTileData(self.x, self.y-1).isCollidable == False:
            if entityManager.entites[self.y-1][self.x] == 0:
                entityManager.entites[self.y-1][self.x] = entityManager.entites[self.y][self.x]
                entityManager.entites[self.y][self.x] = 0
                self.y = self.y - 1
            else:
                self.entity_collision(entityManager.entites[self.y-1][self.x])
                if entityManager.entites[self.y-1][self.x][1].get_active() == False:
                    entityManager.entites[self.y - 1][self.x] = 0
                #print(entityManager.entites[self.y-1][self.x][1].health)


    def entity_collision(self, entity):
        if entity[0] == "monster":
            entity[1].health -= self.attack
            if entity[1].health <= 0:
                entity[1].die()
            else:
                self.health -= entity[1].attack
            self.text_render = self.font.render(str(self.health), 1, (250, 10, 10))
            if self.health <= 0:
                self.die()
        elif entity[0] == "health_potion":
            self.health += 70
            if self.health > 100:
                self.health = 100
            self.text_render = self.font.render(str(self.health), 1, (250, 10, 10))
            entity[1].die()

    def render_text(self, display):
        display.blit(self.text_render, (0, 0))

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