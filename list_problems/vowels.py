"""this is a vowel length count"""
import re
from collections import deque
words = ["banana", "mapleau","apple", 
         "grape","epple","aepple",
         "capleau", "kIwI", "strawberry","AEIOU","aeioua","aapleau"]
word_dict={}
dq=deque()
max_val=0
start_val=0
for i in words:
    count=0
    for j in i:
        if re.search("[aeiouAEIOU]+",j):
            count+=1
        word_dict[i]=count
# print(word_dict)
# obj=sorted(word_dict)     
# print(obj)
for key,val in word_dict.items():
    if val>max_val and val>start_val:
        dq.appendleft(key)
        start_val=val
        max_val=val 
    elif val>max_val and val<=start_val:
        cnt=0
        while start_val>val:
            start_val-=1
            cnt+=1               
        dq.insert(cnt,key)   
     # elif max_val==val:
     #        pass 
    else:
        dq.append(key)
        max_val=val
res=[]

for i in dq:
    res.append(i)
print(res)
  