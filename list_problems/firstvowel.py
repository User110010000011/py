import re
from collections import deque

WORDS = [
    "try", "sky", "maple", "Epple", "apple", "cable",
    "fyatt", "orange", "grape", "slyde", "fly", "zyde"
]

outlist = deque()
rest = []
new_dict = {}

try:
    for word in WORDS:
        count = 0
        word = word.lower()
        for w in word:
            pos = word.index(w)
            if re.search(r"[aeiou]+", w) and pos == 0 and count <= 0:
                outlist.appendleft(word)
                new_dict[word] = pos
                count += 1
            elif re.search(r"[aeiou]+", w) and pos > 0 and count <= 0:
                outlist.append(word)
                new_dict[word] = pos
                count += 1

    for item in WORDS:
        if item not in outlist:
            rest.append(item)

    rest = sorted(rest)
    outlist.extend(rest)

    set_check = set()
    newlist = deque()
    flag = 0

    for key, val in new_dict.items():
        res_list = []
        for v in outlist:
            if new_dict.get(v) == val and val not in set_check and val == 0:
                res_list.append(v)
                res_list = sorted(res_list, reverse=True)
                flag = 0
            elif new_dict.get(v) == val and val not in set_check:
                res_list.append(v)
                res_list = sorted(res_list)
                flag = 1

        set_check.add(val)

        if flag == 0:
            newlist.extendleft(res_list)
        else:
            newlist.extend(res_list)

    print(newlist)

except ValueError:
    print("The integers and special characters cannot be included ",end="\n")