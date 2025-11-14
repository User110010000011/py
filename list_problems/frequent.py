# from collections import Counter
from collections import deque
def freqsorted(results,ans):
    """this is frquency sort program."""
    if len(results)<=0:
        return ans

    max_num=float("-inf")
    val=None
    for k,v in results.items():
        if v>max_num:
            max_num=v
            val=k
        else:
            pass
        ans.append(val)
        results.pop(val)
        return freqsorted(results,ans)   
if __name__=='main':
    set_check=set()
    result={}       
    data = [5, 1, 2, 1, 3, 2, 2, 5, 5, 5]
    dq=deque()
    for i in data:
        if i not in set_check:
            result[i]=1
            set_check.add(i)
        else:
            result[i]+=1
print(freqsorted(result,[]))

# res=sorted(frequency,key=lambda x:frequency[x],reverse=True)

# print(res)
    