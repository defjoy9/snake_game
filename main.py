import pygame
import random


def draw_random_circle(screen, color, radius, screen_width, screen_height):
    x = random.randint(radius, screen_width - radius)
    y = random.randint(radius, screen_height - radius)
    return pygame.draw.circle(screen,color, (x, y), radius, 0)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    draw_random_circle(screen, (0, 255, 0), 10, 1280, 720)
    pygame.display.flip()
pygame.quit()