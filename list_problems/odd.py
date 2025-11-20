def  odd_even(num_list,size):
    """ """
    res={"odd":[],"even":[]}
    for num in num_list:
        if num%2==0:
            res.get('even').append(num)
        else:
            res.get('odd').append(num)
    return res

size=int(input("enter the size of list:"))
num_list=[]
for i in range(1,size+1):
   num_list.append(int(input(f"enter values {i}:")))

print(odd_even(num_list,size))


