import pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Screen size
screen_width = 600
screen_height = 400

# Font
font_style = pygame.font.SysFont("bahnschrift", 25)

# Game window
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Snake block size
block_size = 10

# Clock
clock = pygame.time.Clock()

# Functions
def message(msg, color):
    msg = font_style.render(msg, True, color)
    game_window.blit(msg, [screen_width / 6, screen_height / 3])

def game_loop():
    # Initial position of snake
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Food position
    foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    # Game over flag
    game_over = False

    # Main game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Update snake position
        x1 += x1_change
        y1 += y1_change

        # Check for game over conditions
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_over = True

        # Draw the snake and food
        game_window.fill(black)
        pygame.draw.rect(game_window, green, [foodx, foody, block_size, block_size])
        pygame.draw.rect(game_window, white, [x1, y1, block_size, block_size])
        pygame.display.update()

        # Check if snake has eaten food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

        # Clock speed
        clock.tick(20)

    # End the game
    pygame.quit()
    quit()

# Start the game
game_loop()