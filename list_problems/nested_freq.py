# Nested Frequency Counter
# Problem:
from collections import ChainMap
# from collections import OrderedDict
data = [
    {"city": "New York", "fruit": "apple"},
    {"city": "Paris", "fruit": "apple"},
    {"city": "Paris", "fruit": "banana"},
    {"city": "Paris", "fruit": "banana"},
    {"city": "New York", "fruit": "apple"},
    {"city": "Paris", "fruit": "orange"}
    
]
# 👉 Create a dictionary that shows how many times each fruit appeared per city.
# Expected Output:
# {
#   "New York": {"apple": 2},
#   "Paris": {"apple": 1, "banana": 1}
# }

res_dict={}
 
for elem in data:
    if elem['city'] not in res_dict:
        res_dict[elem['city']]={}
    if elem['fruit'] not in res_dict.get(elem['city']):
        res_dict[elem['city']][elem.get('fruit')]=1
    else:
        res_dict[elem['city']][elem.get('fruit')]+=1


print(res_dict)
                
