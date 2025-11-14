import re
def sort_words(arr,size):
   for i in range(0,size):
        for j in range(i+1,size):
            if len(arr[j])<len(arr[i]):
                arr[i],arr[j]=arr[j],arr[i]
            elif len(arr[j])==len(arr[i]):
                if ord(arr[j][0:1])<ord(arr[i][0:1]):
                    arr[i],arr[j]=arr[j],arr[i]
            
   return arr

words_size=int(input(f"enter the list size:"))
str_list=[]

for i in range(1,words_size+1):
    word_in=input(f"enter the word {i}:")
    if re.fullmatch(r"[a-zA-Z]+",word_in): 
        str_list.append(word_in)
    else:
        raise ValueError("numbers and special letters not allowed")

print(f"previous word list:{str_list}")
print(f"changed word list:{sort_words(str_list,words_size)}")
# word1=["ant","cat"]
# print(ord(word1[0][0:1]),ord(word1[1][0:1]))