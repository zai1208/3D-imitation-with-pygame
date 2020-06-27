import staticube as py3d
import pygame
import sys
screen = pygame.display.set_mode((400, 400))
wireframe = True
outline = True
size = 200
color = (225, 0, 0)
outline_width = 10
while True:
    screen.fill((0, 0, 0))
    py3d.Cube(size, screen, 75, 75, -10, (225, 0, 0), False, True, 1, (225, 225, 225))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
