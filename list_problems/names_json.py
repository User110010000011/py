import os
import json
import re
path="./sample"
path_check=os.listdir("C:/Users/Shailesh_D7/gitdocs")
# print(path_check)
if "sample" not in path_check:
 os.mkdir(path)

word=input("write name:")
#  field=input("fieldname:")
fmt=r"this person name is (?P<username>\w+)"#Regex Group:use this to give group <key> and use the group(key) to get the value.4
try:
  with open("./sample/names.txt","w") as fil:
    fil.writelines(f"this person name is {word}")
  
  with open("./sample/names.txt","r") as fil:
    text=fil.readlines()
  line="".join(text)
  name=re.search(fmt,line).group("username")

#  print(line,txt)
# name=txt.groups(('fieldname','username'))
# print(txt.group('username'))
     
  if not re.fullmatch(r"[A-Za-z]+", name) and 3<=len(name)<=26:
    print("intergers and special characters not allowed")  
  else:
   with open("./name.json",'w') as fil:
    json_data={"name":name} 
    json.dump(json_data,fil)

except Exception as e:
  raise ValueError("None or invalid group name and values error")
             
          