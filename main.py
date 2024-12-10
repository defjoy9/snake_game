import pygame
import random


def generate_random_position(screen_width, screen_height, grid_size):
    x = random.randint(0, (screen_width // grid_size) - 1) * grid_size
    y = random.randint(0, (screen_height // grid_size) - 1) * grid_size
    return (x, y)


def draw_snake():
    for segment in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], grid_size, grid_size))



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock()
fps = 10

grid_size = 20
snake_body = [(340, 360), (320, 360), (300, 360)]
food_color = (255, 0, 0)
food_position = generate_random_position(1280, 720, grid_size)
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
        new_head = (snake_body[0][0] - grid_size, snake_body[0][1])
    elif direction == "RIGHT":
        new_head = (snake_body[0][0] + grid_size, snake_body[0][1])
    elif direction == "UP":
        new_head = (snake_body[0][0], snake_body[0][1] - grid_size)
    elif direction == "DOWN":
        new_head = (snake_body[0][0], snake_body[0][1] + grid_size)

    # Grid
    screen_width, screen_height = 1280, 720
    new_head = (
        new_head[0] % screen_width,
        new_head[1] % screen_height,
    )
    # Game over
    if new_head in snake_body:
        print("Game Over!")  # Display message in console
        running = False

    snake_body = [new_head] + snake_body[:-1]

    # Check if the snake eats the food
    if snake_body[0] == food_position:
        # Grow the snake
        snake_body.append(snake_body[-1])  # Add a new segment at the tail
        # Generate a new food position
        food_position = generate_random_position(1280, 720, grid_size)

    screen.fill("black")
    pygame.draw.rect(screen, food_color, pygame.Rect(food_position[0], food_position[1], grid_size, grid_size))
    draw_snake()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()