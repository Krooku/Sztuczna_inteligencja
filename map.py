import pygame
import potions
import entity
import main_guy

TILESIZE = 32

BUSH_1 = '0'
BUSH_2 = '1'
ROCK_2 = '3'
ROCK_3 = '4'
WALL = '5'
SAND = '.'

# textury
textures = {
    str(BUSH_1): pygame.transform.scale(pygame.image.load("img/bush1.png"), (TILESIZE, TILESIZE)),
    str(BUSH_2): pygame.transform.scale(pygame.image.load("img/bush2.png"), (TILESIZE, TILESIZE)),
    str(WALL): pygame.transform.scale(pygame.image.load("img/wall.png"), (TILESIZE, TILESIZE)),
    str(SAND): pygame.transform.scale(pygame.image.load("img/sand.png"), (TILESIZE, TILESIZE)),
}

class Map:
    def __init__(self):
        self.game = 0
        self.width = 0
        self.height = 0
        self.tile_size = 0
        self.map_data = []
        self.tiles_data = [[]]  # [[0 for j in range(self.width)] for i in range(self.height)]


    def draw_map(self, screen, entity_manager):
        for row in range(self.width):
            for column in range(self.height):
                temp_key = self.map_data[column][row]
                if temp_key in textures:
                    screen.blit(self.tiles_data[column][row].image, (row*TILESIZE, column*TILESIZE))
                if entity_manager.entites[column][row] != 0:
                    screen.blit(entity_manager.entites[column][row].s.image, (row * TILESIZE, column * TILESIZE))



    def init_tile_objects(self, entity_manager):
        for row in range(self.height):
            for column in range(self.width):
                temp_key = self.map_data[row][column]
                # print(temp_key, end='')
                if temp_key == '0':
                    self.tiles_data[row][column] = Bush(self.game, column, row, 1)
                if temp_key == '1':
                    self.tiles_data[row][column] = Bush(self.game, column, row, 2)
                if temp_key == '5':
                    self.tiles_data[row][column] = Wall(self.game, column, row, 1)
                if temp_key == '.':
                    self.tiles_data[row][column] = Sand(self.game, column, row, 1)
                entity_manager.entites[row][column] = 0
        print(self.tiles_data)


    # wczytywanie mapy z pliku
    def load_from_file(self, entity_manager, file_name = "test.map"):
        self.map_data = []
        temp_arr = []
        with open("maps/" + file_name, "rt") as file:
            state = 0  # 0 - wymiary,
            for line in file:
                if state == 0:
                    size = line.replace("\n", "").split(";")
                    self.width = int(size[0])
                    self.height = int(size[1])
                    self.tile_size = int(size[2])
                    self.tiles_data = [[0 for j in range(self.width)] for i in range(self.height)]
                    entity_manager.entites = [[0 for j in range(self.width)] for i in range(self.height)]
                    state = 1
                    continue
                if state == 1:
                    if line[0] == "#":
                        state = 2
                        continue
                    self.map_data.append(line.replace("\n", "").split(" "))
                if state == 2:
                    if line[0] == "#": break
                    temp_arr.append(list(map(int, line.replace("\n", "").split(";"))))
        print(self.map_data)
        self.init_tile_objects(entity_manager)

        for line_arr in temp_arr:
            if line_arr[0] == 0:
                obj = potions.Health_Potion(line_arr[1], line_arr[2])
                entity_manager.add(obj, line_arr[1], line_arr[2])
                self.getTileData(obj.x, obj.y).setOccupiedBy(obj)
            if line_arr[0] == 1:
                obj = entity.Slime(line_arr[1], line_arr[2])
                entity_manager.add(obj, line_arr[1], line_arr[2])
                self.getTileData(obj.x, obj.y).setOccupiedBy(obj)
            if line_arr[0] == 2:
                obj = main_guy.Main_guy(line_arr[1], line_arr[2])
                entity_manager.add(obj, line_arr[1], line_arr[2])
                self.getTileData(obj.x, obj.y).setOccupiedBy(obj)

    def getTileData(self,x,y):
        return self.tiles_data[y][x]

    def getTiles_data(self):
        return self.tiles_data

    def Render(self, display):
        for row in range(self.height):
            for column in range(self.width):
                pygame.draw.rect(display, self.tiles_data[row][column][1], self.tiles_data[row][column][0], 0)

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, tileX, tileY, texture):
        self.logic_attribute_name_list = ['x', 'y', 'name', 'id', 'isCollidable', 'logic_attribute_name_list','characterOccupyingTile'];
        self.game = game
        # self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, pygame.sprite.Group())
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image = texture
        self.rect = self.image.get_rect()
        #ATRYBUTY LOGICZNE
        self.x = tileX
        self.y = tileY
        self.name = self.__class__.__name__
        self.id = id(self)
        self.isCollidable = None;

        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        self.entityOccupyingTile = None

        # # zmienne potrzebne do A*
        # self.h = 0
        # self.g = 0
        # self.f = 0

    # rzeczy logicznie, x, y, nazwa
    def __getstate__(self):
        state = self.__dict__.copy()
        try:
            newstate = {k: state[k] for k in self.logic_attribute_name_list}
        except AttributeError:
            newstate = {k: state[k] for k in ['x', 'y', 'name', 'id', 'isCollidable', 'logic_attribute_name_list']}
        return newstate

    def __setstate__(self, state):
        self.__dict__.update(state)

    def setOccupiedBy(self, entity):
        self.entityOccupyingTile = entity

    def isOccupied(self):
        return self.entityOccupyingTile is not None

class Sand(Tile):
    def __init__(self, game, tileX, tileY, type):
        self.textures = {
            1: pygame.transform.scale(pygame.image.load("img/sand.png"), (TILESIZE, TILESIZE)),
        }
        Tile.__init__(self, game, tileX, tileY, self.textures[type])
        self.isCollidable = False
        self.moveCost = 1

class Bush(Tile):
    def __init__(self, game, tileX, tileY, type):
        self.textures = {
            1: pygame.transform.scale(pygame.image.load("img/bush1.png"), (TILESIZE, TILESIZE)),
            2: pygame.transform.scale(pygame.image.load("img/bush2.png"), (TILESIZE, TILESIZE)),
        }
        Tile.__init__(self, game, tileX, tileY, self.textures[type])
        self.isCollidable = True

class Wall(Tile):
    def __init__(self, game, tileX, tileY, type):
        self.textures = {
            1: pygame.transform.scale(pygame.image.load("img/wall.png"), (TILESIZE, TILESIZE)),
        }
        Tile.__init__(self, game, tileX, tileY, self.textures[type])
        self.isCollidable = True
