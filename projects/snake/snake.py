



import pygame
import sys

# Initialize pygame
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


# Clock to control game speed
clock = pygame.time.Clock()


# Snake Settings 
snake_size = 20
snake_x = WIDTH//2
snake_y = HEIGHT//2
snake_speed = 20

# Movement direction
dx = 0
dy = 0



# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Movement keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -snake_size
                dy = 0
            if event.key == pygame.K_RIGHT:
                dx = snake_size
                dy = 0 
            if event.key == pygame.K_UP:
                dx = 0
                dy = -snake_size
            if event.key == pygame.K_DOWN:
                dx = 0
                dy = snake_size 
                
    # Update snake position
    snake_x += dx
    snake_y += dy
    
    # Fill screen
    screen.fill((0, 0, 0))

    # Draw snake 
    pygame.draw.rect(screen,(0, 255, 0), (snake_x, snake_y, snake_size, snake_size))
    
    pygame.display.update()
    clock.tick(10)

pygame.quit()
sys.exit()