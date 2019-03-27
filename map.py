import pygame

class Map:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.tile_size = 0
        self.map_data = []
        self.tiles_data = [[]]#[[0 for j in range(self.width)] for i in range(self.height)]

    def init_tile_objects(self):
        for row in range(self.height):
            for column in range(self.width):
                temp_key = self.map_data[row][column]#Te ify, żeby kompilowało się :D W razie czego znajdzie się coś lepszego
                # print(temp_key, end='')
                if temp_key == '0':
                    self.tiles_data[row][column] = (pygame.Rect(column * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size), (255,0,0))
                if temp_key == '1':
                    self.tiles_data[row][column] = (pygame.Rect(column * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size), (255,0,0))
                if temp_key == '2':
                    self.tiles_data[row][column] = (pygame.Rect(column * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size), (255,0,0))
                if temp_key == '3':
                    self.tiles_data[row][column] = (pygame.Rect(column * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size), (255,0,0))
                if temp_key == '4':
                    self.tiles_data[row][column] = (pygame.Rect(column * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size), (0,0,0))
                if temp_key == '5':
                    self.tiles_data[row][column] = (pygame.Rect(column * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size), (0,0,255))
                if temp_key == '.':
                    self.tiles_data[row][column] = (pygame.Rect(column * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size), (0,255,0))
        print(self.tiles_data)


    # wczytywanie mapy z pliku
    def load_from_file(self, file_name = "test.map"):
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
        self.init_tile_objects()

    def getTiles_data(self):
        return self.tiles_data

    def Render(self, display):
        for row in range(self.height):
            for column in range(self.width):
                pygame.draw.rect(display, self.tiles_data[row][column][1], self.tiles_data[row][column][0], 0)
