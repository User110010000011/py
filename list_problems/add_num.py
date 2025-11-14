def sums(inputs):
    ins=str(inputs)
    if len(ins)<=1:
         return ins
    else:
     sum=0
     for i in ins:
        sum+=int(i)
   
    return sums(sum)
inputs=int(input("enter the inputs: "))
res=sums(inputs)
print(res)
