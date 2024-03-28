# 1 - Import library
import pygame
from pygame.locals import *
from random import randint

# 2 - Initiera spelet
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
width, height = 64*10, 64*8
screen=pygame.display.set_mode((width, height))

# Player variabler
player_x = 256
player_y = 440
keys = [False, False, False, False]

# Wall variabler
wall_y = -64
rand_wall = randint(0,8)
nmbr_of_walls = 0
wall_speed = 2

# Kolla om spelet är över eller inte
is_game = False

# 3 - Ladda bilder
player = pygame.image.load("zombie.png")
wall = pygame.image.load("wall.png")

def wall_render(rand, wall_y):
    for i in range(0, 10):
        if not (i == rand or i == rand + 1):
            screen.blit(wall, (i*64, wall_y))

def wall_handler(wall_y, rand, nmbr_of_walls, wall_speed):
    wall_y += wall_speed
    if wall_y > height:
        wall_y = -64
        rand = randint(0,8)
        nmbr_of_walls += 1
        wall_speed +=1

    return wall_y, rand, nmbr_of_walls, wall_speed  

def collide(player_x, player_y, wall_y, rand_wall):
    if (player_y >= wall_y and player_y <= wall_y + 64) and\
        ((player_x > 0 and player_x <= rand_wall*64) or (player_x > (rand_wall+1)*64 and player_x < width+64)):
        return True
    else:
        return False

# 4 - Loopa igenom spelet
while 1:
    if not is_game:
        screen.fill((255,255,255))
        textsurface = myfont.render("Press enter to start", False, (0, 0, 0))
        screen.blit(textsurface,(180, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key==K_RETURN:
                    player_x = 256
                    player_y = 440
                    wall_y = -64
                    rand_wall = randint(0,8)
                    nmbr_of_walls = 0
                    keys = [False, False, False, False]
                    wall_speed = 2
                    is_game = True
    else:
        # 5 - Rensa skärmen innan vi ritar ut igen
        screen.fill((255,255,255))
        # 6 - Rita alla element på skärmen (Spelare, vägg)
        screen.blit(player, (player_x, player_y))

        textsurface = myfont.render(str(nmbr_of_walls), False, (0, 0, 0))
        screen.blit(textsurface,(10, 0))

        wall_y, rand_wall, nmbr_of_walls, wall_speed = wall_handler(wall_y, rand_wall, nmbr_of_walls, wall_speed)
        wall_render(rand_wall, wall_y)

        if collide(player_x, player_y, wall_y, rand_wall):
            is_game = False

        # 7 - Updatera skärmen
        pygame.display.flip()
        # 8 - Loopa igenom alla event
        for event in pygame.event.get():
            # kolla om eventet är X button
            if event.type == pygame.QUIT:
                # Om det är, quit the game
                pygame.quit() 
                exit(0) 
            if event.type == pygame.KEYDOWN:
                if event.key==K_UP:
                    keys[0]=True
                elif event.key==K_LEFT:
                    keys[1]=True
                elif event.key==K_DOWN:
                    keys[2]=True
                elif event.key==K_RIGHT:
                    keys[3]=True

            if event.type == pygame.KEYUP:
                if event.key==pygame.K_UP:
                    keys[0]=False
                elif event.key==pygame.K_LEFT:
                    keys[1]=False
                elif event.key==pygame.K_DOWN:
                    keys[2]=False
                elif event.key==pygame.K_RIGHT:
                    keys[3]=False

        if keys[0]:
            if player_y > 0:
                player_y -= 15
        elif keys[2]:
            if player_y < height-64:
                player_y += 15 
        if keys[1]: 
            if player_x > 0:
                player_x -= 15
        elif keys[3]:
            if player_x < width-64:
                player_x += 15