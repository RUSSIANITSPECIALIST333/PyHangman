import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 1917
HEIGHT = 1017
SPEED = 2

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the rectangle
rect = pygame.Rect(WIDTH / 2, HEIGHT / 2, 50, 50)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the rectangle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rect.y -= SPEED
    if keys[pygame.K_DOWN]:
        rect.y += SPEED
    if keys[pygame.K_LEFT]:
        rect.x -= SPEED
    if keys[pygame.K_RIGHT]:
        rect.x += SPEED

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), rect)
    pygame.display.flip()