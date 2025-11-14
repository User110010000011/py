import base64
import numpy as np
from decimal import Decimal,ROUND_HALF_DOWN
import math,copy
import cv2
# f(x, y) = xe−(x2 + y2)
# sum=x*math.exp(-(x^2+y^2))
# np.gradient()
print(cv2.__version__)
img=cv2.imread("test_img_1.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh_value,thresh_img=cv2.threshold(gray,139,255,cv2.THRESH_BINARY) #for normal threshold to binarize image
# thresh_img=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)#to binarize image for image 
                                                                                              # with varied lighting
# print(thresh_value)
contours,hierarchy=cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
ctr_img=img.copy()
val=-5.658026752876856e+40
value=Decimal(str(val)).quantize(Decimal('1'),rounding=ROUND_HALF_DOWN)
print(value)
print(img.shape)
# contour_list=contours[100]
print(contours[100:150])
for cnt in contours[0:100]:
   cv2.drawContours(ctr_img,[cnt],0,(0,255,0),2)
# cv2.resize(img,(600,480),interpolation=cv2.INTER_CUBIC)
   cv2.imshow("face_img",ctr_img)
cv2.waitKey(0)&ord('q')
cv2.destroyAllWindows()