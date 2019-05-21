import pygame
import map
import main_guy
import entity_manager

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (10, 123, 10)
blue = (0, 0, 100)
bg_color = white

window_width = 640
window_height = 320
FPS = 30

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Sztuczna inteligencja')
clock = pygame.time.Clock()

entity_manager = entity_manager.Entity_manager()
mapa = map.Map()
mapa.load_from_file(entity_manager)

gameExit = False

guy = entity_manager.find("main_guy")
font = pygame.font.SysFont("dejavusans", 54)
end_text = font.render("NIE ZYJESZ", 1, (250, 255, 255))
while not gameExit: #game_loop
    for event in pygame.event.get(): #event_loop
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                #entity_manager.find("main_guy").move(entity_manager, mapa, "right")
                if guy.active == True:
                    guy.move(entity_manager, mapa, "right")
            elif event.key == pygame.K_LEFT:
                if guy.active == True:
                    guy.move(entity_manager, mapa, "left")
            elif event.key == pygame.K_DOWN:
                if guy.active == True:
                    guy.move(entity_manager, mapa, "down")
            elif event.key == pygame.K_UP:
                if guy.active == True:
                    guy.move(entity_manager, mapa, "up")
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = True


    gameDisplay.fill(bg_color)
    mapa.draw_map(gameDisplay, entity_manager)
    guy.render_text(gameDisplay)
    if guy.active == False:
        gameDisplay.blit(end_text, (window_width / 2 - end_text.get_width() / 2, window_height / 2 - end_text.get_height() / 2))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()
