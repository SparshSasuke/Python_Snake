import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bullet Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_width, player_height = 50, 50
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height
player_speed = 5

# Bullet
bullet_width, bullet_height = 10, 20
bullet_x, bullet_y = 0, 0
bullet_speed = 10
bullet_state = "ready"  # "ready" - ready to fire, "fire" - bullet is moving

def player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_width, player_height))

def bullet(x, y):
    pygame.draw.rect(screen, RED, (x, y, bullet_width, bullet_height))

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullet_state = "fire"

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    if bullet_state == "fire":
        bullet_y -= bullet_speed
        bullet(bullet_x, bullet_y)
        if bullet_y <= 0:
            bullet_state = "ready"

    player(player_x, player_y)

    pygame.display.update()

# Quit the game
pygame.quit()
sys.exit()
