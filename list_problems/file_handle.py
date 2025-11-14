# file="example.txt"
# with open(file,'w') as fil:
#      fil.writelines("Hello this is a New World and it is A new world")
from collections import Counter
file="./example.txt"
word_set={}
result_list=[]
with open(file,'r') as fil:
    res=fil.read() 
new_list=[]
res_list=res.split(" ")
for i in res_list:
    new_list.append(i.title())

count_dict=Counter(new_list)
res_dict={}
for key,val in count_dict.items():
    res_dict[key]=val

print(res_dict)


