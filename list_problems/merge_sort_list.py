from collections import deque
set_check=set()

def merge_list(list1:list,list2:list,res:list):
    j=0
    if len(list1)==0 and  len(list2)==0:
        return res
    elif len(list1)==0:
        res.extend(list2)
        return res
    elif len(list2)==0:
        res.extend(list1)
        return res
    else:
        i=0
        if list1[i]<list2[j]:
            res.append(list1[i]) 
            list1.pop(i)
            i+=1
            return merge_list(list1,list2,res)
        else:
            i=0
            if list1[i]>list2[j]:
               res.append(list2[j])
               list2.pop(j)
               j+=1        
            return  merge_list(list1,list2,res)
                     
                

list1=[1,3,5]
list2=[2,4,6]
print(merge_list(list1,list2,[]))



           

