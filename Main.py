# Import statements
import pygame
import sys
import random

pygame.init()

# Variables for setup
SW, SH = 600, 600
BLOCK_SIZE = 50
pygame.font.SysFont('arial', BLOCK_SIZE * 2)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()

# Snake class with variables and methods
class Snake:
    def __init__(self):
        # Variables for the snakes body, head, if its dead and position
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        # Global variables
        global apple
        global boostApple

        # Check if the snake collided with itself, if it did it is dead
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
                self.dead = True

        # If the snake died restart the game with a new snake and new apples
        if self.dead:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            apple = Apple()

        # Place the snakes head into the body array and check if you have gotten any apples (body length) then reapply the head
        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

# Apple class with random variables for the spawnpoint
class Apple:
    def __init__(self):
        self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
    
    # Drawing the apple on the screen
    def update(self):
        pygame.draw.rect(screen, "red", self.rect)

# BoostedApple has inherited the same variables as Apple but i've overriddien the update method to make it blue
class BoostedApple(Apple):
    def update(self):
        pygame.draw.rect(screen, "blue", self.rect)

# Draw the grid for the game
def drawgrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)

# Creating game mechanics by calling the classes and creating instances
drawgrid()
snake = Snake()
apple = Apple()
boostApple = BoostedApple()

# Controlling the snake with controls using x and y positions
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1

    screen.fill('black')
    drawgrid()

    # Calling update methods for the game
    snake.update()
    apple.update()
    boostApple.update()

    # Draw the head of the snake
    pygame.draw.rect(screen, "green", snake.head)

    # Draw the body of the snake
    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    # Snake body extension 
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()

    # Snake body extension
    if snake.head.x == boostApple.x and snake.head.y == boostApple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        boostApple = BoostedApple()

    pygame.display.update()
    clock.tick(10)
