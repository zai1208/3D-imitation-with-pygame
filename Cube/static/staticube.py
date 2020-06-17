"""
Notes:
IMPORTANT: pygame screen must be pre-made with pygame code
e.g: surface = pygame.display.set_mode((100 -> width, 100 ->height))
then surface must be passed into the screen argument
1 - the color attribute must be a tuple such as (225, 0, 0) which is red
2 - the screen attribute  is what pygame surface to display it to 
"""
''' 
Note2: by default draws a red cube if color parameter & extras aren't passed in
'''
import pygame

def Cube((x, y, z), size, screen, color=(225, 0, 0), wireframe=False, outline=True, outline_width=0, outline_col=(225, 225, 225)):
   X,Y = size = screen.get_width(), screen.get_height()
   truex = x + size / 2
   truey = y - size / 2
   if z == 0 or z < 0:
       act_z = 1
   else:
       act_z = z
   truesize = act_z + size * act_z + 
   Pos = [
   (x + 10, y + 10), 
   (x + X / 2 + size, y + Y / 2 - size), 
   (20, 20), 
   (10, 20)
   ]
   Pos2 = [
   (Pos[0[0]] + size / 4, Pos[0[1]] + size / 4),
   (Pos2[0[0]] + size / 2, Pos2[0[1]]),
   (Pos2[1[0]], Pos2[1[1]] + size / 2), 
   (Pos2[0[0]], Pos2[0[1]] + size / 2)
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
   Pos1[2]
   ]
   if wireframe == False
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
