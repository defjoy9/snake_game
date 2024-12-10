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
clock = pygame.time.Clock()
fps = 10

radius = 10
snake_body = [(340, 360), (330, 360), (320, 360)]
circle_color = (255, 0, 0)
circle_position = generate_random_position(1280, 720, radius)
direction = "RIGHT"


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keyboard input for movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            elif event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

    # Move the snake
    if direction == "LEFT":
        new_head = (snake_body[0][0] - radius * 2, snake_body[0][1])
    elif direction == "RIGHT":
        new_head = (snake_body[0][0] + radius * 2, snake_body[0][1])
    elif direction == "UP":
        new_head = (snake_body[0][0], snake_body[0][1] - radius * 2)
    elif direction == "DOWN":
        new_head = (snake_body[0][0], snake_body[0][1] + radius * 2)


    screen_width, screen_height = 1280, 720
    new_head = (
        new_head[0] % screen_width,  # Wrap x-coordinate
        new_head[1] % screen_height  # Wrap y-coordinate
    )
    snake_body = [new_head] + snake_body[:-1]

    screen.fill("black")
    pygame.draw.circle(screen, circle_color, circle_position, radius)
    draw_snake()
    pygame.display.flip()

    clock.tick(fps) #speed

pygame.quit()