import pygame
import sys
from simulation import Simulation

pygame.init()

infoObject = pygame.display.Info()

width = infoObject.current_h
screen = pygame.display.set_mode((width, width))
pygame.display.set_caption("Turing Patterns")

clock = pygame.time.Clock()
simulation = Simulation(screen, 40, width)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((254, 248, 250))  # black
    simulation.update()
    simulation.display()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
