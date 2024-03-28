import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

#Bestäm storleken på spelplanen
width, height = 64*10, 64*8

screen = pygame.display.set_mode((width, height))

player_x = 200
player_y = 200
keys = [False, False, False, False]

player = pygame.image.load("zombie.png")

while 1:
    # Rita ut en vit spelplan
    screen.fill((255, 255, 255))

    # Rita ut bilden player på en x, y koordinat
    screen.blit(player, (player_x, player_y))

    # Updatera spelplanen
    pygame.display.flip()

    for event in pygame.event.get(): # Kolla om spelplanen stängs ner. I så fall, stäng av programmet
        if event.type == pygame.QUIT: # Om det är fallet avsluta programmet helt
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_LEFT:
                keys[1] = False
            elif event.key == pygame.K_DOWN:
                keys[2] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False
            # Updatera y-positionen
        # Updatera y-positionen
        if keys[0]:  # Om uppåtknappen är intryckt
            if player_y > 0:  # Om koordinaten är större än 0 (ej utanför spelplanen)
                player_y -= 15  # Ändra y-positionen med 15 pixlar. Spelaren åker uppåt
        elif keys[2]:  # Om nedåttangenten är intryckt
            if player_y < height-64:  # Om koodinaten är mindre än höjden på spelplanen (ej utanför spelplanen)
                player_y += 15  # Ändra y-positionen med 15 pixlar. Spelaren åker nedåt
        if keys[1]:  # Om vänster tangent är nedtryckt
            if player_x > 0:  # Om spelaren är innanför spelplanen
                player_x -= 15  # Minska positionen i x-led. Spelaren åker vänster
        elif keys[3]:  # Om höger tangent är nedtryckt
            if player_x < width-64:  # Om spelaren är innanför spelplanen
                player_x += 15  # Öka positionen i x-led. Spelaren åker höger