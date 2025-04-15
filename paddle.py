import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Paddle properties
paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_vel = 0
acceleration = 0.6
friction = 0.85
max_speed = 12
base_max_speed = 8
speed_boost = 0.05  # Increment max speed while holding keys
scale_factor = 1.0  # Paddle scaling

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Input handling
    keys = pygame.key.get_pressed()
    is_moving = False
    if keys[pygame.K_LEFT]:
        paddle_vel -= acceleration
        is_moving = True
    if keys[pygame.K_RIGHT]:
        paddle_vel += acceleration
        is_moving = True

    # Adjust max speed for rewarding smooth control
    if is_moving:
        max_speed = min(max_speed + speed_boost, 12)
    else:
        max_speed = base_max_speed

    # Apply friction and clamp velocity
    paddle_vel *= friction
    paddle_vel = max(-max_speed, min(max_speed, paddle_vel))

    # Update paddle position
    paddle.x += paddle_vel

    # Keep paddle on screen
    if paddle.left < 0:
        paddle.left = 0
        paddle_vel = 0
    if paddle.right > WIDTH:
        paddle.right = WIDTH
        paddle_vel = 0

    # Visual scaling effect for "juice"
    scale_factor = 1.1 if is_moving else 1.0
    scaled_paddle = paddle.inflate((PADDLE_WIDTH * (scale_factor - 1)), 0)

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, scaled_paddle)
    pygame.display.flip()
    clock.tick(60)
