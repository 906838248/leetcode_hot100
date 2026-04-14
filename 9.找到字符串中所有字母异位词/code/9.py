from typing import List
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        num_p = 0
        result = []
        np = len(p)
        ns = len(s)
        dict_p = defaultdict(int)
        if(np>ns): return result
        
        window = defaultdict(int)
        left = 0
        for i in p:
            dict_p[i] +=1
        for right,char in enumerate(s):
            if((right - left)<np):
                window[char] +=1
            else:

                if(window==dict_p):
                    result.append(left)
                window[char] +=1
                window[s[left]] -= 1
                if window[s[left]]==0:
                    window.pop(s[left])
                left +=1
        if(window==dict_p):
            result.append(left)
        return result

s = "baa"
p = "aa"           
a = Solution()
a.findAnagrams(s,p)

        
            



