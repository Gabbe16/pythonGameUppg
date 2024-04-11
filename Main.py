import pygame
import sys
import random

pygame.init()

SW, SH = 600, 600

BLOCK_SIZE = 50
pygame.font.SysFont('arial', BLOCK_SIZE*2)

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)

drawGrid()

snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)
        # 7.00

    pygame.display.update()
    clock.tick(10)
