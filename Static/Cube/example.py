import staticube as py3d
import pygame
import sys
screen = pygame.display.set_mode((100, 100))
wireframe = True
outline = True
size = 100
color = (225, 0, 0)
outline_width = 10
Pos = [(10, 10), (100 / 2 + size, 100 / 2 - size), (20, 20), (10, 20)]
Pos2 = [
(10 + size / 4, 10 + size / 4),
((10 + size / 4) + size / 2, 10 + size / 4),
((10 + size / 4) + size / 2, (10 + size / 4) + size / 2),
(10 + size / 4, (10 + size / 4) + size / 2)
]
Pos3 = [
Pos[0],
Pos2[0],
Pos2[3],
Pos[3]
]
Pos4 = [
Pos[1],
Pos2[1],
Pos2[2],
Pos[2]]
Pos5 = [
Pos[0],
Pos2[0],
Pos2[1],
Pos[1]
]
Pos6 = [
Pos[3],
Pos2[3],
Pos2[2],
Pos[2]
]
while True:
    screen.fill((0, 0, 0))
    if wireframe == False:
       # first side (the front)
       front = pygame.draw.polygon(screen, color, Pos)

       # Second side (the back)

       back = pygame.draw.polygon(screen, color, Pos2)

       # Third side (the left)

       left = pygame.draw.polygon(screen, color, Pos3)

       # Fourth side (the right)


       right = pygame.draw.polygon(screen, color, Pos4)
       # fifth side (the top)

       top = pygame.draw.polygon(screeen, color, Pos5)

       # sixth side(the bottom)
       pygame.draw.polygon(screen, color, Pos6)
    if outline == True:
      # outlines drawn if wanted
      pygame.draw.lines(screen, (225, 225, 225), Pos, width=outline_width)
      pygame.draw.lines(screen, (225, 225, 225), Pos2, width=outline_width)
      pygame.draw.lines(screen, (225, 225, 225), Pos3, width=outline_width)
      pygame.draw.lines(screen, (225, 225, 225), Pos4, width=outline_width)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
