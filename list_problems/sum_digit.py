import math
def sum_digits(num:int,sum:int):
   if num<10:
      return num+sum
   else:
     q=num/10
     r=num%10
   #  print(q,r)
     sum+=r
     return sum_digits(math.floor(q),sum)


numbers = [11,20,56,89]
sum=[]
for i in numbers:
  sum.append(sum_digits(i,0)) 
 
print(sorted(sum))