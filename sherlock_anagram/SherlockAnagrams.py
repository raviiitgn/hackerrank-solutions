def sherlockAndAnagrams(s):
    freq = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            temp_dict = {}
            for jj in s[i:j]:
                temp_dict[jj] = temp_dict.get(jj,0)+1
            freq[frozenset(temp_dict.items())] = freq.get(frozenset(temp_dict.items()),0)+1
    res = 0
    for count in freq.values():
        res += count*(count-1)/2
    return res

print(sherlockAndAnagrams("kkkk"))
