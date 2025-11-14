""" """
from collections import Counter
def char_freq(cnt,res):
    """this is used to sort based on the character frequency and if same frequency sort based on alphabet order."""
    if len(cnt)<=0:
        return res
    val=0
    max_elem=max(cnt.values())
    if max_elem>1:
        for k,v in cnt.items():
            if v==max_elem:
                res+=k*max_elem
                val=k
            else:
                pass
    else:
        min_key=min(cnt.keys())
        res+=min_key  
        val=min_key
    cnt.pop(val)
    return  char_freq(cnt,res)    
S_T = "treehoouse"#"eeehorstu"
n_s=[i for i in S_T]
cont=Counter(n_s)
# print(cnt)
res1=char_freq(cont,"")
print(res1,end="\n")
