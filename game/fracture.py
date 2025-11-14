from sort_tuple import ascSort
from numpy import random
import pygame
import math
import queue
class Fracture:
    def __init__(self):
        self.x=0
        self.y=0
        self.used_x = set()
        self.points_drawn = 0
        self.tri_coord=[]
        self.points_loc=[]
        self.pq=queue.PriorityQueue()
        self.x_points=[]
        self.count=0
    def bo_wat(self,points_arr,surface):
       
    #    print(points_arr)
       x_min = min(p[0] for p in points_arr)
       x_max = max(p[0] for p in points_arr)
       y_min = min(p[1] for p in points_arr)
       y_max = max(p[1] for p in points_arr)
       dx = x_max - x_min
       dy = y_max - y_min
       delta_max = max(dx, dy)
       mid_x = (x_min + x_max) / 2
       mid_y = (y_min + y_max) / 2
       A = (mid_x - 2 * delta_max, mid_y - delta_max)
       B = (mid_x, mid_y + 2* delta_max)
       C = (mid_x + 2 * delta_max, mid_y - delta_max)
       
       print(A,B,C)
       pygame.draw.polygon(surface,(0,0,255),[A,B,C],2)
       return 
    def min_distance(self,c1,c2):
     x1,y1=c1
     x2,y2=c2
     sum=(x2-x1)**2+(y2-y1)**2
     res=math.sqrt(sum)
     return res
    def draw(self, surface, max_points):
        if self.points_drawn >= max_points:
            return
        self.count=max_points
        self.x = random.randint(10, surface.get_width() - 10)
        attempts = 0
        while self.x in self.used_x and attempts < 10:
            self.x = random.randint(10, surface.get_width() - 10)
            attempts =attempts+1
        self.used_x.add(self.x)
        self.y = random.randint(10, surface.get_height() - 10)  
        pygame.draw.circle(surface,(255,0,0), (self.x, self.y), 2)
        self.points_loc.append((self.x,self.y))
        self.x_points.append(self.x)
        self.points_drawn =self.points_drawn+1
        return
    def voro_fract(self,surface):
         width=surface.get_width()
         height=surface.get_height()
        #  top=(0+self.x,0)
        #  left_end=((self.x,self.y+height))
        # #  print(self.dq,self.min_elem)
        #  pygame.draw.line(surface,(0,0,255),top,left_end,3)#sweep line  
         top=(0+self.x,0)
         left_end=((self.x,self.y+60))
        #  print(self.points_loc)
         if len(self.points_loc)==self.count:
          newarr=ascSort(self.points_loc)
          print(newarr[0],newarr[len(newarr)-1])
          self.bo_wat(newarr,surface)
         else:
            pass
         return