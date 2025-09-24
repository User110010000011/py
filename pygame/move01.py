import pygame
import numpy as np
import random
from pygame import gfxdraw,transform
import math
WIDTH =1000
HEIGHT =600
# line=pygame.draw.line()
SURF_COLOR = (100,200,200)
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface((60,60))
L_end=5
R_end=WIDTH-65
base_speed=5
high_speed=8
T_end=5
D_end=HEIGHT-65
edge_bound=[L_end,R_end,T_end,D_end]
surface.fill(SURF_COLOR)
# gfxdraw.rectangle(surface, (0, 0,50,50), (0, 0, 0))  # black borderw
#center=(425,265)
def collide(rect,rect2):
    x1,y1=rect
    x2,y2=rect2
    sum=(x2-x1)**2+(y2-y1)**2
    res=math.sqrt(sum)
    return math.ceil(res)
def rotate(x,y):
    theta=math.radians(2)
    matrix=np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])
    mat_2=np.array([x,y])
    # mat_T=np.transpose(mat_2)
    rotate=np.matmul(matrix,mat_2)
    x,y=rotate
    return x,y
def get_curr_pos():
      print(rect.x,rect.y)
# def other_block(rect,rect_2):
#     center_1=rect.center
#     print(center_1)
#     center_2=rect_2.center
#     print(center_2)
rect = pygame.Rect(0,400, 20,20)
# collide_rec=gfxdraw.rectangle(surface,rect,(0,0,0))
rect_2=pygame.Rect(300,200,10,10)
rect_3=pygame.Rect(300,500,10,10)
running = True
while running:
    center_rect=rect.center
    center_2=rect_2.center
    keys = pygame.key.get_pressed()
    ans=collide(center_rect,center_2)
    print(ans,center_rect,center_2)
    if ans>=80:
     if rect_2.y>T_end and rect_2.y<=D_end and running: 
       rect_2.y-=10
       rect_2.y+=10
     if keys[pygame.K_a] and rect.x>L_end:
          if keys[pygame.K_RSHIFT]:
              rect.x-=high_speed
          rect.x -=base_speed
        
     if keys[pygame.K_d] and rect.x<=R_end:
          if keys[pygame.K_RSHIFT]:
              rect.x+=high_speed
          rect.x +=base_speed
     if keys[pygame.K_w] and rect.y>T_end:
        if keys[pygame.K_RSHIFT]:
              rect.y-=high_speed
        rect.y -=base_speed
        # transform.rotate(surface,360.0)
     if keys[pygame.K_s] and rect.y<=D_end:
         if keys[pygame.K_RSHIFT]:
              rect.y+=base_speed
         else:
          rect.y +=high_speed
     if keys[pygame.K_RCTRL] and rect.y<=D_end and rect.y>T_end and rect.x<=R_end and rect.x>L_end:
         rect.x,rect.y=rotate(rect.x,rect.y)
     if keys[pygame.K_SPACE]:
         if keys[pygame.KEYDOWN]:
             rect.y-=10
         else:
              theta=math.radians(4)
              rect.y+=math.sin(theta)
    else:
         rect.x,rect.y=rotate(rect.x,rect.y)
        # pygame.transform.flip(rect,True)
    screen.fill((128, 255, 128))  
    screen.blits([(surface,rect),(surface,rect_2),(surface,rect_3)]) 
    pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
