import pygame
import map

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (10, 123, 10)
blue = (0, 0, 100)
bg_color = white

window_width = 600
window_height = 600
FPS = 30

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Sztuczna inteligencja')
clock = pygame.time.Clock()

mapa = map.Map()
mapa.load_from_file()

gameExit = False

test = pygame.Rect(332, 32, 32, 32)

while not gameExit: #game_loop
    for event in pygame.event.get(): #event_loop
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = True



    gameDisplay.fill(bg_color)
    pygame.draw.rect(gameDisplay, red, test, 0)
    mapa.Render(gameDisplay)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()
