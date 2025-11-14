
# Expected Output:
# {
#     "Bob": {"age": 22, "score": 95},
#     "Charlie": {"age": 23, "score": 90},
#     "Alice": {"age": 25, "score": 88}
# }

def sort_dict(students:dict,key,res_dict):
     if len(students)<=0:
           return res_dict
     else:
          max_value=float("-inf")
          key=None
          for k,v in students.items():
                if students[k]['score']>max_value:
                  max_value=students[k]['score']
                  key=k
                else:
                  pass
          if students[key] and students[key]['score']==max_value:
                  res_dict[key]=students[key]['score']
          students.pop(key)
          return sort_dict(students,key,res_dict)
        
students = {
    "Alice": {"age": 25, "score": 88},
    "Bob": {"age": 22, "score": 95},
    "Charlie": {"age": 23, "score": 90},
     "eddie": {"age": 23, "score": 87},
      "georgie": {"age": 23, "score": 1000}
}
max_value=float('-inf')
print(sort_dict(students,None,{}))    
   

