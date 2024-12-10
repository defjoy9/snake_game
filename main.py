import pygame
import random


def generate_random_position(screen_width, screen_height, radius):
    x = random.randint(radius, screen_width - radius)
    y = random.randint(radius, screen_height - radius)
    return (x, y)

def draw_snake():
    for segment in snake_body:
        pygame.draw.circle(screen, (0, 255, 0), segment, radius)
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

radius = 10
snake_body = [(340, 360), (330, 360), (320, 360)]
circle_color = (255, 0, 0)
circle_position = generate_random_position(1280, 720, radius)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    pygame.draw.circle(screen, circle_color, circle_position, radius)

    # snake body
    draw_snake()

    pygame.display.flip()
pygame.quit()