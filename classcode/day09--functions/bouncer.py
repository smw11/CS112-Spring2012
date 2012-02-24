import pygame
from pygame import draw
from random import randrange
from pygame.locals import *

tie_x, tie_y = 400,300
tie_dx, tie_dy = 1,1
def draw_tie(surf, pos, color=(255,255,255), size=40):
    "Draws a tie fighter"
    x,y = pos
    
    width = size/8

    draw.rect(surf, color, (x, y, width, size))
    draw.rect(surf, color, (x+(size-width), y, width, size))
    draw.rect(surf, color, (x, y+(size-width)/2, size, width))
    draw.circle(surf, color, (x+size/2, y+size/2), size/4)

def move(x, y, dx, dy, bounds):
    x+=dx
    y+=dy
    if x<bounds.left or x>bounds.right-40:
        dx*=-2
        x+=dx*2
    if y<bounds.top or y>bounds.bottom-40:
        dy*=-2
        y+=dy*2
    return x, y, dx, dy



pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
screen_bounds = screen.get_rect()

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    screen.fill((0,0,0))
    tie_x, tie_y,tie_dx,tie_dy = move(tie_x, tie_y, tie_dx, tie_dy, screen_bounds)
    draw_tie(screen, [tie_x, tie_y])
    
    pygame.display.flip()
    clock.tick(50)
    
print "ByeBye"
