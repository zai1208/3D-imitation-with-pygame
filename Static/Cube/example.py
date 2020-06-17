import staticube as py3d
import pygame
screen = pygame.display.set_mode((100, 100))

while True:
    py3d.Cube(100, screen, 10, 10, 10)
