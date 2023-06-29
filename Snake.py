import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Slither Game')

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set up the snake
snake_size = 20
snake_speed = 10
snake_x = window_width / 2
snake_y = window_height / 2
snake_x_change = 0
snake_y_change = 0
snake_body = []
snake_length = 1

# Set up the food
food_size = 20
food_x = round(random.randrange(0, window_width - food_size) / 20) * 20
food_y = round(random.randrange(0, window_height - food_size) / 20) * 20

# Set up the game clock
clock = pygame.time.Clock()

# Game over flag
game_over = False

# Function to display the snake
def draw_snake(snake_body):
    for part in snake_body:
        pygame.draw.rect(window, BLACK, [part[0], part[1], snake_size, snake_size])

# Game loop
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_size
                snake_x_change = 0

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for boundaries
    if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
        game_over = True

    # Update the window
    window.fill(WHITE)
    pygame.draw.rect(window, GREEN, [food_x, food_y, food_size, food_size])

    # Update snake body
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Check for snake-food collision
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, window_width - food_size) / 20) * 20
        food_y = round(random.randrange(0, window_height - food_size) / 20) * 20
        snake_length += 1

    # Check for snake self-collision
    for part in snake_body[:-1]:
        if part == snake_head:
            game_over = True

    # Draw the snake
    draw_snake(snake_body)

    # Update the game window
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
