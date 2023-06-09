import pygame
import sys
import random

pygame.init()

WIDTH = 595
HEIGHT = 595
CELL_SIZE = 35

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

initial_head_pos = [CELL_SIZE * 3, CELL_SIZE * 3]
snake_pos = [initial_head_pos, [initial_head_pos[0] - CELL_SIZE, initial_head_pos[1]], [initial_head_pos[0] - 2 * CELL_SIZE, initial_head_pos[1]]]

snake_speed = [CELL_SIZE, 0]

def generate_food_pos():
    while True:
        food_x = random.randrange(1, (WIDTH // CELL_SIZE)) * CELL_SIZE
        food_y = random.randrange(1, (HEIGHT // CELL_SIZE)) * CELL_SIZE
        new_food_pos = [food_x, food_y]
        if new_food_pos not in snake_pos:
            return new_food_pos

food_pos = generate_food_pos()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 30)

apple_image = pygame.image.load('apple.png')
apple_image = pygame.transform.scale(apple_image, (CELL_SIZE, CELL_SIZE))

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (150, 191, 13), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (150, 191, 13), (0, y), (WIDTH, y))

def game_over():
    message_font = pygame.font.SysFont(None, 40)
    message = message_font.render("Game Over! Press R to restart or Q to quit.", True, (135, 206, 235))
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    return False
            if event.type == pygame.QUIT:
                return False
        clock.tick(20)
        
def draw_objects():
    screen.fill((249, 255, 229))

    for pos in snake_pos:
        pygame.draw.rect(screen, (98, 189, 105), pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, GRAY, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE), 1)

    screen.blit(apple_image, (food_pos[0], food_pos[1]))
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    draw_grid()

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
            sys.exit()

    snake_pos.insert(0, [round(snake_pos[0][0] + snake_speed[0]), round(snake_pos[0][1] + snake_speed[1])])
    if snake_pos[0] == food_pos:
        food_pos = generate_food_pos()
        score += 1
    else:
        snake_pos.pop()

    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            if game_over():
                initial_head_pos = [CELL_SIZE * 3, CELL_SIZE * 3]
                snake_pos = [initial_head_pos, [initial_head_pos[0] - CELL_SIZE, initial_head_pos[1]], [initial_head_pos[0] - 2 * CELL_SIZE, initial_head_pos[1]]]
                snake_speed = [CELL_SIZE, 0]
                food_pos = generate_food_pos()
                score = 0
            else:
                sys.exit()

    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or
            snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT):
        if game_over():
            initial_head_pos = [CELL_SIZE * 3, CELL_SIZE * 3]
            snake_pos = [initial_head_pos, [initial_head_pos[0] - CELL_SIZE, initial_head_pos[1]], [initial_head_pos[0] - 2 * CELL_SIZE, initial_head_pos[1]]]
            snake_speed = [CELL_SIZE, 0]
            food_pos = generate_food_pos()
            score = 0
        else:
            sys.exit()

    draw_objects()
    pygame.display.update()
    clock.tick(20)