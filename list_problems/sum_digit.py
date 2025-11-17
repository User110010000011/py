"""sum digits """
import math
def sum_digits(num,sum):
    """this is used to sum digits """
    if num<10:
        return num+sum
    else:
        q=num/10
        r=num%10
   #  print(q,r)
        sum+=r
    return sum_digits(math.floor(q),sum)


numbers = [11,20,56,89]
sum2=[]
for i in numbers:
    sum2.append(sum_digits(i,0)) 
print(sorted(sum2))
