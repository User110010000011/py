import pygame
import numpy as np
import random
from fracture import Fracture
from decimal import Decimal,ROUND_HALF_DOWN
import math
WIDTH =800
HEIGHT =600
fract=Fracture()
SURF_COLOR = (100,200,200)
pygame.init()
is_collide=False
def assign_surf_tri():
     pass
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface((60,60))
surf2_x,surf2_y=80,80
surface_2=pygame.Surface((surf2_x,surf2_y))
L_end=5
R_end=WIDTH-65
base_speed=4
high_speed=6
T_end=5
cnt_THRESH=20
D_end=HEIGHT-65
edge_bound=[L_end,R_end,T_end,D_end]
surface.fill(SURF_COLOR)
surface_2.fill((0,255,0))
# mask=np.zeros((100,100),np.uint8)
cnt=0
avg=0
min_arr=[]
set_X=set()
set_Check=set()
sorted_arr=[]
min_sorted=None

def triangluate():
    surface_3=pygame.Surface((85,85))
def normal_vec_2d(p1,p2):
 x1,y1=p1
 x2,y2=p2
 direction_vector=(x2-x1,y2-y1)#direction
 normal_clock=(-(y2-y1),x2-x1)#inward
 normal_counter=(y2-y1,-(x2-x1))#outward
 pygame.draw.line(surface_2,(0,0,255),(surf2_x,surf2_y),normal_clock,3)
 print(normal_counter)
 return
 #unit_normal_vec=normal_clock/math.sqrt(normal_clock[0]^2+normal_clock[1]^2)    

def collide(rect,rect2):
    offset=3
    x1,y1=rect
    x2,y2=rect2
    sum=(x2-x1)**2+(y2-y1)**2
    res=math.sqrt(sum)
    return math.ceil(res)+offset
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

rect = pygame.Rect(0,400, 20,20)

rect_2=pygame.Rect(300,200,50,80)
rect_3=pygame.Rect(300,500,10,10)
running = True
while running:
    center_rect=rect.center
    center_2=rect_2.center
    keys = pygame.key.get_pressed()
    ans=collide(center_rect,center_2)
   
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
       
     if keys[pygame.K_s] and rect.y<=D_end:
         if keys[pygame.K_RSHIFT]:
              rect.y+=base_speed
         else:
          rect.y +=high_speed
     if keys[pygame.K_RCTRL] and rect.y<=D_end and rect.y>T_end and rect.x<=R_end and rect.x>L_end:
         rect.x,rect.y=rotate(rect.y,rect.x)
     if keys[pygame.K_SPACE]:
         if keys[pygame.KEYDOWN]:
             rect.y-=10
         else:
              theta=math.radians(4)
              rect.y+=math.sin(theta)
    else:
        center_player = rect.center
        center_box = rect_2.center
        dist = fract.min_distance(center_player, center_box)
        thresh = collide(rect.center, rect_2.center)

        if dist <= thresh:
            is_collide = True
          
            x, y = rotate(rect.x, rect.y,)
            rect.x, rect.y = int(x), int(y)
        else:
            is_collide = False
    screen.fill((128, 255, 128)) 
    # if cnt<cnt_THRESH and is_collide==True:
    #     fract.draw(surface_2,cnt_THRESH)
    #     cnt=cnt+1
    if is_collide:
        fract.draw(surface_2,cnt_THRESH)
        fract.voro_fract(surface_2)
    else:
        pass
#------ normal_vec_2d((surf2_x,0),(surf2_x,surf2_y))-------
    # img_str=pygame.image.tostring(surface,'RGB')
    # img_frame=np.frombuffer(img_str,dtype=np.uint8).reshape((60,60,3)) 
    # img_frame.reshape((30,15,3))
    # print(img_frame[0])
    # rand_points_in_object(rect_2)
    screen.blits([(surface,rect),(surface_2,rect_2),(surface_2,rect_3)]) 
    pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()


