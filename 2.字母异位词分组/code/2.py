from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str in strs:
            count = [0]*26

            for word in str:
                count[ord(word)-ord('a')] += 1

            key = tuple(count)
            result[key].append(str)
        return list(result.values())
        
