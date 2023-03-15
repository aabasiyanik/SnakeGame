import pygame
import sys
import random

pygame.init()

# Oyun ekranının boyutları
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

# Renkler
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Yılan ve yem için başlangıç ​​koordinatları
snake_pos = [[100, 100], [80, 100], [60, 100]]
snake_speed = [CELL_SIZE, 0]
food_pos = [random.randrange(1, (WIDTH//CELL_SIZE)) * CELL_SIZE, random.randrange(1, (HEIGHT//CELL_SIZE)) * CELL_SIZE]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

def game_over():
    pygame.quit()
    sys.exit()

def draw_objects():
    screen.fill(WHITE)

    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_speed[1] != CELL_SIZE:
                snake_speed = [0, -CELL_SIZE]
            if event.key == pygame.K_DOWN and snake_speed[1] != -CELL_SIZE:
                snake_speed = [0, CELL_SIZE]
            if event.key == pygame.K_LEFT and snake_speed[0] != CELL_SIZE:
                snake_speed = [-CELL_SIZE, 0]
            if event.key == pygame.K_RIGHT and snake_speed[0] != -CELL_SIZE:
                snake_speed = [CELL_SIZE, 0]

        if event.type == pygame.QUIT:
            game_over()

    snake_pos.insert(0, [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]])

    if snake_pos[0] == food_pos:
        food_pos = [random.randrange(1, (WIDTH//CELL_SIZE)) * CELL_SIZE, random.randrange(1, (HEIGHT//CELL_SIZE)) * CELL_SIZE]
    else:
        snake_pos.pop()

    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over()

    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or
            snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT):
        game_over()

    draw_objects()
    pygame.display.update()
    clock.tick(10)