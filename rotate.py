import numpy as np
import math
def distance(c1,c2):
     x1,y1=c1
     x2,y2=c2
#    pythogras=np.hypot()
#center:rec1=(10, 410),rec2=(315, 215)
# (10, 410) (315, 215)
     sum=(x2-x1)**2+(y2-y1)**2
     res=math.sqrt(sum)
     print(res)
def normal_vec_2d(p1,p2):
 x1,y1=p1[0],p1[1]
 x2,y2=p2[0],p2[0]
 direction_vector=(x2-x1,y2-y1)
 normal_clock=(-(y2-y1),x2-x1)
 normal_counter=(y2-y1,-(x2-x1))
 #unit_normal_vec=normal_clock/math.sqrt(normal_clock[0]^2+normal_clock[1]^2)
def gravity():
     pass
x=10
y=25
w,h=7,8
theta=math.radians(60.0)
matrix=np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])
mat_2=np.transpose([x,y])
rotate=np.matmul(matrix,mat_2)
x,y=rotate
print(x,y)
print(matrix)
distance((10,410),(315,215))